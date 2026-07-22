# AGENTS.md — mywiki (MS Wiki)

Obsidian 노트 → Quartz v4 빌드 → Vercel / GitHub Pages 이중 배포 개인 지식 저장소. 이 문서는 이 레포에서 AI 에이전트 작업의 **최상위 진입점(SSOT)**입니다.

- **적용 프로필**: `prototype` — [`profiles/prototype.md`](./.claude/reference/profiles/prototype.md)
  - 콘텐츠·설정 중심의 정적 사이트 생성기이므로 경량 규범을 적용합니다(자동화 테스트 비필수, 외과적 변경 원칙, 백엔드 서버 미도입).
- **오케스트레이션**: 대규모 다단계 리팩터링이 필요한 경우에 한해 [`orchestration.md`](./.claude/reference/orchestration.md)를 참조합니다.

## Facts (무엇을 만드는가)

- 사양·설계의 1차 앵커는 [`docs/spec.md`](./docs/spec.md)(경량)입니다. 보조 컨텍스트는 [`README.md`](./README.md)·[`docs/`](./docs/)를 참조합니다. `prototype` 프로필상 `worklog.md`는 의무화하지 않으며, 주요 변경은 README에 가볍게 기재합니다.

## Project Shape

- `content/` — Obsidian 노트(마크다운). `publish: true` 메타데이터가 붙은 노트만 웹 공개
- `quartz/`, `quartz.config.ts`, `quartz.layout.ts` — Quartz v4 빌드·레이아웃 설정
- `index_md.py`, `export_publish_notes.py` — 노트 인덱싱·발행 보조 스크립트 (Python)
- `public/`, `static_pages/`, `Dockerfile`, `vercel.json`, `deploy.ps1` — 배포 자산

## Local Rules

- `publish: true` 게이트를 존중합니다. 비공개 노트를 임의로 공개 전환하지 않습니다.
- 요청된 범위 내에서만 콘텐츠·설정을 변경하고, Quartz 코어(`quartz/`) 개조는 최소화합니다(오버 엔지니어링 금지).
- 배포(Vercel/Pages/`deploy.ps1`)는 사용자 승인 후에만 수행합니다.

## Verification

```bash
npx quartz build --serve     # 로컬 미리보기
python index_md.py           # 인덱스 재생성 (필요 시)
```

빌드가 실패하면 정확한 사유를 보고합니다.
