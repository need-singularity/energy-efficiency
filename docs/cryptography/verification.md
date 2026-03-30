# N6 Cryptography Hypotheses -- Independent Verification

## Methodology

Each hypothesis (H-CR-1 through H-CR-48) is evaluated on three axes:

1. **Math check**: Does the n=6 derivation hold arithmetically?
2. **Fact check**: Does the predicted value match real-world standards?
3. **Causality check**: Is the n=6 expression the *reason* the value was chosen,
   or is it a post-hoc fit? Cryptographic parameters were chosen for specific
   engineering/security reasons (diffusion, birthday bounds, performance).
   Matching a number is not the same as explaining it.

### Grading Scale

| Grade | Meaning |
|-------|---------|
| EXACT | Math correct, value matches standard, derivation is at least plausible |
| CLOSE | Math correct, value matches, but derivation is clearly retrofitted |
| WEAK | Value matches only approximately, or the n=6 expression is one of many possible decompositions |
| FAIL | Value is wrong, or the claimed match is misleading |
| UNVERIFIABLE | Claim cannot be checked against public data |

### Critical Context: The Overfitting Problem

n=6 produces the following small-number toolkit:

```
  sigma=12, tau=4, phi=2, sopfr=5, mu=1, J2=24, lambda=2, n=6
```

With two-term arithmetic (+, -, *, /, ^) on these 8 values, you can generate
most small integers and most powers of 2 up to 2^12. Cryptographic parameters
are overwhelmingly powers of 2 (128, 256, 512, 1024, 2048, 4096) because
computers use binary. Any power of 2 from 2^1 to 2^12 can be trivially
expressed as 2^(some combination of sigma, tau, phi, sopfr, mu).

This does not mean n=6 *caused* these choices. It means the parameter space
is small enough that coincidental matches are *expected*.

---

## Tier 1: Symmetric Encryption (AES)

### H-CR-1: AES Block Size = 2^(sigma-sopfr) = 2^7 = 128

- **Math**: 12 - 5 = 7; 2^7 = 128. Correct.
- **Fact**: AES block = 128 bits. Correct.
- **Causality**: Rijndael supported 128/192/256-bit blocks. NIST fixed 128
  for standardization. The choice of 128 was driven by: (a) 64-bit blocks
  had birthday-bound problems at 2^32 blocks, (b) 128 was the next power of 2,
  (c) hardware word alignment. The expression "sigma - sopfr" has no known
  connection to any of these reasons.
- **Grade: CLOSE** -- value matches, derivation is retrofitted.

### H-CR-2: AES-128 Key = 2^(sigma-sopfr) = 128

- **Math**: Same as H-CR-1. Correct.
- **Fact**: AES-128 key = 128 bits. Correct.
- **Causality**: Key = block size is the simplest design choice. Not derived
  from number theory.
- **Grade: CLOSE**

### H-CR-3: AES-192 Key = sigma * 2^tau = 12 * 16 = 192

- **Math**: 12 * 16 = 192. Correct.
- **Fact**: AES-192 key = 192 bits. Correct.
- **Causality**: 192 = 128 + 64 = 1.5 * 128. It exists to fill the gap between
  128 and 256. The expression "sigma * 2^tau" is one of many ways to reach 192.
  Also note: the hypothesis text itself gives *two different* derivations
  (sigma * 2^tau and 128 * 3/2), which is a sign of curve-fitting.
- **Grade: CLOSE**

### H-CR-4: AES-256 Key = 2^(sigma-tau) = 2^8 = 256

- **Math**: 12 - 4 = 8; 2^8 = 256. Correct.
- **Fact**: AES-256 = 256 bits. Correct.
- **Causality**: 256 = 2^8 is the obvious next power of 2 after 128. 8 = sigma-tau
  is one decomposition of 8; also 8 = 2^3, 8 = 2*4, etc.
- **Grade: CLOSE**

### H-CR-5: AES-128 Rounds = sopfr * phi = 5 * 2 = 10

- **Math**: 5 * 2 = 10. Correct.
- **Fact**: AES-128 = 10 rounds. Correct.
- **Causality**: The Rijndael designers chose rounds based on wide-trail
  strategy analysis. 10 rounds gives sufficient margin over the best known
  differential/linear attack complexity. 10 = 5*2 = 2*5 = many decompositions.
  The expression "sopfr * phi" is cherry-picked. You could equally write
  10 = sigma - phi, or 10 = n + tau, or 10 = 2 * sopfr.
