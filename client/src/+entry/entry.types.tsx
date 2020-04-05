export interface GiveawayEntry {
  id: string;
  firstName: string;
  lastName: string;
  email: string;
  gdprAccepted: boolean;
  createdAt: string;
}

export type GiveawayEntryInputDto = Pick<
  GiveawayEntry,
  "firstName" | "lastName" | "email" | "gdprAccepted"
>;
