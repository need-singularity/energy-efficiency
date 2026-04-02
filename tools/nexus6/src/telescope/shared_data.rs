use rayon::prelude::*;

/// Pre-computed shared data that all lenses can use.
/// The distance matrix is computed once and shared read-only.
pub struct SharedData {
    /// Lower-triangle pairwise Euclidean distances, length = N*(N-1)/2
    pub distance_matrix: Vec<f64>,
    /// Number of data points
    pub n: usize,
    /// Dimensionality of each point
    pub d: usize,
}

impl SharedData {
    /// Compute the shared data from raw row-major data.
    /// `n` = number of points, `d` = dimensions per point.
    pub fn compute(data: &[f64], n: usize, d: usize) -> Self {
        assert_eq!(data.len(), n * d, "data length must equal n*d");

        let pair_count = n * (n - 1) / 2;

        // Build flat index list for parallel iteration
        let distances: Vec<f64> = (0..pair_count)
            .into_par_iter()
            .map(|idx| {
                // Convert flat index to (i, j) where i > j
                let (i, j) = flat_to_pair(idx, n);
                let row_i = &data[i * d..(i + 1) * d];
                let row_j = &data[j * d..(j + 1) * d];
                euclidean_dist(row_i, row_j)
            })
            .collect();

        SharedData {
            distance_matrix: distances,
            n,
            d,
        }
    }

    /// Get distance between point i and point j.
    /// Panics if i == j or indices out of range.
    pub fn dist(&self, i: usize, j: usize) -> f64 {
        assert_ne!(i, j, "distance to self is zero, use 0.0 directly");
        let (big, small) = if i > j { (i, j) } else { (j, i) };
        let idx = big * (big - 1) / 2 + small;
        self.distance_matrix[idx]
    }
}

/// Convert a flat lower-triangle index to (i, j) pair where i > j.
fn flat_to_pair(idx: usize, _n: usize) -> (usize, usize) {
    // i*(i-1)/2 + j = idx, find i such that i*(i-1)/2 <= idx
    let i = ((1.0 + (1.0 + 8.0 * idx as f64).sqrt()) / 2.0).floor() as usize;
    let j = idx - i * (i - 1) / 2;
    (i, j)
}

fn euclidean_dist(a: &[f64], b: &[f64]) -> f64 {
    a.iter()
        .zip(b.iter())
        .map(|(x, y)| (x - y) * (x - y))
        .sum::<f64>()
        .sqrt()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_flat_to_pair() {
        // For n=4, pairs: (1,0), (2,0), (2,1), (3,0), (3,1), (3,2)
        assert_eq!(flat_to_pair(0, 4), (1, 0));
        assert_eq!(flat_to_pair(1, 4), (2, 0));
        assert_eq!(flat_to_pair(2, 4), (2, 1));
        assert_eq!(flat_to_pair(3, 4), (3, 0));
        assert_eq!(flat_to_pair(4, 4), (3, 1));
        assert_eq!(flat_to_pair(5, 4), (3, 2));
    }
}
