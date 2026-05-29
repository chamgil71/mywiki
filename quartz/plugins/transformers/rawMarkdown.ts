import { QuartzTransformerPlugin } from "../types"

export const RawMarkdown: QuartzTransformerPlugin = () => {
  return {
    name: "RawMarkdown",
    markdownPlugins() {
      return [
        () => {
          return (_, file) => {
            file.data.rawMarkdown = file.value ? file.value.toString() : ""
          }
        },
      ]
    },
  }
}

declare module "vfile" {
  interface DataMap {
    rawMarkdown: string
  }
}
