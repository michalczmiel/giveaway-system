import React from "react";

import styles from "./EntryFormCheckbox.module.css";

interface EntryFormCheckboxProps {
  name: string;
  inputRef?: any;
}

function EntryFormCheckbox({ inputRef, name }: EntryFormCheckboxProps) {
  return (
    <div className={styles.formField}>
      <input
        className={styles.formFieldCheckbox}
        type="checkbox"
        required
        placeholder="GDPR"
        name={name}
        ref={inputRef}
      />
      <label htmlFor="gdpr">Do you accept GDPR?</label>
    </div>
  );
}

export default EntryFormCheckbox;
