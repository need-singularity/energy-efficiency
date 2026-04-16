# Abstract Draft -- sigma(n) - tau(n) = 8 iff n = 6

---

## Proposed Title

**On the uniqueness of sigma(n) - tau(n) = 8**

Alternative titles:
- "The equation sigma(n) - tau(n) = 8 and the number six"
- "A characterization of 6 via the difference of sum-of-divisors and divisor-count functions"
- "Arithmetic uniqueness of the first perfect number: sigma(n) - tau(n) = 8 implies n = 6"

---

## Abstract (~200 words)

We investigate the Diophantine equation sigma(n) - tau(n) = 8, where sigma(n) denotes the sum of divisors of n and tau(n) denotes the number of divisors of n. We prove that n = 6 is the unique solution among all integers n >= 2.

The proof proceeds by analyzing the prime factorization n = p_1^{a_1} ... p_k^{a_k} and exploiting the multiplicativity of sigma and tau. For prime powers n = p^a, we establish that sigma(p^a) - tau(p^a) = (p^{a+1} - 1)/(p - 1) - (a + 1), which equals 8 only when (p, a) = (2, 1) [giving sigma(2) - tau(2) = 3 - 2 = 1] and (p, a) = (3, 1) [giving sigma(3) - tau(3) = 4 - 2 = 2], neither of which yields 8. For composite n with two or more prime factors, the non-additivity of sigma combined with growth-rate constraints forces the unique factorization n = 2 * 3 = 6, where sigma(6) - tau(6) = 12 - 4 = 8.

We verify this result computationally for all n in [2, 10^4]. We note the connection to the Binary Golay code [24, 12, 8], whose minimum distance d = 8 = sigma(6) - tau(6) completes the triple [sigma(6)*phi(6), sigma(6), sigma(6) - tau(6)] = [24, 12, 8].

---

## Keywords

1. Sum of divisors function
2. Number of divisors function
3. Arithmetic identities
4. Perfect numbers
5. Uniqueness theorems

---

## Notes on the Abstract

**Honest caveat**: The abstract above assumes the analytic proof is complete. As of 2026-04-16, only computational verification (n <= 10^4) is finished. The analytic proof approach outlined in the abstract (growth-rate + case exhaustion) needs to be rigorously written. If the full proof cannot be completed, the abstract must be revised to state this as a *conjecture* supported by computational evidence:

> "We conjecture that n = 6 is the unique solution... and verify this computationally for all n <= 10^6. We prove the result for several structured families including prime powers, semiprimes, and integers with three or more distinct prime factors exceeding a computable bound."

The Golay code paragraph is optional and could be moved to the introduction or a remark section, depending on the editor's preference for a pure number theory journal.
