import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"

const Giscus: QuartzComponent = ({ displayClass, fileData }: QuartzComponentProps) => {
  // 메인 첫 화면(index.md)에는 댓글창을 띄우지 않으려면 아래 주석(//)을 해제하세요.
   if (fileData.slug === "index") return <></>

  return (
    <div class={`giscus ${displayClass ?? ""}`} style={{ marginTop: "3rem" }}></div>
  )
}

Giscus.afterDOMLoaded = `
  function loadGiscus() {
    const container = document.querySelector('.giscus');
    if (!container) return;
    
    // 기존 iframe 초기화 (SPA 라우팅 시 중복 방지)
    container.innerHTML = '';
    
    const script = document.createElement('script');
    script.src = 'https://giscus.app/client.js';
    
    script.setAttribute('data-repo', 'chamgil71/mywiki-comments');
    script.setAttribute('data-repo-id', 'R_kgDORElb_g');
    script.setAttribute('data-category', 'Announcements');
    script.setAttribute('data-category-id', 'DIC_kwDORElb_s4C6ts0');
    script.setAttribute('data-mapping', 'pathname');
    script.setAttribute('data-strict', '1');
    script.setAttribute('data-reactions-enabled', '1');
    script.setAttribute('data-emit-metadata', '0');
    script.setAttribute('data-input-position', 'bottom');
    
    // 현재 Quartz 테마 확인 후 Giscus에 적용
    const isDark = document.documentElement.getAttribute("saved-theme") === "dark";
    script.setAttribute('data-theme', isDark ? 'transparent_dark' : 'light');
    script.setAttribute('data-lang', 'ko');
    script.crossOrigin = 'anonymous';
    script.async = true;
    
    container.appendChild(script);
  }
  
  // 초기 로드
  loadGiscus();
  
  // 페이지 네비게이션(SPA 전환) 시 스크립트 재실행
  document.addEventListener("nav", () => {
    loadGiscus();
  });
  
  // 테마 토글 버튼 클릭 시 Giscus 테마 실시간 동기화
  document.addEventListener('themechange', (e) => {
    const iframe = document.querySelector('iframe.giscus-frame');
    if (!iframe) return;
    const theme = e.detail.theme === 'dark' ? 'transparent_dark' : 'light';
    iframe.contentWindow.postMessage(
      { giscus: { setConfig: { theme } } },
      'https://giscus.app'
    );
  });
`

export default (() => Giscus) satisfies QuartzComponentConstructor