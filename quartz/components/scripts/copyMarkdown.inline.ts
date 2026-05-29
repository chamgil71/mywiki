document.addEventListener("nav", () => {
  const buttons = document.getElementsByClassName("copy-md-button") as HTMLCollectionOf<HTMLButtonElement>

  for (const button of buttons) {
    const onClick = async () => {
      try {
        const encoded = button.getAttribute("data-markdown") || ""
        const rawMarkdown = decodeURIComponent(encoded)
        
        await navigator.clipboard.writeText(rawMarkdown)

        button.classList.add("copied")

        setTimeout(() => {
          button.classList.remove("copied")
        }, 1200)
      } catch (err) {
        console.error("Markdown copy failed", err)
      }
    }

    button.addEventListener("click", onClick)
    
    // Clean up event listener when dynamic page transition happens
    window.addCleanup(() => button.removeEventListener("click", onClick))
  }
})
