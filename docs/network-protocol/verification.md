# N6 Network Protocol Hypotheses -- Verification Report

Date: 2026-03-30

## Methodology

Each hypothesis (H-NP-1 through H-NP-18) is checked against:
1. **Math check**: Does the claimed n=6 derivation hold arithmetically?
2. **Fact check**: Does the predicted value match real-world standards/practice?
3. **Grade**: EXACT / CLOSE / WEAK / FAIL / UNVERIFIABLE

Grade definitions:
- **EXACT**: Math is correct AND the real-world value matches precisely.
- **CLOSE**: Math is correct AND the real-world value is in the right ballpark but not precise.
- **WEAK**: Math is correct BUT the match is trivial, cherry-picked, or the derivation path is arbitrary.
- **FAIL**: The real-world value does not match the claim.
- **UNVERIFIABLE**: The claim cannot be checked against a concrete standard or measurement.

---

## H-NP-1: IPv6 Address Length = 2^(sigma-sopfr) = 128 bits

**Math check**: sigma(6)=12, sopfr(6)=5, difference=7, 2^7=128. Correct.

**Fact check**: IPv6 addresses are 128 bits per RFC 2460 / RFC 8200. Exact match.

**Commentary**: The math is clean and the match is exact. However, the derivation path (sigma minus sopfr) is one of many possible arithmetic combinations of n=6 functions. The choice of "sigma minus sopfr" is not motivated by any structural argument -- it is selected because it produces 7, which yields 128. The subsidiary claim that IPv4's 32 bits = 2^sopfr(6) is a separate post-hoc fit.

**Grade: EXACT** (value match is real; derivation path is cherry-picked but arithmetically sound)

---

## H-NP-2: TCP 6 Control Flags = n

**Math check**: n=6. Trivially correct.

**Fact check**: RFC 793 defines exactly 6 control bits in the TCP header: URG, ACK, PSH, RST, SYN, FIN. This is correct for the original 1981 specification. The document correctly acknowledges that later extensions added ECE, CWR, and NS (bringing the total to 9), while arguing the original 6 are the "core" set.

**Commentary**: The value match is genuine but the derivation is the most trivial possible -- the number itself IS n. Any protocol with exactly 6 of something would "match." The mapping of individual flags to divisors of 6 ({1,2,3,6}) is purely decorative and has no structural justification. The subsidiary claim that TCP has 11 states = sigma-mu is separately checked at H-NP-13.

**Grade: WEAK** (real match but trivially n=6 itself; decorative divisor mapping)

---

## H-NP-3: WiFi 6 = Generation n

**Math check**: n=6. Trivially correct.

**Fact check**: WiFi Alliance did name 802.11ax as "WiFi 6." The generation numbering is correct.

**Commentary**: This is a naming convention match, not a technical constant. The "WiFi 6" name was assigned retroactively by the WiFi Alliance in 2018 as a marketing simplification. Previous generations were not numbered this way (802.11a/b/g/n/ac). The claim that WiFi 6 is the "optimal efficiency generation" is subjective. The subsidiary claims (MU-MIMO 8 streams = sigma-tau, 1024-QAM = 2^(sigma-phi)) are separate numerological fits to WiFi 6 features that were not designed around n=6.

**Grade: WEAK** (trivial naming match; efficiency optimality claim is subjective)

---

## H-NP-4: 5G NR tau(6)=4 Optimization Dimensions

**Math check**: tau(6)=4. Correct.

**Fact check**: 3GPP does define key 5G KPIs, but the number of "optimization dimensions" depends entirely on how you categorize them. The document lists Speed/Latency/Density/Reliability, but 3GPP also identifies energy efficiency, mobility, spectrum efficiency, and area traffic capacity as distinct KPIs (ITU-R M.2083 defines 8 key capabilities for IMT-2020). The density target of 10^6 devices/km^2 does contain a literal "6" but this is a coincidence of the metric system.

**Commentary**: The "4 dimensions" framing is a selective grouping. The network slicing claim (4 types: eMBB, URLLC, mMTC, V2X) is closer -- 3GPP initially defined 3 slice types (eMBB, URLLC, mMTC); V2X was added later and its status as a separate slice type is debatable.

**Grade: WEAK** (the "4 dimensions" requires selective categorization; ITU defines 8 KPIs)

---

## H-NP-5: DNS Root Servers = sigma(6)+mu(6) = 13

**Math check**: sigma(6)=12, mu(6)=1, sum=13. Correct.

