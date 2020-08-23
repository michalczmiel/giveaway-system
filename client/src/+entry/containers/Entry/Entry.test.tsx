import { setupServer } from "msw/node";
import { render } from "@testing-library/react";

import Entry from "./Entry";
import { entryHandlers } from "../../mocks";

const server = setupServer(...entryHandlers);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test("Registers", () => {
  render(<Entry />);
});
