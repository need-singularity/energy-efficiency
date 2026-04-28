# archive/_deprecated/2026-04-29-cross-repo-publish-canonical/

papers/.own own 9 (`papers-cross-repo-publish-canonical`, papers commit 6b670f9) 에 따라 archive.

## 폐기 사유

own 9 mandate: sister repos (anima / n6-architecture / hexa-lang / airgenome / nexus / hive / void)
는 자체 zenodo/osf publish 도구 작성 금지. paper 발행 시 papers CLI 에 위임.

## 폐기 파일

| file | original path | reason |
|------|--------------|--------|
| `zenodo_upload.hexa` | `bridge/scripts/zenodo_upload.hexa` | STUB DRAFT (실제 API 호출 0, println 만), 0 consumer, 2026-04-14 작성. papers CLI 의 `tool/zenodo_publish.hexa` (529 LoC, hexa-native) 가 superseded. |

## 후속 진입점

```
papers publish <paper-id> --target zenodo --sandbox --dry-run
papers publish <paper-id> --target all
```

`/Users/ghost/core/papers/bin/papers` (12-verb dispatch). secret 통합으로 `secret get zenodo.token`
자동 inject (hard-coded 토큰 금지).

## raw compliance

- raw 65 idempotent: git mv (history 보존)
- raw 91 C3 honest: archive 사유 + 후속 path 명시
- own 9 grandfather note: archive/marker migration 완료 후 block 격상

## 검증 도구

```
papers cross-repo-lint --report      # n6 BLOCK 표시
papers cross-repo-lint --selftest    # 3 fixtures
```

## 관련

- papers/.own own 9: `papers-cross-repo-publish-canonical`
- papers commit 6b670f9: own 9 등재
- papers commit a3f73a3: tool/papers_cross_repo_lint.hexa land
- /Users/ghost/core/.workspace: papers.cli + papers.manifest resource canonical
