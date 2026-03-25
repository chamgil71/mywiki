import { QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative, SimpleSlug } from "../../quartz/util/path"

type TagCloudOpts = {}

const TagCloud: QuartzComponentConstructor<TagCloudOpts> = (_opts) => {
  // 에러 3, 4, 5 해결: 필요한 props인 fileData, allFiles, displayClass를 모두 정확히 받아옵니다. (안 쓰는 cfg는 제거)
  return function TagCloudComponent({ fileData, allFiles, displayClass }: QuartzComponentProps) { 
    const tagMap: Record<string, number> = {}

    for (const file of allFiles) {
      const tags = file.frontmatter?.tags ?? []

      for (const tag of tags) {
        tagMap[tag] = (tagMap[tag] ?? 0) + 1
      }
    }

    const tags = Object.entries(tagMap).sort((a, b) => b[1] - a[1])

    return (
      <div class={`tag-cloud ${displayClass ?? ""}`}>
        <h3>Tags</h3>
        <ul>
          {tags.map(([tag, count]) => {
            // 핵심: 현재 위치(fileData.slug)를 기준으로 태그의 상대 경로를 자동 계산합니다.
            const tagHref = resolveRelative(fileData.slug!, `tags/${tag}` as SimpleSlug)
            
            return (
              <li>
                <a href={tagHref}>
                  {tag} ({count})
                </a>
              </li>
            )
          })}
        </ul>
      </div>
    )
  }
}

export default TagCloud