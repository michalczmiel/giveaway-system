import React, { useState } from "react";

import EntryForm from "../../components/EntryForm";
import EntrySubmitted from "../../components/EntrySubmitted";
import EntryRepository from "../../entry.repository";
import { GiveawayEntryInputDto } from "../../entry.types";

import styles from "./Entry.module.css";

function Entry() {
  const [hasSubmitted, setHasSubmitted] = useState<boolean>(false);

  async function handleSubmit(values: GiveawayEntryInputDto) {
    try {
      await EntryRepository.postEntry(values);
      setHasSubmitted(true);
    } catch (error) {
      console.error(error);
    }
  }

  return (
    <div className={styles.entry}>
      <h1>Giveaway</h1>
      {hasSubmitted ? (
        <EntrySubmitted />
      ) : (
        <EntryForm onSubmit={handleSubmit} />
      )}
    </div>
  );
}

export default Entry;
