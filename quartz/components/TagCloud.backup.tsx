import { QuartzComponentConstructor } from "./types"
import cfg from "../../quartz.config"  // ← 이 줄 추가 (중요!)

type TagCloudOpts = {}

const TagCloud: QuartzComponentConstructor<TagCloudOpts> = (_opts) => {
  return ({ allFiles }) => {

    const tagMap: Record<string, number> = {}

    for (const file of allFiles) {
      const tags = file.frontmatter?.tags ?? []

      for (const tag of tags) {
        tagMap[tag] = (tagMap[tag] ?? 0) + 1
      }
    }

    const tags = Object.entries(tagMap).sort((a, b) => b[1] - a[1])

    const base = cfg.configuration.baseUrl 
      ? `/${cfg.configuration.baseUrl}` 
      : ""

    return (
      <div class="tag-cloud">
        <h3>Tags</h3>
        <ul>
          {tags.map(([tag, count]) => (
            <li>
              <a href={`${base}/tags/${tag}`}>
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