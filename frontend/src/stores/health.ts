import axios from "axios";
import { defineStore } from "pinia";

interface HealthPayload {
  service: string;
  status: string;
  version: string;
}

export const useHealthStore = defineStore("health", {
  state: () => ({
    health: null as HealthPayload | null,
    loading: false,
    error: "",
  }),
  actions: {
    async fetchHealth() {
      this.loading = true;
      this.error = "";

      try {
        const response = await axios.get<HealthPayload>("/api/health/");
        this.health = response.data;
      } catch (error) {
        this.error =
          error instanceof Error ? error.message : "Unknown health check error";
      } finally {
        this.loading = false;
      }
    },
  },
});
