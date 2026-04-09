import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import TagCloud from "./quartz/components/TagCloud"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [],
  footer: Component.Footer({
    links: {
      // 1. 본인의 GitHub 저장소 주소로 변경
      "© 2026 MS Wiki GitHub": "https://github.com/chamgil71/mywiki",
      // 2. 필요 없다면 디스코드 대신 다른 유용한 링크를 넣거나 삭제하세요.
      "Built with Quartz": "https://quartz.jzhao.xyz/",        // 핵심 엔진
      "Content written in Obsidian": "https://obsidian.md",
      "Hosted on GitHub Pages": "https://pages.github.com/",   // 호스팅
      // "Original by jackyzha0": "https://github.com/jackyzha0/quartz", // 원작자 리스펙트
    },
    // 3. (선택사항) 푸터 텍스트 커스터마이징 
    // Quartz v4에서는 기본적으로 "Created with Quartz"가 붙지만 
    // 원하신다면 이곳에 추가 텍스트를 구성할 수 있습니다.
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      folderDefaultState: "collapsed",
    }),
    Component.DesktopOnly(Component.Spacer()),
    Component.DesktopOnly(Component.RecentNotes({
      title: "최근 게시물",
      limit: 4,
      showTags: false,
    })),
    
  ],
  right: [
    Component.DesktopOnly(Component.TableOfContents()),
    // Component.Search(),
    Component.TagList(),
    // Component.Graph(),
    TagCloud({}),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
  ],
  right: [],
}
