import axios from "axios";

import { Config } from "../config/config";

export const HttpClient = axios.create({
  baseURL: Config.apiUrl,
});
