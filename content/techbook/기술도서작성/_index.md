---
created: 2026-02-12
name: index_tech
publish: true
source: 본문출처
tags: null
title: Index
type:
- techbook
---

## 기술도서 자료 index

- [[ch00.TABLE_OF_CONTENTS## 전체 목차 (Table of Contents)|옵시디언가이드]]



#### 옵시디언
- dataview 옵시디언 사용 ( 웹에서는 에러)

```dataview
list 
FROM "msshin/60-AI/기술도서작성"
WHERE file.name != "index"
SORT file.folder ASC
```