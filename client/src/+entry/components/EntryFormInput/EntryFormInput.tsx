import React from "react";

import styles from "./EntryFormInput.module.css";

interface EntryFormInputProps {
  type: string;
  name: string;
  inputRef?: any;
  placeholder?: string;
  required?: boolean;
}

function EntryFormInput({
  type,
  name,
  inputRef,
  placeholder = "",
  required = true,
}: EntryFormInputProps) {
  return (
    <div className={styles.formField}>
      <input
        className={styles.formFieldInput}
        type={type}
        required={required}
        placeholder={placeholder}
        name={name}
        ref={inputRef}
      />
    </div>
  );
}

export default EntryFormInput;