- **Grade: WEAK** -- correct value, but the specific decomposition is arbitrary.

### H-CR-6: AES-192 Rounds = sigma = 12

- **Math**: sigma(6) = 12. Correct.
- **Fact**: AES-192 = 12 rounds. Correct.
- **Causality**: AES rounds follow the formula Nr = max(Nk, Nb) + 6, where
  Nk = key length / 32 and Nb = block length / 32 = 4. For AES-192:
  Nr = max(6, 4) + 6 = 12. The "+6" in Rijndael's formula is a security
  margin constant, not sigma(6). That said, this is the strongest n=6 match
  in the AES tier: the actual design formula literally contains "+6".
- **Grade: CLOSE** -- the Rijndael formula does use 6, but it is n not sigma.

### H-CR-7: AES-256 Rounds = sigma + phi = 12 + 2 = 14

- **Math**: 12 + 2 = 14. Correct.
- **Fact**: AES-256 = 14 rounds. Correct.
- **Causality**: Rijndael formula: Nr = max(8, 4) + 6 = 14. Again, the "+6"
  is the security margin. Writing it as "sigma + phi = 12 + 2" reshuffles the
  actual formula (8 + 6 = 14).
- **Grade: CLOSE**

### H-CR-8: AES State = tau x tau = 4x4

- **Math**: tau(6) = 4; 4x4 = 16 bytes = 128 bits. Correct.
- **Fact**: AES state = 4x4 byte matrix. Correct.
- **Causality**: 128 bits / 8 bits per byte = 16 bytes; 4x4 is the only square
  arrangement. The choice of 4 is forced by 128-bit block size and byte-level
  operations. tau(6) = 4 is coincidental.
- **Grade: CLOSE**

---

## Tier 2: Hash Functions (SHA)

### H-CR-9: SHA-256 Output = 2^(sigma-tau) = 2^8 = 256

- **Math**: 12 - 4 = 8; 2^8 = 256. Correct.
- **Fact**: SHA-256 = 256 bits. Correct.
- **Causality**: Same as H-CR-4. 256 = 2^8 needs no number-theoretic
  justification. It was chosen to provide 128-bit collision resistance (birthday
  bound), matching AES-128 security level.
- **Grade: CLOSE**

### H-CR-10: SHA-256 Block = 2^(sigma-tau+1) = 2^9 = 512

- **Math**: 12 - 4 + 1 = 9; 2^9 = 512. Correct.
- **Fact**: SHA-256 block = 512 bits. Correct.
- **Causality**: Block = 2 * output is a standard Merkle-Damgard design
  choice. The "+1" in the exponent is not from n=6 arithmetic; it is from
  the doubling.
- **Grade: CLOSE**

### H-CR-11: SHA-256 Rounds = 2^n = 2^6 = 64

- **Math**: 2^6 = 64. Correct.
- **Fact**: SHA-256 = 64 rounds. Correct.
- **Causality**: SHA-256 uses 64 rounds because it processes 64 message schedule
  words (one per round), derived from the 16-word (512-bit) input block expanded
  to 64 words. 64 = 2^6 is a natural power of 2. That n = 6 matches the exponent
  is a coincidence -- the SHA family was designed around word counts, not perfect
  number theory.
- **Grade: CLOSE** -- numerically exact, causally unrelated.

### H-CR-12: SHA-512 Output = 2^(sigma-tau+1) = 2^9 = 512

- **Math**: 9 = 12 - 4 + 1. Correct.
- **Fact**: SHA-512 = 512 bits. Correct.
- **Causality**: 512 = 2 * 256 = next power of 2. Same pattern.
- **Grade: CLOSE**

### H-CR-13: SHA-256 State Words = sigma - tau = 8

- **Math**: 12 - 4 = 8. Correct.
- **Fact**: SHA-256 uses 8 working variables (a-h), 8 initial hash values. Correct.
- **Causality**: 8 words * 32 bits = 256 bits = output size. The state size is
  determined by the output size, not by sigma - tau.
- **Grade: CLOSE**

---

## Tier 3: Asymmetric Encryption (RSA)

### H-CR-14: RSA-2048 = 2^(sigma-mu) = 2^11 = 2048

