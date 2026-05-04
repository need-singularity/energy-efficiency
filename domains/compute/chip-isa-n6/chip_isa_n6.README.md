# chip_isa_n6

Xn6 24-instruction ISA: encode / decode / round-trip. Productized port of
`~/core/n6-architecture/domains/compute/chip-isa-n6/` (305-line
`xn6_asm_examples.hexa`, 24 mnemonics over 6 op families × 4 variants).

## Anchors

- `J2 = 2*sigma = 24` -- both **instruction count** and **instruction width**
  in bits (24 bits = 3 bytes per instruction).
- `n = 6` -- funct3 *used* values (6 of 8 codes; 2 reserved).
- `tau = 4` -- variants per op family.
- `sigma-tau = 8` -- scalar-bus width upstream; here imm is `7` bits
  (`24 - 3 funct3 - 2 variant - 3*4 reg = 7`), one less than the bus to
  fit J2=24 exactly. Documented honestly.

## 24-bit layout

```
[23..21] funct3 (3b)   gemm=000  softmax=001  topk=010
                        gate=011  reduce=100  conv=101   (110/111 reserved)
[20..19] variant (2b)  00 / 01 / 10 / 11
[18..15] rd      (4b)  destination register r0..r15
[14..11] rs1     (4b)
[10..7]  rs2     (4b)
[6..0]   imm     (7b, signed two's complement, range [-64..63])
```

## Import

```python
from modules.chip_isa_n6 import encode, decode, roundtrip_test

b = encode("gemm.m r1, r2, r3")
print(b.hex())                     # 009180  (3 bytes)
print(decode(b))                   # gemm.m r1, r2, r3, 0

assert roundtrip_test("sm.exp r0, r4, r0, -5")
```

## CLI

```sh
python chip_isa_n6.py --self-test
python chip_isa_n6.py --list-ops
python chip_isa_n6.py --encode "gemm.m r1, r2, r3"
python chip_isa_n6.py --decode 009180
```

## Falsifier list

1. **Round-trip lossless** for all 24 mnemonics with arbitrary
   `(rd, rs1, rs2, imm)` -- `encode -> decode -> encode` is byte-identical.
2. **Width fits J2=24**. `3+2+4+4+4+7 == 24` is asserted in self-test.
3. **6 funct3 codes used, 2 reserved**. Decoding a reserved funct3
   (`110`/`111`) raises `ValueError`.
4. **24 mnemonics in table** == `J2`. Self-test asserts
   `len(list_ops()) == 24` and 4 variants per funct3.
5. **Out-of-range fields** (imm overflow, reg >= 16) raise `ValueError`
   at encode time.

## Honesty / source-vs-impl gap

- Upstream `xn6_asm_examples.hexa` defines mnemonics via `@xn6(op="...")`
  attributes but does **not** specify a concrete bit layout. The 24-bit
  packing in this module is **derived** to match J₂=24 width + n=6 funct3
  use; treat as a candidate encoding, not a fixed external spec.
- imm is **7 bits**, not the upstream-bus's `sigma-tau = 8`. One bit was
  consumed by the funct3+variant combo to keep total == J2. If a future
  spec promotes width to 32 bits, restore imm to 8.
- Source claims "24 = funct3 used (6) × variant (4)"; this module preserves
  the count exactly (`24 == J2 == 6*4 == n*tau`).
