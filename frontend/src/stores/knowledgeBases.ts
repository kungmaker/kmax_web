import axios from "axios";
import { defineStore } from "pinia";

export interface KnowledgeBase {
  id: number;
  name: string;
  description: string;
  status: "active" | "draft" | "archived";
  document_count: number;
  created_at: string;
  updated_at: string;
}

interface KnowledgeBasePayload {
  name: string;
  description: string;
  status: KnowledgeBase["status"];
}

export const useKnowledgeBaseStore = defineStore("knowledgeBases", {
  state: () => ({
    items: [] as KnowledgeBase[],
    loading: false,
    creating: false,
    error: "",
  }),
  actions: {
    async fetchKnowledgeBases() {
      this.loading = true;
      this.error = "";

      try {
        const response = await axios.get<KnowledgeBase[]>(
          "/api/knowledge-bases/",
        );
        this.items = response.data;
      } catch (error) {
        this.error =
          error instanceof Error
            ? error.message
            : "Unknown knowledge base error";
      } finally {
        this.loading = false;
      }
    },
    async createKnowledgeBase(payload: KnowledgeBasePayload) {
      this.creating = true;
      this.error = "";

      try {
        const response = await axios.post<KnowledgeBase>(
          "/api/knowledge-bases/",
          payload,
        );
        this.items = [
          response.data,
          ...this.items.filter((item) => item.id !== response.data.id),
        ];
        return response.data;
      } catch (error) {
        this.error =
          error instanceof Error
            ? error.message
            : "Unknown knowledge base error";
        throw error;
      } finally {
        this.creating = false;
      }
    },
  },
});
