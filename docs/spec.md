# mywiki (MS Wiki) 사양서 (spec.md)

> [!IMPORTANT]
> 본 사양서는 개발 요구사항 및 설계의 **닻(anchor)**입니다.
> 에이전트 단독으로 수정할 수 없으며, 변경 시 반드시 사용자의 사전 승인을 받아야 합니다.
> `prototype` 프로필상 경량 사양이며, 상세 계획은 [`통합-서비스-구성-계획.md`](./통합-서비스-구성-계획.md)를 참조합니다.

## 1. 개요 및 목적
- **비즈니스 배경**: Obsidian으로 축적한 AI·투자·기술 리서치 노트를 선택적으로 웹에 공개하고 싶다.
- **해결하려는 문제**: `publish: true` 메타데이터가 붙은 노트만 Quartz v4로 빌드해 Vercel/GitHub Pages에 이중 배포한다.
- **최종 목표**: 노트 편집 → 빌드 → 이중 배포 흐름을 안정적으로 유지하고, 비공개 노트 유출을 방지한다.

## 2. 세부 요구사항 및 범위
- **기능 요구사항** (README 기준 시드):
  - F-1: `content/` 노트 중 `publish: true`만 공개 빌드
  - F-2: Quartz v4 빌드 및 Vercel(주)·GitHub Pages(백업) 이중 배포
  - F-3: 노트 인덱싱·발행 보조 스크립트(`index_md.py`, `export_publish_notes.py`)
  - F-4: _TODO — 추가 요구사항(테마/검색 등)_
- **비기능 요구사항**:
  - 프라이버시: `publish` 게이트 준수, 비공개 노트 임의 공개 전환 금지
  - 변경 최소화: Quartz 코어(`quartz/`) 개조 최소화(오버 엔지니어링 금지)

## 3. 시스템 아키텍처 및 설계
- **데이터 흐름**: `content/(Obsidian MD)` → `Quartz v4 빌드(quartz.config/layout)` → `public/` → `Vercel / GitHub Pages`
- **설정 파일**: `quartz.config.ts`, `quartz.layout.ts`, `vercel.json`, `Dockerfile`, `deploy.ps1`

## 4. 검증 계획
- **테스트 시나리오**: 로컬 빌드/미리보기로 공개 노트 렌더 및 비공개 노트 제외 확인
- **검증 명령**:
  ```bash
  npx quartz build --serve
  python index_md.py     # 필요 시
  ```
- **기대 성공 지표**: 빌드 성공 + `publish:true` 노트만 노출. 배포는 사용자 승인 후.