- **Math**: 12 - 1 = 11; 2^11 = 2048. Correct.
- **Fact**: RSA-2048 is the current standard. Correct.
- **Causality**: RSA key sizes are chosen based on estimated difficulty of
  factoring (GNFS complexity). 2048 bits provides ~112 bits of security.
  The choice of 2048 = 2^11 is a power-of-2 convenience. sigma - mu = 11 is one
  of many ways to get 11 from {1,2,4,5,6,12,24}.
- **Grade: CLOSE**

### H-CR-15: RSA-4096 = 2^sigma = 2^12 = 4096

- **Math**: 2^12 = 4096. Correct.
- **Fact**: RSA-4096 is used for high-security applications. Correct.
- **Causality**: 4096 = 2 * 2048. Power-of-2 doubling. sigma = 12 matching the
  exponent is coincidental.
- **Grade: CLOSE**

### H-CR-16: RSA Prime Size = key/phi = 2048/2 = 1024

- **Math**: 2048 / 2 = 1024. Correct.
- **Fact**: RSA-2048 uses two ~1024-bit primes. Correct.
- **Causality**: RSA is defined as n = p*q where p and q are roughly equal primes.
  Half the key size per prime is definitional, not an n=6 insight. Using phi(6)=2
  to explain "two primes" is tautological -- RSA uses two primes by construction.
- **Grade: WEAK** -- trivially true, not insightful.

### H-CR-17: RSA Public Exponent = F_tau = F_4 = 65537

- **Math**: tau(6) = 4; F_4 = 2^(2^4) + 1 = 65537. Correct.
- **Fact**: Standard RSA e = 65537. Correct.
- **Causality**: 65537 is the largest known Fermat prime. It is chosen because:
  (a) it is prime, (b) it has low Hamming weight (fast exponentiation),
  (c) it is large enough to resist small-exponent attacks. The connection to
  tau(6) is that tau(6) = 4, and F_4 happens to be the last Fermat prime.
  This is the strongest coincidence in the document. However, F_4 was known
  since Euler; the connection is that tau(6) indexes it, not that n=6 *caused*
  the choice.
- **Grade: EXACT** -- genuinely interesting numerical coincidence.

---

## Tier 4: Stream Cipher (ChaCha20)

### H-CR-18: ChaCha20 Rounds = J_2 - tau = 24 - 4 = 20

- **Math**: 24 - 4 = 20. Correct.
- **Fact**: ChaCha20 = 20 rounds. Correct.
- **Causality**: Bernstein chose 20 rounds (originally Salsa20/20) based on
  cryptanalysis margin. 8 rounds were broken, 12 rounds had theoretical
  attacks, 20 provided ample margin. The expression J_2(6) - tau(6) is
  retrofitted; 20 can also be written as 4 * sopfr, or sigma + sigma - tau,
  or many other ways.
- **Grade: CLOSE**

### H-CR-19: ChaCha20 State = tau^2 = 16 words

- **Math**: 4^2 = 16. Correct.
- **Fact**: ChaCha20 state = 16 x 32-bit words = 512 bits. Correct.
- **Causality**: 512-bit state = 256-bit key + 64-bit counter + 64-bit nonce +
  128-bit constant. 512 bits / 32 bits per word = 16 words. The state breakdown
  (4 + 8 + 2 + 2) matches n=6 values, but these sizes are determined by security
  requirements (256-bit key) and practical constraints (32-bit words for ARM/x86).
- **Grade: CLOSE**

### H-CR-20: ChaCha Quarter Round = tau = 4 ARX ops

- **Math**: tau(6) = 4. Correct.
- **Fact**: ChaCha quarter round has 4 ARX operations. Correct.
- **Causality**: A "quarter round" operates on 4 words (hence "quarter" of 16).
  Each word gets one ARX operation. 4 ops is structurally required, not a free
  design parameter.
- **Grade: WEAK** -- the number 4 is forced by the quarter-round definition.

---

## Tier 5: Elliptic Curve Cryptography

### H-CR-21: P-256 Field = 2^(sigma-tau) = 256

- **Math**: Same as H-CR-4/H-CR-9. Correct.
- **Fact**: NIST P-256 = 256-bit prime field. Correct.
- **Causality**: 256-bit ECC provides ~128-bit security. Same power-of-2
  reasoning as SHA-256 and AES-256.
- **Grade: CLOSE**

### H-CR-22: P-384 Field = sigma * 2^sopfr = 12 * 32 = 384

