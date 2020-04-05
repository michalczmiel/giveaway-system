import { HttpClient } from "../network/httpClient";
import { GiveawayEntry, GiveawayEntryInputDto } from "./entry.types";
import { caseKeys } from "object-casing";
import { snakeCase } from "lodash";

function toSnakeCase<T extends object>(obj: T) {
  return caseKeys(obj, snakeCase);
}

const EntryRepository = {
  getEntry(entryId: string) {
    return HttpClient.get<GiveawayEntry>(`/giveaway/entry/${entryId}`);
  },
  postEntry(attributes: GiveawayEntryInputDto) {
    return HttpClient.post<GiveawayEntry>("/giveaway/entry", {
      data: {
        type: "giveaway-entry",
        attributes: toSnakeCase(attributes),
      },
    });
  },
};

export default EntryRepository;
