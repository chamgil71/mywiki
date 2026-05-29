import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
// @ts-ignore
import copyMarkdownScript from "./scripts/copyMarkdown.inline"
import styles from "./styles/copyMarkdown.scss"

const CopyMarkdown: QuartzComponent = ({ fileData }: QuartzComponentProps) => {
  const rawMarkdown = fileData.rawMarkdown ?? ""
  const encodedMarkdown = encodeURIComponent(rawMarkdown)

  return (
    <button
      class="copy-md-button"
      data-markdown={encodedMarkdown}
      title="Copy Markdown"
      aria-label="Copy Markdown"
    >
      <svg
        xmlns="http://www.w3.org/2000/svg"
        width="18"
        height="18"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        stroke-width="2"
        stroke-linecap="round"
        stroke-linejoin="round"
      >
        <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
        <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
      </svg>
    </button>
  )
}

CopyMarkdown.afterDOMLoaded = copyMarkdownScript
CopyMarkdown.css = styles

export default (() => CopyMarkdown) satisfies QuartzComponentConstructor