- **Math**: 12 * 32 = 384. Correct.
- **Fact**: NIST P-384 = 384-bit prime field. Correct.
- **Causality**: 384 = 256 * 1.5 = 3 * 128. Chosen to match ~192-bit security.
  The expression sigma * 2^sopfr is one of many routes to 384.
- **Grade: CLOSE**

### H-CR-23: Ed25519 = 2^(sigma-tau) - 1 = 255

- **Math**: 2^8 - 1 = 255. Correct.
- **Fact**: Curve25519 operates over a field near 2^255. Correct.
- **Causality**: The prime 2^255 - 19 was chosen by Bernstein for fast modular
  arithmetic (close to a power of 2). The "255" comes from wanting ~128-bit
  security with a Mersenne-like prime, not from 2^8 - 1.
- **Grade: CLOSE**

### H-CR-24: ECC Cofactors in {1, 2, 4, 8}

- **Math**: These are indeed n=6-related values. Correct.
- **Fact**: P-256 cofactor = 1, Curve25519 cofactor = 8, Ed448 cofactor = 4. Correct.
- **Causality**: Cofactors are small powers of 2 by construction (curves are
  chosen so that cofactor * prime-order subgroup = curve order). Small powers
  of 2 always match n=6 values because n=6 values include {1, 2, 4, 8}.
  This is circular.
- **Grade: WEAK** -- any small power of 2 would match.

---

## Tier 6: HMAC & Key Derivation

### H-CR-25: HMAC = phi = 2 hash passes

- **Math**: phi(6) = 2. Correct.
- **Fact**: HMAC does 2 hash calls. Correct.
- **Causality**: HMAC uses 2 passes to prevent length-extension attacks.
  The number 2 is the minimum needed; using phi(6) = 2 to explain "two passes"
  is not meaningful -- any construction with an inner and outer operation has 2
  steps.
- **Grade: WEAK** -- trivially 2.

### H-CR-26: HMAC Key Block = 2^(sigma-tau+1) = 512

- **Math**: 2^9 = 512. Correct.
- **Fact**: HMAC-SHA256 key block = 512 bits (= SHA-256 block size). Correct.
- **Causality**: HMAC key block = underlying hash block size. This is not a
  separate parameter; it is inherited from SHA-256.
- **Grade: CLOSE** -- correct but derivative of H-CR-10.

### H-CR-27: HKDF = phi = 2 phases

- **Math**: phi(6) = 2. Correct.
- **Fact**: HKDF = Extract + Expand = 2 phases. Correct.
- **Causality**: Same issue as H-CR-25. Any two-step process matches phi=2.
  The two phases serve distinct purposes (entropy extraction vs. key expansion).
- **Grade: WEAK** -- trivially 2.

### H-CR-28: PBKDF2 Iteration Count Base = sopfr * phi = 10

- **Math**: 5 * 2 = 10. Correct.
- **Fact**: PBKDF2 minimums are in multiples of powers of 10, but the actual
  recommended counts (600,000 per OWASP 2023, 10,000 minimum per older NIST)
  are chosen based on hardware speed, not number theory.
- **Causality**: Saying "10,000 = 10 * 1000" and attributing the "10" to n=6
  while ignoring the "1000" is selective. The base-10 numbering system, not
  perfect numbers, explains why recommendations are round decimal numbers.
- **Grade: WEAK**

---

## Tier 7: Post-Quantum Cryptography

### H-CR-29: Kyber n = 2^(sigma-tau) = 256

- **Math**: Same as H-CR-4. Correct.
- **Fact**: CRYSTALS-Kyber / ML-KEM uses n=256. Correct.
- **Causality**: n=256 is chosen for efficient NTT (Number Theoretic Transform)
  computation, which requires a power of 2. 256 gives adequate security with
  reasonable performance. Same power-of-2 reasoning applies.
- **Grade: CLOSE**

### H-CR-30: Kyber Ring = Z_q[x]/(x^256+1)

- **Math**: x^(2^8) + 1. Same as above.
- **Fact**: Correct.
- **Causality**: Duplicate of H-CR-29. The ring dimension is the same parameter.
  The hypothesis acknowledges that the modulus q=3329 has no n=6 connection.
- **Grade: CLOSE** -- but this is the same claim as H-CR-29, not independent.

### H-CR-31: NIST PQC Security Levels = sopfr = 5

- **Math**: sopfr(6) = 5. Correct.
- **Fact**: NIST defined 5 security levels. Correct.
- **Causality**: NIST chose 5 levels to bracket the 3 AES key sizes (128/192/256)
  with symmetric and hash-based equivalences. Having 5 categories for a
  standardization process is an organizational choice, not a mathematical
  inevitability.
