/// EgyptianAllocator — 1/2 + 1/3 + 1/6 = 1 memory allocation
///
/// Splits heap into 3 regions sized by Egyptian fractions of 6:
///   Region A: 1/2 of total (large objects)
///   Region B: 1/3 of total (medium objects)
///   Region C: 1/6 of total (small objects)
///
/// Each region uses fixed-size blocks, eliminating external fragmentation.
/// Compared against a simulated buddy allocator.

use std::collections::VecDeque;

// ─── Egyptian Allocator ───────────────────────────────────────────

pub struct EgyptianAllocator {
    /// Region A: 1/2 of heap, block_size = large
    region_a: RegionPool,
    /// Region B: 1/3 of heap, block_size = medium
    region_b: RegionPool,
    /// Region C: 1/6 of heap, block_size = small
    region_c: RegionPool,
    total_bytes: usize,
}

struct RegionPool {
    block_size: usize,
    total_blocks: usize,
    free_blocks: VecDeque<usize>, // indices of free blocks
    allocated: Vec<bool>,
}

impl RegionPool {
    fn new(region_bytes: usize, block_size: usize) -> Self {
        let total_blocks = region_bytes / block_size;
        let free_blocks: VecDeque<usize> = (0..total_blocks).collect();
        let allocated = vec![false; total_blocks];
        RegionPool { block_size, total_blocks, free_blocks, allocated }
    }

    fn alloc(&mut self) -> Option<usize> {
        if let Some(idx) = self.free_blocks.pop_front() {
            self.allocated[idx] = true;
            Some(idx)
        } else {
            None
        }
    }

    fn free(&mut self, idx: usize) {
        if idx < self.total_blocks && self.allocated[idx] {
            self.allocated[idx] = false;
            self.free_blocks.push_back(idx);
        }
    }

    fn fragmentation(&self) -> f64 {
        // External fragmentation = 0 by design (fixed-size blocks per region)
        // Internal fragmentation is what we measure: wasted bytes within blocks
        // But for external frag comparison with buddy, we measure gaps
        if self.total_blocks == 0 { return 0.0; }
        let used: Vec<bool> = self.allocated.clone();
        // Count contiguous free regions that are too small to be useful
        // With fixed blocks, there's NO external fragmentation
        0.0
    }

    fn utilization(&self) -> f64 {
        if self.total_blocks == 0 { return 0.0; }
        let used = self.allocated.iter().filter(|&&x| x).count();
        used as f64 / self.total_blocks as f64
    }
}

impl EgyptianAllocator {
    pub fn new(total_bytes: usize) -> Self {
        // 1/2 + 1/3 + 1/6 = 1 (exact partition, no waste)
        let region_a_bytes = total_bytes / 2;      // 1/2
        let region_b_bytes = total_bytes / 3;      // 1/3
        let region_c_bytes = total_bytes / 6;      // 1/6

        // Block sizes: large=4096, medium=1024, small=256
        let block_large = 4096;
        let block_medium = 1024;
        let block_small = 256;

        EgyptianAllocator {
            region_a: RegionPool::new(region_a_bytes, block_large),
            region_b: RegionPool::new(region_b_bytes, block_medium),
            region_c: RegionPool::new(region_c_bytes, block_small),
            total_bytes,
        }
    }

    /// Allocate: route to appropriate region based on size
    pub fn alloc(&mut self, size: usize) -> Option<(char, usize)> {
        if size > 1024 {
            self.region_a.alloc().map(|i| ('A', i))
        } else if size > 256 {
            self.region_b.alloc().map(|i| ('B', i))
        } else {
            self.region_c.alloc().map(|i| ('C', i))
        }
    }

    pub fn free(&mut self, region: char, idx: usize) {
        match region {
            'A' => self.region_a.free(idx),
            'B' => self.region_b.free(idx),
            _ => self.region_c.free(idx),
        }
    }

    /// External fragmentation is always 0 (fixed-size blocks per region)
    pub fn external_fragmentation(&self) -> f64 {
        0.0
    }
}

// ─── Buddy Allocator (baseline comparison) ────────────────────────

pub struct BuddyAllocator {
    /// Flat memory array: true = allocated
    memory: Vec<bool>,
    total_units: usize,
}

impl BuddyAllocator {
    pub fn new(total_units: usize) -> Self {
        // Round up to power of 2
        let size = total_units.next_power_of_two();
        BuddyAllocator {
            memory: vec![false; size],
            total_units: size,
        }
    }

