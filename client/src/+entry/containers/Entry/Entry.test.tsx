import { rest } from "msw";
import { setupServer } from "msw/node";
import { render } from "@testing-library/react";

import Entry from "./Entry";

const server = setupServer(
  rest.post("/giveaway/entry", (req, res, ctx) => {
    return res(
      ctx.json({
        id: "id",
        firstName: "Michael",
        lastName: "Scott",
        email: "michael.scott@dm.com",
        gdprAccepted: true,
        createdAt: "2017",
      })
    );
  })
);

beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

test("Registers", () => {
  render(<Entry />);
});
