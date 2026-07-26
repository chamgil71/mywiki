import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const TopNav: QuartzComponent = (_props: QuartzComponentProps) => {
  return (
    <nav id="top-nav">
      <a href="/" id="top-nav-logo">MS Wiki</a>
      <div id="top-nav-links">
        <a href="/report">Report</a>
        <a href="/techbook">기술문서</a>
        <a href="/prompt/%ED%94%84%EB%A1%AC%ED%94%84%ED%8A%B8">프롬프트</a>
        <a href="/about">About</a>
        <a
          href="https://github.com/chamgil71"
          target="_blank"
          rel="noopener noreferrer"
        >
          GitHub ↗
        </a>
      </div>
    </nav>
  )
}

export default (() => TopNav) satisfies QuartzComponentConstructor