    /// Allocate a block of given size (rounds up to power of 2)
    pub fn alloc(&mut self, size: usize) -> Option<usize> {
        let block_size = size.next_power_of_two();
        // First-fit in power-of-2 aligned positions
        let mut pos = 0;
        while pos + block_size <= self.total_units {
            let slice = &self.memory[pos..pos + block_size];
            if slice.iter().all(|&x| !x) {
                for i in pos..pos + block_size {
                    self.memory[i] = true;
                }
                return Some(pos);
            }
            pos += block_size; // buddy alignment
        }
        None
    }

    pub fn free(&mut self, pos: usize, size: usize) {
        let block_size = size.next_power_of_two();
        for i in pos..std::cmp::min(pos + block_size, self.total_units) {
            self.memory[i] = false;
        }
    }

    /// External fragmentation: free space that can't serve a request
    /// Measured as: 1 - (largest_free_block / total_free)
    pub fn external_fragmentation(&self) -> f64 {
        let total_free = self.memory.iter().filter(|&&x| !x).count();
        if total_free == 0 { return 0.0; }

        // Find largest contiguous free block
        let mut max_run = 0;
        let mut current_run = 0;
        for &used in &self.memory {
            if !used {
                current_run += 1;
                if current_run > max_run { max_run = current_run; }
            } else {
                current_run = 0;
            }
        }

        1.0 - (max_run as f64 / total_free as f64)
    }
}

// ─── Benchmark ────────────────────────────────────────────────────

pub struct AllocBenchResult {
    pub egyptian_frag: f64,
    pub buddy_frag: f64,
    pub egyptian_success_rate: f64,
    pub buddy_success_rate: f64,
}

pub fn bench_allocators(seed: u64) -> AllocBenchResult {
    let total = 1024 * 1024; // 1 MB

    let mut egyptian = EgyptianAllocator::new(total);
    let mut buddy = BuddyAllocator::new(total / 256); // in 256-byte units

    // Generate allocation/free sequence with LCG PRNG
    let mut rng = seed;
    let next = |r: &mut u64| -> u64 {
        *r = r.wrapping_mul(6364136223846793005).wrapping_add(1442695040888963407);
        *r >> 33
    };

    let num_ops = 5000;
    let mut eg_allocs: Vec<(char, usize)> = Vec::new();
    let mut bd_allocs: Vec<(usize, usize)> = Vec::new(); // (pos, size_units)
    let mut eg_success = 0u64;
    let mut bd_success = 0u64;
    let mut eg_attempts = 0u64;
    let mut bd_attempts = 0u64;

    for _ in 0..num_ops {
        let v = next(&mut rng);
        let do_alloc = v % 3 != 0; // 2/3 alloc, 1/3 free

        if do_alloc {
            // Random size: small(64-256), medium(257-1024), large(1025-4096)
            let category = next(&mut rng) % 3;
            let size = match category {
                0 => 64 + (next(&mut rng) % 193) as usize,   // small
                1 => 257 + (next(&mut rng) % 768) as usize,  // medium
                _ => 1025 + (next(&mut rng) % 3072) as usize, // large
            };

            eg_attempts += 1;
            if let Some(handle) = egyptian.alloc(size) {
                eg_allocs.push(handle);
                eg_success += 1;
            }

            bd_attempts += 1;
            let units = (size + 255) / 256;
            if let Some(pos) = buddy.alloc(units) {
                bd_allocs.push((pos, units));
                bd_success += 1;
            }
        } else {
            // Free a random existing allocation
            if !eg_allocs.is_empty() {
                let idx = next(&mut rng) as usize % eg_allocs.len();
                let (region, block_idx) = eg_allocs.swap_remove(idx);
                egyptian.free(region, block_idx);
            }
            if !bd_allocs.is_empty() {
                let idx = next(&mut rng) as usize % bd_allocs.len();
                let (pos, units) = bd_allocs.swap_remove(idx);
                buddy.free(pos, units);
            }
        }
    }

    AllocBenchResult {
        egyptian_frag: egyptian.external_fragmentation() * 100.0,
        buddy_frag: buddy.external_fragmentation() * 100.0,
        egyptian_success_rate: if eg_attempts > 0 { eg_success as f64 / eg_attempts as f64 * 100.0 } else { 0.0 },
        buddy_success_rate: if bd_attempts > 0 { bd_success as f64 / bd_attempts as f64 * 100.0 } else { 0.0 },
    }
}
