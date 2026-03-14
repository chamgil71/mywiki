---
name: My Wiki
publish: false
type:
  - index
---

# 👋 안녕하세요! 나의 지식 창고입니다.

여기에서 제가 공유하는 노트들을 확인하실 수 있습니다.

[공유노트1](/공유노트1)  <-- 이미 publish: true로 설정한 다른 노트의 이름을 적어보세요.

## 폴더명 확인

```dataview
TABLE file.folder AS Folder  
FROM ""  
GROUP BY file.folder  
SORT file.folder ASC
```


## 속성 여부 확인 (dataviewjs)

```dataviewjs
const pages = dv.pages("");

let counter = {};

for (const p of pages) {
  if (!p.file.frontmatter) continue;

  for (const key of Object.keys(p.file.frontmatter)) {
    counter[key] = (counter[key] || 0) + 1;
  }
}

dv.table(
  ["Property", "Used Count"],
  Object.entries(counter)
    .sort((a, b) => b[1] - a[1])
);
```


## 적용 내용 찾기 "title"
```dataview
TABLE file.link, title
FROM ""
WHERE title
SORT file.name ASC
```

## 빈속성값찾기

**고급: “속성은 있는데 값이 비어있는 파일” 찾기  

```dataview
TABLE file.link, status  
FROM ""  
WHERE status = null
SORT file.name ASC
```


## Property Normalization Map

| 기존 속성 | 정규 속성 | 조치 |
|---|---|---|
| Status | status | rename |
| 상태 | status | rename |
| created_at | created | rename |
| 생성일 | created | rename |
| 최종수정일 | updated | rename |
| tag | tags | merge |
| title | ❌ | 제거 |
| description | ❌ | 제거 |


```dataviewjs
const forbidden = ["Status","상태","created_at","최종수정일","tag"];

dv.table(
  ["Property","Used"],
  forbidden
    .map(k => [k, dv.pages("").where(p=>p.file.frontmatter && k in p.file.frontmatter).length])
    .filter(r => r[1] > 0)
);
```



```dataviewjs
let folders = new Set();  
  
for (let p of dv.pages()) {  
folders.add(p.file.folder);  
}  
  
dv.list([...folders].sort());
```

