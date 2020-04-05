import React from "react";

import styles from "./EntryFormSubmit.module.css";

interface EntryFormSubmitProps {
  label: string;
}

function EntryFormSubmit({ label }: EntryFormSubmitProps) {
  return (
    <div className={styles.entryFormSubmit}>
      <button className={styles.entryFormSubmitButton} type="submit">
        {label}
      </button>
    </div>
  );
}

export default EntryFormSubmit;
