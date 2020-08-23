import { Config } from "../config";

if (Config.isApiMockingEnabled) {
  require("../mocks");
}

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />
}
