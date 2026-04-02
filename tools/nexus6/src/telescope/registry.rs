use std::collections::HashMap;

/// Category of a lens in the registry.
#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]
pub enum LensCategory {
    /// The 22 foundational lenses from the telescope specification.
    Core,
    /// The 10 domain-specific lens combinations.
    DomainCombo,
    /// Extended lenses added through incremental expansion (toward 411).
    Extended,
    /// User-defined custom lenses.
    Custom,
}

/// Metadata entry for a single lens in the registry.
#[derive(Debug, Clone)]
pub struct LensEntry {
    pub name: String,
    pub category: LensCategory,
    pub description: String,
    /// Domains where this lens is most effective.
    pub domain_affinity: Vec<String>,
    /// Other lenses that pair well with this one.
    pub complementary: Vec<String>,
}

/// Central registry for all lens metadata.
///
/// This is a *metadata* registry — it stores descriptions, affinities and
/// relationships. The actual scan logic lives in the `Lens` trait implementors.
/// The registry enables discovery ("which lenses suit domain X?") and
/// incremental growth toward the full 411-lens set.
pub struct LensRegistry {
    entries: HashMap<String, LensEntry>,
}

impl LensRegistry {
    /// Create a new registry pre-populated with the 22 Core lenses.
    pub fn new() -> Self {
        let mut reg = LensRegistry {
            entries: HashMap::new(),
        };
        for entry in super::core_lenses::core_lens_entries() {
            reg.entries.insert(entry.name.clone(), entry);
        }
        reg
    }

    /// Register a new lens entry. Overwrites if name already exists.
    pub fn register(&mut self, entry: LensEntry) {
        self.entries.insert(entry.name.clone(), entry);
    }

    /// Look up a lens by name.
    pub fn get(&self, name: &str) -> Option<&LensEntry> {
        self.entries.get(name)
    }

    /// Return all lenses belonging to the given category.
    pub fn by_category(&self, cat: LensCategory) -> Vec<&LensEntry> {
        self.entries
            .values()
            .filter(|e| e.category == cat)
            .collect()
    }

    /// Recommend lenses for a given domain string (case-insensitive substring match).
    pub fn for_domain(&self, domain: &str) -> Vec<&LensEntry> {
        let domain_lower = domain.to_lowercase();
        self.entries
            .values()
            .filter(|e| {
                e.domain_affinity
                    .iter()
                    .any(|d| d.to_lowercase().contains(&domain_lower))
            })
            .collect()
    }

    /// Total number of registered lenses.
    pub fn len(&self) -> usize {
        self.entries.len()
    }

    /// Whether the registry is empty.
    pub fn is_empty(&self) -> bool {
        self.entries.is_empty()
    }

    /// Iterator over all entries.
    pub fn iter(&self) -> impl Iterator<Item = (&String, &LensEntry)> {
        self.entries.iter()
    }
}

impl Default for LensRegistry {
    fn default() -> Self {
        Self::new()
    }
}
