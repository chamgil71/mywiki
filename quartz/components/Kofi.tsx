import { QuartzComponent, QuartzComponentConstructor } from "./types"

const Kofi: QuartzComponent = () => {
  return (
    <div
      style={{
        marginTop: "2rem",
        padding: "1rem",
        borderTop: "1px solid var(--lightgray)",
        textAlign: "center",
      }}
    >
      <a
        href="https://ko-fi.com/chamgil"
        target="_blank"
        rel="noopener noreferrer"
      >
        ☕ Support this project on Ko-Fi
      </a>
    </div>
  )
}

export default (() => Kofi) satisfies QuartzComponentConstructor