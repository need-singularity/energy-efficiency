import Lake
open Lake DSL

package «n6» where
  -- v4 M2: Mathlib 통합

lean_lib «N6» where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @ "master"

@[default_target]
lean_exe «n6exe» where
  root := `Main