- **Grade: WEAK** -- coincidence with a small integer.

### H-CR-32: Leech Lattice as PQC Foundation

- **Math**: J_2(6) = 24 = Leech lattice dimension. Correct.
- **Fact**: The Leech lattice is a mathematical object of interest in lattice
  theory, but practical lattice-based cryptography (Kyber, Dilithium) does NOT
  use the Leech lattice. They use module lattices in much higher dimensions.
- **Causality**: The Leech lattice is studied for sphere packing, not for
  cryptographic hardness assumptions. The claim that it forms the "foundation"
  of PQC is speculative.
- **Grade: UNVERIFIABLE** -- theoretical speculation, not supported by current PQC designs.

---

## Tier 8: Zero-Knowledge Proofs

### H-CR-33: ZK Pairing Groups = tau = 4

- **Math**: tau(6) = 4. Correct.
- **Fact**: Pairing-based ZK uses G1, G2, GT, and the scalar field. Counting
  these as "4 groups" is reasonable but debatable -- GT is a multiplicative
  group and the scalar field is not typically called a "group" in this context.
  Standard descriptions say "3 groups (G1, G2, GT) with a bilinear map."
- **Causality**: The number of groups in a bilinear pairing is determined by the
  mathematical definition of pairings, not by divisor counts.
- **Grade: WEAK** -- the count of "4" requires including the scalar field, which
  is non-standard.

### H-CR-34: Sigma Protocol = sigma/tau = 3 rounds

- **Math**: 12/4 = 3. Correct.
- **Fact**: Sigma protocols have 3 rounds (commit, challenge, response). Correct.
- **Causality**: The 3-round structure comes from the definition of interactive
  proof systems (prover sends, verifier sends, prover sends). Saying sigma/tau = 3
  is post-hoc. Three-move protocols are the simplest non-trivial interactive proofs.
- **Grade: CLOSE** -- correct value, retrofitted explanation.

### H-CR-35: Groth16 Proof = sigma/tau = 3 elements

- **Math**: 3. Correct.
- **Fact**: Groth16 proof = 2 G1 elements + 1 G2 element = 3 elements. Correct.
- **Causality**: Groth16's proof size comes from the algebraic structure of
  the QAP (Quadratic Arithmetic Program) encoding. 3 is the minimum possible
  for this proof system.
- **Grade: CLOSE**

### H-CR-36: BLS12-381 Embedding Degree = sigma = 12

- **Math**: sigma(6) = 12. Correct.
- **Fact**: BLS12-381 and BN254 both have embedding degree k=12. Correct.
- **Causality**: Embedding degree 12 is chosen because it provides a good
  balance between security and efficiency for pairing computation at the
  128-bit security level. k=12 means the pairing target group is in F_{p^12}.
  The value 12 is determined by the BLS curve construction method, not by
  perfect number theory. That said, 12 appearing naturally in both contexts
  is a noteworthy coincidence.
- **Grade: EXACT** -- genuinely interesting coincidence.

---

## Tier 9: Digital Signatures

### H-CR-37: ECDSA Signature = phi = 2 components

- **Math**: phi(6) = 2. Correct.
- **Fact**: ECDSA/EdDSA/Schnorr signatures are (r, s) pairs. Correct.
- **Causality**: A Schnorr-like signature inherently has 2 components: a
  commitment (r) and a response (s). This is a structural minimum, like
  HMAC having 2 passes. phi(6) = 2 adds no insight.
- **Grade: WEAK** -- trivially 2.

### H-CR-38: EdDSA Deterministic Nonce = mu = 1

- **Math**: mu(6) = 1. The connection to "determinism" is metaphorical, not
  mathematical.
