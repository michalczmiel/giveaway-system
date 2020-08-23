import { setupMockForBrowser, setupMockForServer } from "./setup";
import { handlers } from "./handlers";

if (typeof window === 'undefined') {
  setupMockForServer(handlers);
} else {
  setupMockForBrowser(handlers);
}
