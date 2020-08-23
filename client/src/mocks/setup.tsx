import { setupWorker, RequestHandler } from "msw";
import { setupServer } from "msw/node";

export function setupMockForBrowser(handlers: RequestHandler[]) {
  const worker = setupWorker(...handlers)
  worker.start();
};

export function setupMockForServer(handlers: RequestHandler[]) {
  const server = setupServer(...handlers);
  server.listen();
};