**Fact check**: There are exactly 13 DNS root server identities (A through M), operated by 12 organizations. This has been the case since 1997 and remains unchanged. Exact match.

**Commentary**: The number 13 is genuinely a fixed architectural constant, constrained by the 512-byte UDP packet size limit for DNS responses. The n=6 derivation (12+1) is clean. However, sigma+mu is just one of many expressions that yield 13. The deeper explanation (512-byte UDP constraint forcing 13 NS records) is the actual engineering reason, not number theory. The subsidiary claim about majority = 7 = sigma-sopfr is numerically correct but has no causal relationship to consensus protocols (DNS root servers do not use majority voting).

**Grade: EXACT** (value match is real and architecturally significant; derivation is post-hoc)

---

## H-NP-6: HTTP Methods = sigma(6)-tau(6) = 8

**Math check**: sigma(6)=12, tau(6)=4, difference=8. Correct.

**Fact check**: This is where it gets complicated. RFC 7231 (HTTP/1.1 Semantics) defines GET, HEAD, POST, PUT, DELETE, CONNECT, OPTIONS, TRACE -- that is 8 methods. However, PATCH is defined in RFC 5789 and is universally considered a standard HTTP method. The document lists PATCH instead of CONNECT in its table of 8, which is an error of substitution. The actual standard set in common use is 9 methods (the 8 from RFC 7231 plus PATCH from RFC 5789). If you count only RFC 7231, the answer is 8. If you count all standard methods, it is 9.

**Commentary**: The document's own table lists PATCH but omits CONNECT, which is dishonest bookkeeping -- swapping one method for another to maintain the count of 8. RFC 7231 itself defines 8, so the number is defensible if you draw the line at a single RFC, but the practical answer is 9. The CRUD-to-tau(6) mapping (4 operations) is a reasonable but standard observation unrelated to n=6.

**Grade: CLOSE** (8 holds for RFC 7231 alone, but the table swaps CONNECT for PATCH; real-world count is 9)

---

## H-NP-7: OSI 7 Layers = sigma(6)-sopfr(6)

**Math check**: sigma(6)=12, sopfr(6)=5, difference=7. Correct.

**Fact check**: The OSI model (ISO 7498) has exactly 7 layers. Exact match.

**Commentary**: The value match is exact. The subsidiary mapping of layer numbers to n=6 function values (Layer 4 = tau(6), Layer 2 = phi(6), Layer 1 = mu(6)) is decorative -- the layer numbers 1 through 7 will inevitably hit several n=6 function values. The claim that TCP/IP's 4 layers = tau(6) is a neat secondary match. As with other hypotheses, the derivation path (sigma minus sopfr) is selected to hit 7.

**Grade: EXACT** (value match is real; same derivation path concern as H-NP-1)

---

## H-NP-8: Ethernet MTU 1500 = 6 x 250

**Math check**: 1500 / 6 = 250. Correct. The document then decomposes 250 = phi(6) x sopfr(6)^3 = 2 x 125. This is arithmetically correct (2 x 5^3 = 250).

**Fact check**: IEEE 802.3 Ethernet MTU is 1500 bytes. Correct. Jumbo frames are 9000 bytes and 9000/1500 = 6. Correct.

**Commentary**: Any number is divisible by 6 if it happens to be a multiple of 6. The real reason for 1500 bytes is historical: it was a compromise between latency and throughput for 10 Mbps Ethernet in the early 1980s, balancing RAM costs and collision domain efficiency. The Egyptian fraction decomposition (750+500+250) is mathematically correct but has no engineering significance. The jumbo frame ratio of 6 is a genuinely interesting coincidence. The title formula "n x (sigma-tau)^(sigma-sopfr-tau-1)" evaluates to 6 x 8^2 = 384, not 1500 -- the title formula appears to be wrong.

**Grade: WEAK** (1500 is divisible by 6, but so are many numbers; jumbo frame ratio is interesting; title formula is incorrect)

---

## H-NP-9: TCP Initial Window = sigma(6)-phi(6) = 10

**Math check**: sigma(6)=12, phi(6)=2, difference=10. Correct.

**Fact check**: RFC 6928 recommends IW=10 segments. The historical progression 1->2->4->10 is accurate (RFC 2001 -> RFC 2414 -> RFC 3390 -> RFC 6928).

**Commentary**: The value match to 10 is exact. The historical progression mapping (1=mu, 2=phi, 4=tau, 10=sigma-phi) is the strongest structural argument in this document -- four successive RFC values each matching an n=6 arithmetic function. However, IW=3 was also a valid setting under RFC 3390 (for MSS > 1095), which breaks the clean sequence. The progression is also just 1, 2, 4, 10 -- the jumps are roughly "doubling then a bigger jump," which is common in engineering parameter tuning.

