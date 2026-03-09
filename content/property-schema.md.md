---
name: My Wiki
publish: true
type:
---

# Vault Property Schema (Canonical)

## 공통
- type      : domain | resource | project
- status    : active | archived | evergreen

## 날짜
- created   : YYYY-MM-DD
- updated   : YYYY-MM-DD

## Domain
- sources   : resource 링크 배열

## Resource
- source    : 출처
- collected : YYYY-MM-DD

## Project
- deadline
- related-domain