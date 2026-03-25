import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "MS wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "ko-KR",
    baseUrl: process.env.VERCEL 
      ? process.env.VERCEL        // Vercel 환경
      : "chamgil71.github.io/mywiki",    // GitHub Pages 환경
    ignorePatterns: ["private", "templates", ".obsidian"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "IBM Plex Sans KR",     // 한국어 지원 + 테크 느낌
        body: "IBM Plex Sans KR",       // 통일감 있는 본문
        code: "JetBrains Mono",         // 개발자 선호 코드 폰트
      },
      colors: {
        lightMode: {
          light: "#FAFAFA",             // 약간 따뜻한 흰색 배경
          lightgray: "#E8E8E8",         // 구분선, 테두리
          gray: "#A0A0A0",              // 비활성 텍스트
          darkgray: "#3D3D3D",          // 본문 텍스트
          dark: "#1A1A1A",              // 제목
          secondary: "#2563EB",         // 링크, 강조 (블루)
          tertiary: "#3B82F6",          // 호버, 보조 강조
          highlight: "rgba(37, 99, 235, 0.06)",  // 코드/인용 배경
          textHighlight: "#FBBF2488",   // 텍스트 하이라이트
        },
        darkMode: {
          light: "#0F0F10",             // 진한 배경
          lightgray: "#1E1E22",         // 구분선
          gray: "#6B6B6B",              // 비활성 텍스트
          darkgray: "#CDCDCD",          // 본문 텍스트
          dark: "#F0F0F0",              // 제목
          secondary: "#60A5FA",         // 링크 (밝은 블루)
          tertiary: "#93C5FD",          // 호버
          highlight: "rgba(96, 165, 250, 0.08)",
          textHighlight: "#FBBF2488",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [
	  Plugin.RemoveDrafts(),
      Plugin.ExplicitPublish(), // publish: true가 있는 파일만 발행
    ],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage({
        sort: (a: any, b: any) => {
          const aIsFolder = a.children !== undefined
          const bIsFolder = b.children !== undefined
          if (aIsFolder && !bIsFolder) return -1
          if (!aIsFolder && bIsFolder) return 1
          const aName = a.displayName ?? a.slug ?? ""
          const bName = b.displayName ?? b.slug ?? ""
          return aName.localeCompare(bName, "ko") * -1
        }
      }),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      // Plugin.CustomOgImages(),
    ],
  },
}

export default config