**Grade: CLOSE** (10 matches exactly; the 4-step progression is striking but IW=3 was also standard and is omitted)

---

## H-NP-10: BGP AS Path Length = tau(6) = 4

**Math check**: tau(6)=4. Correct.

**Fact check**: Average AS path length on the Internet is approximately 3.5-4.5 hops depending on measurement point and time. APNIC and RIPE data generally show values in the range 3.5-4.2. The claim of "approximately 4" is reasonable. The claim of "approximately 12-16 Tier-1 ISPs" is roughly correct (commonly cited as ~15-16, though the exact number is debated). The claim of "optimal 6 peering relationships per AS" is not supported by data -- large networks peer with hundreds or thousands of others.

**Commentary**: The AS path length match is approximate. The "optimal 6 peering" claim has no empirical basis. The Tier-1 count being "near sigma(6)=12" is a stretch when the actual count is 15-16.

**Grade: CLOSE** (AS path length ~4 is roughly right; peering claim is unsupported)

---

## H-NP-11: QUIC Multiplexed Streams = J_2(6) = 24

**Math check**: J_2(6) = 6^2 * product(1 - 1/p^2) for primes p|6 = 36 * (1-1/4)(1-1/9) = 36 * 3/4 * 8/9 = 36 * 24/36 = 24. Correct.

**Fact check**: QUIC (RFC 9000) does not specify a fixed number of concurrent streams. The initial_max_streams transport parameter is negotiated. Common defaults: Chromium uses 100 for bidi streams. The claim that "effective active streams are ~24" is not well-documented. The claim that "average web page resources ~20-30" is approximately correct (HTTP Archive median is around 60-80 requests per page as of recent data, though many are small).

**Commentary**: There is no standard or empirical measurement that pins QUIC streams to 24. The Chrome per-origin limit of 6 (H-NP-18) times 4 is one way to get 24, but the actual QUIC stream defaults are much higher. The "effective active" framing is unfalsifiable.

**Grade: UNVERIFIABLE** (no standard or measurement confirms 24 as a meaningful QUIC constant)

---

## H-NP-12: TLS Handshake = phi(6) = 2 RTT

**Math check**: phi(6)=2. Correct.

**Fact check**: TLS 1.2 full handshake requires 2 round trips. TLS 1.3 full handshake requires 1 round trip. TLS 1.3 0-RTT resumption requires 0 round trips. These are all correct.

**Commentary**: The match for TLS 1.2 = 2 RTT is exact. The progression 2->1->0 mapped to phi->mu->0 is numerologically tidy but the values 2, 1, 0 are such small integers that matching them to number-theoretic functions is not impressive. Any protocol handshake will use a small number of round trips. The prediction about post-quantum TLS reverting to 2-RTT is speculative but plausible (larger key exchanges may require more rounds).

**Grade: WEAK** (2 RTT for TLS 1.2 is exact but trivially small; any 2-valued protocol feature would match phi(6))

---

## H-NP-13: TCP State Machine = sigma(6)-mu(6) = 11

**Math check**: sigma(6)=12, mu(6)=1, difference=11. Correct.

**Fact check**: RFC 793 TCP state diagram has exactly 11 states: CLOSED, LISTEN, SYN-SENT, SYN-RECEIVED, ESTABLISHED, FIN-WAIT-1, FIN-WAIT-2, CLOSE-WAIT, CLOSING, LAST-ACK, TIME-WAIT. Exact match.

**Commentary**: This is one of the stronger matches. 11 is not a "round" number and the TCP state count is a well-defined, fixed architectural constant from RFC 793. The derivation sigma-mu = 12-1 = 11 is clean. That said, sigma-mu is one of dozens of computable expressions from n=6 functions, and you could match many integers in the range 1-24 with some combination.

**Grade: EXACT** (11 states is a precise, non-trivial match to a non-obvious constant)

---

## H-NP-14: Port Number Space = 2^(sigma+tau) = 2^16 = 65536

**Math check**: sigma(6)=12, tau(6)=4, sum=16, 2^16=65536. Correct.

**Fact check**: TCP/UDP port fields are 16-bit unsigned integers, giving 65536 ports (0-65535). Exact match. Well-known ports 0-1023 = 1024 = 2^10 is also correct. The document claims 10 = sigma-phi = 12-2, which is arithmetically correct.

