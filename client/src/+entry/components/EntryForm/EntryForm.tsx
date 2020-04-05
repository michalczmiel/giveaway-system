import React from "react";
import { useForm } from "react-hook-form";

import EntryFormField from "../EntryFormInput";
import EntryFormSubmit from "../EntryFormSubmit";
import EntryFormCheckbox from "../EntryFormCheckbox";
import { GiveawayEntryInputDto } from "../../entry.types";

import styles from "./EntryForm.module.css";

interface EntryFormProps {
  onSubmit: (values: GiveawayEntryInputDto) => void;
}

function EntryForm({ onSubmit }: EntryFormProps) {
  const { register, handleSubmit } = useForm<GiveawayEntryInputDto>();

  return (
    <div className={styles.form}>
      <form onSubmit={handleSubmit(onSubmit)}>
        <EntryFormField
          type="text"
          name="firstName"
          placeholder="First name"
          inputRef={register}
        />
        <EntryFormField
          type="text"
          name="lastName"
          placeholder="Last name"
          inputRef={register}
        />
        <EntryFormField
          type="email"
          name="email"
          placeholder="Email"
          inputRef={register}
        />
        <EntryFormCheckbox name="gdpr_accepted" inputRef={register} />
        <EntryFormSubmit label="Submit" />
      </form>
    </div>
  );
}

export default EntryForm;
