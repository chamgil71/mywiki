import { QuartzComponentConstructor, QuartzComponentProps } from "./types"  // ← types import에 QuartzComponentProps 추가

type TagCloudOpts = {}

const TagCloud: QuartzComponentConstructor<TagCloudOpts> = (_opts) => {
  return function TagCloudComponent({ allFiles, cfg }: QuartzComponentProps) {  // ← 여기 props에 cfg 받기!

    const tagMap: Record<string, number> = {}

    for (const file of allFiles) {
      const tags = file.frontmatter?.tags ?? []

      for (const tag of tags) {
        tagMap[tag] = (tagMap[tag] ?? 0) + 1
      }
    }

    const tags = Object.entries(tagMap).sort((a, b) => b[1] - a[1])

    // baseUrl을 cfg에서 안전하게 가져옴
    const base = cfg.baseUrl ? `/${cfg.baseUrl}` : ""

    return (
      <div class="tag-cloud">
        <h3>Tags</h3>
        <ul>
          {tags.map(([tag, count]) => (
            <li>
              <a href={`https://${base}/tags/${tag}`}>
                {tag} ({count})
              </a>
            </li>
          ))}
        </ul>
      </div>
    )
  }
}

export default TagCloud