**Commentary**: 16-bit fields are extremely common in computing (16-bit integers, Unicode BMP, etc.), so matching 16 to some n=6 expression is not remarkable. The well-known port range of 1024 = 2^10 is a standard power-of-2 boundary. The claim about ephemeral port start 49152 = 3 x 2^14 is factually correct (49152 = 3 x 16384) but sigma+phi = 14, not "sigma+phi" as labeled -- the document says 2^(sigma+phi) which would be 2^14 = 16384, and 3 x 16384 = 49152. This is arithmetically valid but increasingly contrived.

**Grade: WEAK** (16-bit fields are ubiquitous; matching 16 = sigma+tau is unimpressive)

---

## H-NP-15: HTTP Status Code Classes = sopfr(6) = 5

**Math check**: sopfr(6) = 2+3 = 5. Correct.

**Fact check**: HTTP defines exactly 5 status code classes: 1xx, 2xx, 3xx, 4xx, 5xx. Exact match.

**Commentary**: The value match is exact. However, "5 categories" is an extremely common organizational pattern (5-point scales, 5 senses, etc.). The decomposition of client/server error mapping to prime factors 2 and 3 is decorative. The number 5 appears in countless contexts and sopfr(6)=5 is just one way to derive it.

**Grade: EXACT** (value is precisely correct; derivation is one of many ways to get 5)

---

## H-NP-16: RSA Minimum Key Size = 2^(sigma-mu) = 2048

**Math check**: sigma(6)=12, mu(6)=1, difference=11, 2^11=2048. Correct.

**Fact check**: NIST SP 800-57 and CA/Browser Forum Baseline Requirements both specify RSA-2048 as the minimum acceptable key size for most purposes. Exact match. The progression 512->1024->2048->4096 is real, and these are standard RSA key sizes.

**Commentary**: RSA key sizes are powers of 2 by convention (512, 1024, 2048, 4096), so the only question is which power. 2^11=2048 happens to be the current minimum standard. The "progression" mapping (2^9, 2^10, 2^11, 2^12) to various n=6 expressions is post-hoc: the document admits 2^9 = "non-standard" mapping. Powers of 2 from 9 to 12 will inevitably overlap with n=6 arithmetic outputs. The match to the current standard (2048) via sigma-mu is the same derivation as H-NP-13 (TCP 11 states), which is internally consistent.

**Grade: EXACT** (2048 is correct; power-of-2 key sizes make this less surprising)

---

## H-NP-17: Ethernet Frame Preamble = sigma-tau = 8 Bytes

**Math check**: sigma(6)=12, tau(6)=4, difference=8. Correct.

**Fact check**: Ethernet preamble is 7 bytes of 10101010 pattern plus 1 byte SFD (10101011), totaling 8 bytes. Correct. MAC addresses are 6 bytes (EUI-48). Correct. Minimum Ethernet frame size is 64 bytes = 2^6. Correct.

**Commentary**: The 8-byte preamble match reuses the same sigma-tau=8 formula as H-NP-6 (HTTP methods). Using the same formula for unrelated constants weakens the framework -- if sigma-tau "means" HTTP methods, it should not also "mean" preamble bytes. The MAC address = 6 bytes = n is a genuine and well-known fact. The minimum frame 64 = 2^6 is a real match. These subsidiary facts (MAC=6, min frame=2^6) are arguably more interesting than the preamble claim.

**Grade: CLOSE** (individual values match but sigma-tau=8 is overloaded across hypotheses; MAC=6 bytes is the strongest point here and arguably deserves its own hypothesis)

---

## H-NP-18: Browser Concurrent Connections = n = 6

**Math check**: n=6. Trivially correct.

**Fact check**: Chrome, Firefox, and Safari all default to 6 concurrent connections per origin for HTTP/1.1. This is correct and well-documented (Chromium source: `kMaxSocketsPerGroup = 6`).

**Commentary**: This is a genuine, precise, independently-arrived-at engineering constant. Major browsers converged on 6 through empirical testing. The original HTTP/1.1 spec (RFC 2616) recommended 2, and browsers independently found 6 to be optimal. However, the n=6 "derivation" is just n itself -- the simplest possible match. The fact that browsers converged on this value through experimentation is interesting but does not require number theory to explain (it is a tradeoff between parallelism and server load/congestion).

**Grade: WEAK** (real engineering constant but derivation is trivially n=6 itself)

---

## Summary Table