- **Fact**: EdDSA uses deterministic nonces. Correct.
- **Causality**: This is a philosophical analogy ("squarefree = no repetition =
  deterministic"), not a mathematical derivation. mu(6) = 1 does not predict
  or constrain nonce generation.
- **Grade: WEAK** -- metaphor, not derivation.

### H-CR-39: ML-DSA-65 Params = (k,l) = (6,5) = (n, sopfr)

- **Math**: n = 6, sopfr(6) = 5; ML-DSA-65 has (k,l) = (6,5). Correct.
- **Fact**: ML-DSA-65 (formerly Dilithium3) uses k=6, l=5. Correct.
- **Causality**: This is the most striking numerical coincidence in the entire
  document. ML-DSA parameter selection was based on lattice security estimates
  and performance optimization. The (6,5) pair provides Level 3 security.
  The match with (n, sopfr(6)) is almost certainly coincidental, but it is
  remarkably specific.
- **Grade: EXACT** -- remarkable coincidence worth noting.

### H-CR-40: Signature Verify Ratio

- **Math**: Various approximate ratios.
- **Fact**: ECDSA verify is roughly 1.5-2x sign cost. RSA verify is much
  faster than sign (because e=65537 is small vs. large d).
- **Causality**: The ratios are approximate and depend heavily on implementation.
  Claiming phi=2 for ECC and 1/6 for RSA is hand-wavy.
- **Grade: WEAK** -- approximate at best.

---

## Tier 10: Entropy & Random Number Generation

### H-CR-41: Entropy Pool = 2^sigma = 2^12 = 4096

- **Math**: 2^12 = 4096. Correct.
- **Fact**: The Linux kernel historically used a 4096-bit entropy pool.
  NOTE: As of Linux 5.18+ (2022), the entropy pool model was significantly
  reworked by Jason Donenfeld; the old fixed-size pool concept no longer applies
  in the same way.
- **Causality**: 4096 = 2^12 is a standard page-size-aligned buffer. Power-of-2
  sizing is universal in systems programming.
- **Grade: CLOSE**

### H-CR-42: DRBG Reseed Interval = 2^(sigma*tau) = 2^48

- **Math**: 12 * 4 = 48; 2^48. Correct.
- **Fact**: NIST SP 800-90A specifies max reseed interval of 2^48 for CTR_DRBG
  and Hash_DRBG. Correct.
- **Causality**: 2^48 was chosen as a conservative limit based on security
  analysis of the DRBG constructions. sigma * tau = 48 is one decomposition;
  48 = 6 * 8 = 3 * 16 = many others. However, this is a less "obvious" power
  of 2 than 128 or 256, so the match is more noteworthy.
- **Grade: EXACT** -- specific enough to be interesting.

### H-CR-43: Min Entropy = ln(2) nats/bit

- **Math**: This is a unit conversion (1 bit = ln(2) nats), not an n=6
  derivation.
- **Fact**: Correct by definition.
- **Causality**: This is not a hypothesis; it is the definition of the
  relationship between bits and nats. No n=6 connection.
- **Grade: FAIL** -- this is a unit conversion, not a prediction.

### H-CR-44: RNG Conditioning Ratio = sigma/tau = 3:1

- **Math**: 12/4 = 3. Correct.
- **Fact**: Real conditioning ratios vary widely (2:1 to 10:1+) depending on
  source quality. Intel's RDRAND internals are not public.
- **Causality**: The "~3:1" claim is unsubstantiated. Different entropy sources
  have different ratios.
- **Grade: UNVERIFIABLE**

---

## Tier 11: Protocol-Level Parameters

### H-CR-45: TLS 1.3 Cipher Suites = sopfr = 5

- **Math**: sopfr(6) = 5. Correct.
- **Fact**: RFC 8446 defines 5 cipher suites for TLS 1.3. Correct.
- **Causality**: The 5 suites are: 3 AES variants (128-GCM, 256-GCM, 128-CCM)
  + 1 ChaCha20 + 1 AES-128-CCM-8. The count of 5 reflects the practical
  combinations of {AES-128, AES-256, ChaCha20} x {GCM, CCM, CCM-8, Poly1305}
  filtered for usefulness. It is an engineering decision, not derivable from
  sopfr(6).
- **Grade: CLOSE** -- correct count, coincidental.

### H-CR-46: TLS 1.3 Handshake = mu = 1 RTT

- **Math**: mu(6) = 1. Correct.
- **Fact**: TLS 1.3 full handshake = 1-RTT. Correct.
- **Causality**: 1-RTT was a primary design goal for TLS 1.3 (latency
  reduction). Using mu(6) = 1 to explain "one round trip" is like using it to
  explain any singleton quantity. The number 1 is universal.
- **Grade: WEAK** -- the number 1 matches everything.

### H-CR-47: Certificate Chain = sigma/tau = 3

- **Math**: 12/4 = 3. Correct.
- **Fact**: Most HTTPS chains are 3 deep (Root, Intermediate, Leaf). Correct.
- **Causality**: The 3-level hierarchy reflects operational PKI practice:
  root CAs are kept offline, intermediate CAs issue end-entity certificates.
  3 is a natural hierarchy depth.
- **Grade: CLOSE**

### H-CR-48: GCM Block Limit = 2^(sigma*phi) = 2^24

- **Math**: 12 * 2 = 24; 2^24. Correct.
- **Fact**: The claimed "practical limit" of 2^24 blocks per nonce is
  misleading. NIST SP 800-38D allows up to 2^39 - 256 bits of plaintext per
  invocation. The 2^32 invocations-per-key limit is the more commonly cited
  bound. There is a 2^24 figure for certain multi-key GCM security bounds in
  academic literature, but it is not *the* standard limit.
- **Causality**: The hypothesis selects a specific bound from among several
  GCM security limits to match 2^24.
- **Grade: WEAK** -- cherry-picked limit.

---

## Summary Table

| ID | Hypothesis | Value Match | Grade | Notes |
|----|-----------|-------------|-------|-------|
| H-CR-1 | AES block = 128 | Yes | CLOSE | Power of 2 retrofit |
| H-CR-2 | AES-128 key = 128 | Yes | CLOSE | Same as block |
| H-CR-3 | AES-192 key = 192 | Yes | CLOSE | Multiple derivations given |
| H-CR-4 | AES-256 key = 256 | Yes | CLOSE | 2^8 is obvious |
| H-CR-5 | AES-128 rounds = 10 | Yes | WEAK | Arbitrary decomposition |
| H-CR-6 | AES-192 rounds = 12 | Yes | CLOSE | Rijndael formula uses +6 |
| H-CR-7 | AES-256 rounds = 14 | Yes | CLOSE | Rijndael formula uses +6 |
| H-CR-8 | AES state = 4x4 | Yes | CLOSE | Forced by 128-bit block |
| H-CR-9 | SHA-256 = 256 | Yes | CLOSE | Same as AES-256 reasoning |
| H-CR-10 | SHA-256 block = 512 | Yes | CLOSE | 2x output is standard |
| H-CR-11 | SHA-256 rounds = 64 | Yes | CLOSE | 2^6 coincidence |
| H-CR-12 | SHA-512 = 512 | Yes | CLOSE | Next power of 2 |
| H-CR-13 | SHA-256 state = 8 words | Yes | CLOSE | 256/32 = 8 |
| H-CR-14 | RSA-2048 | Yes | CLOSE | Power of 2 |
| H-CR-15 | RSA-4096 | Yes | CLOSE | Power of 2 |
| H-CR-16 | RSA primes = 1024 | Yes | WEAK | Definitionally half |
| H-CR-17 | RSA e = F_4 = 65537 | Yes | EXACT | Genuinely interesting |
| H-CR-18 | ChaCha20 = 20 rounds | Yes | CLOSE | Retrofitted expression |
| H-CR-19 | ChaCha state = 16 words | Yes | CLOSE | 512/32 = 16 |
| H-CR-20 | ChaCha QR = 4 ops | Yes | WEAK | Forced by definition |
| H-CR-21 | P-256 = 256 | Yes | CLOSE | Same 2^8 pattern |
| H-CR-22 | P-384 = 384 | Yes | CLOSE | 3 * 128 |
| H-CR-23 | Ed25519 = 255 | Yes | CLOSE | Mersenne-like prime choice |
| H-CR-24 | ECC cofactors | Yes | WEAK | Small powers of 2 always match |
| H-CR-25 | HMAC = 2 passes | Yes | WEAK | Trivially 2 |
| H-CR-26 | HMAC block = 512 | Yes | CLOSE | Inherited from SHA-256 |
| H-CR-27 | HKDF = 2 phases | Yes | WEAK | Trivially 2 |
| H-CR-28 | PBKDF2 base = 10 | Partial | WEAK | Base-10 numbering system |
| H-CR-29 | Kyber n = 256 | Yes | CLOSE | NTT requires power of 2 |
| H-CR-30 | Kyber ring degree | Yes | CLOSE | Duplicate of H-CR-29 |
| H-CR-31 | PQC 5 levels | Yes | WEAK | Small integer coincidence |
| H-CR-32 | Leech lattice PQC | N/A | UNVERIFIABLE | Speculative |
| H-CR-33 | ZK pairing = 4 groups | Debatable | WEAK | Non-standard counting |
| H-CR-34 | Sigma protocol = 3 | Yes | CLOSE | Minimal interactive proof |
| H-CR-35 | Groth16 = 3 elements | Yes | CLOSE | QAP structure determines this |
| H-CR-36 | BLS12 k = 12 | Yes | EXACT | Noteworthy coincidence |
| H-CR-37 | ECDSA = 2 components | Yes | WEAK | Trivially 2 |
| H-CR-38 | EdDSA determinism | Yes | WEAK | Metaphor, not math |
| H-CR-39 | ML-DSA (6,5) | Yes | EXACT | Remarkable coincidence |
| H-CR-40 | Sig verify ratio | Approx | WEAK | Implementation-dependent |
| H-CR-41 | Entropy pool = 4096 | Partial | CLOSE | Legacy Linux, since reworked |
| H-CR-42 | DRBG reseed = 2^48 | Yes | EXACT | Non-obvious match |
| H-CR-43 | Min entropy = ln(2) | Yes | FAIL | Unit conversion, not prediction |
| H-CR-44 | RNG ratio = 3:1 | Unverified | UNVERIFIABLE | No public data |
| H-CR-45 | TLS 1.3 = 5 suites | Yes | CLOSE | Engineering count |
| H-CR-46 | TLS 1.3 = 1 RTT | Yes | WEAK | The number 1 matches anything |
| H-CR-47 | Cert chain = 3 | Yes | CLOSE | Standard PKI practice |
| H-CR-48 | GCM limit = 2^24 | Partial | WEAK | Cherry-picked bound |

---

## Aggregate Statistics

```
  EXACT:          5  (10.4%)   -- H-CR-17, H-CR-36, H-CR-39, H-CR-42, (H-CR-11 borderline)
  CLOSE:         25  (52.1%)
  WEAK:          14  (29.2%)
  FAIL:           1  ( 2.1%)   -- H-CR-43
  UNVERIFIABLE:   3  ( 6.3%)   -- H-CR-32, H-CR-44 (H-CR-48 reclassified to WEAK)
```

Compare to the original document's self-assessment of 81.3% EXACT. After honest
evaluation: 10% EXACT, 52% CLOSE, 29% WEAK, 2% FAIL, 6% UNVERIFIABLE.

---

## Honest Assessment

### What is genuinely interesting (EXACT)

1. **H-CR-17**: RSA e = 65537 = F_{tau(6)}. The 4th Fermat prime indexing
   through tau(6)=4 is a specific, non-trivial match.
2. **H-CR-36**: BLS12 embedding degree = 12 = sigma(6). The pairing-friendly
   curve family's defining parameter matching the divisor sum is noteworthy.
3. **H-CR-39**: ML-DSA-65 (k,l) = (6,5) = (n, sopfr). Two independent
   parameters both matching n=6 functions is unlikely by chance alone.
4. **H-CR-42**: NIST DRBG reseed = 2^48 = 2^(sigma*tau). Less obvious than
   standard power-of-2 sizes.

### What the document does well

- Every n=6 arithmetic calculation is mathematically correct
- Every standard value cited is factually accurate
- The pattern-matching is comprehensive and well-organized

### What the document overstates

- Claiming "EXACT match" for every hypothesis conflates numerical coincidence
  with causal explanation
- Cryptographic parameters are overwhelmingly powers of 2 (or small multiples).
  n=6 arithmetic can produce *every* exponent from 1 to 12 using simple
  two-term operations on {sigma, tau, phi, sopfr, mu}. The probability of
  matching any given power-of-2 parameter is essentially 1.
- Several hypotheses are duplicates (H-CR-29/30, H-CR-4/9/21) or trivial
  (any pair = phi = 2; any count of 1 = mu = 1)
- The document switches between different decompositions for the same number
  (e.g., 192 has two derivations), which is a hallmark of post-hoc fitting

### Bottom line

The n=6 arithmetic functions produce a toolkit of small integers that can match
almost any cryptographic parameter because those parameters are themselves
drawn from a small set of powers of 2. The framework is a creative lens for
organizing cryptographic constants, but it does not explain *why* those
constants were chosen. The 4-5 genuinely interesting coincidences (F_4, BLS12,
ML-DSA-65, DRBG 2^48) deserve further investigation; the remaining 43
hypotheses are retrofitted pattern matches.

---

> Part of [N6 Architecture](https://github.com/need-singularity/n6-architecture) | [TECS-L](https://github.com/need-singularity/TECS-L)
