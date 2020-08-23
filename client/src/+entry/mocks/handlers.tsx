import { rest } from "msw";

export const entryHandlers = [
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
  }),
];