| ID | Hypothesis | Claimed Value | Real Value | Math OK | Grade |
|----|-----------|--------------|------------|---------|-------|
| H-NP-1 | IPv6 address bits | 128 | 128 | Yes | EXACT |
| H-NP-2 | TCP control flags | 6 | 6 (original), 9 (modern) | Yes | WEAK |
| H-NP-3 | WiFi generation | 6 | 6 (naming convention) | Yes | WEAK |
| H-NP-4 | 5G optimization dims | 4 | 8 (ITU KPIs), 3-4 (selective) | Yes | WEAK |
| H-NP-5 | DNS root servers | 13 | 13 | Yes | EXACT |
| H-NP-6 | HTTP methods | 8 | 8 (RFC 7231) or 9 (with PATCH) | Yes | CLOSE |
| H-NP-7 | OSI layers | 7 | 7 | Yes | EXACT |
| H-NP-8 | Ethernet MTU | 1500 | 1500 | Yes | WEAK |
| H-NP-9 | TCP initial window | 10 | 10 (RFC 6928) | Yes | CLOSE |
| H-NP-10 | BGP AS path length | 4 | ~3.5-4.2 | Yes | CLOSE |
| H-NP-11 | QUIC streams | 24 | No standard (default ~100) | Yes | UNVERIFIABLE |
| H-NP-12 | TLS handshake RTT | 2 | 2 (TLS 1.2) | Yes | WEAK |
| H-NP-13 | TCP states | 11 | 11 | Yes | EXACT |
| H-NP-14 | Port number space | 65536 | 65536 | Yes | WEAK |
| H-NP-15 | HTTP status classes | 5 | 5 | Yes | EXACT |
| H-NP-16 | RSA min key size | 2048 | 2048 | Yes | EXACT |
| H-NP-17 | Ethernet preamble | 8 bytes | 8 bytes | Yes | CLOSE |
| H-NP-18 | Browser connections | 6 | 6 | Yes | WEAK |

## Score Distribution

| Grade | Count | Hypotheses |
|-------|-------|-----------|
| EXACT | 6 | H-NP-1, H-NP-5, H-NP-7, H-NP-13, H-NP-15, H-NP-16 |
| CLOSE | 4 | H-NP-6, H-NP-9, H-NP-10, H-NP-17 |
| WEAK | 7 | H-NP-2, H-NP-3, H-NP-4, H-NP-8, H-NP-12, H-NP-14, H-NP-18 |
| FAIL | 0 | -- |
| UNVERIFIABLE | 1 | H-NP-11 |

## Overall Assessment

**6 of 18 hypotheses receive EXACT grades**, meaning the n=6 arithmetic is correct and the real-world value matches precisely. The strongest matches are:

- **H-NP-13 (TCP 11 states)**: 11 is a non-obvious number and sigma-mu=11 is a clean derivation.
- **H-NP-5 (DNS 13 root servers)**: 13 is a non-obvious fixed constant.
- **H-NP-1 (IPv6 128 bits)**: 2^7 derivation is clean, though 128 is a common power-of-2.

**Structural concerns across all hypotheses:**

1. **Cherry-picking derivation paths.** The n=6 arithmetic toolkit (sigma, tau, phi, sopfr, mu, J_2, lambda, and their pairwise sums/differences/products) generates dozens of integers in the range 1-36. Most small integers appearing in networking standards can be "derived" from some combination. The document never explains *why* a particular combination (e.g., sigma minus sopfr vs. sigma minus tau) corresponds to a particular domain.

2. **Formula reuse.** sigma-tau=8 is used for both HTTP methods (H-NP-6) and Ethernet preamble (H-NP-17). sigma-mu=11 is used for both TCP states (H-NP-13) and RSA key exponent (H-NP-16). If these formulas had unique physical meaning, they should not map to unrelated domains.

3. **Trivial matches.** Five hypotheses (H-NP-2, H-NP-3, H-NP-8, H-NP-14, H-NP-18) use n=6 directly or match ubiquitous powers of 2. These are not meaningful predictions.

4. **Post-hoc fitting.** None of these hypotheses predicted a value before it was known. Every derivation was constructed after knowing the target number. A proper test of the framework would be to predict an unknown constant.

5. **The framework produces no FAIL results partly because it is flexible enough to fit almost any small integer.** The absence of failures is not evidence of correctness -- it is evidence of overfitting.

**Bottom line:** The arithmetic is uniformly correct. Six real-world values match exactly. But the explanatory power is limited by the large number of available n=6 expressions and the absence of any a priori derivation mechanism connecting specific arithmetic functions to specific protocol design dimensions.
