---
created: 2026-02-12
modified: 2026-03-24
name: index
publish: true
source: 본문출처
tags:
- AI
title: _index
type:
- report
---

## AI 보고서 index


#### 목차



```dataview
list 
FROM "msshin/10-Projects/AIreport"
WHERE file.name != "_index"
SORT file.folder ASC
```