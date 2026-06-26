import { createRouter, createWebHistory } from "vue-router";

import HomeView from "@/views/HomeView.vue";
import KnowledgeBaseCreateView from "@/views/KnowledgeBaseCreateView.vue";
import KnowledgeBaseListView from "@/views/KnowledgeBaseListView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/knowledge-bases",
      name: "knowledge-bases",
      component: KnowledgeBaseListView,
    },
    {
      path: "/knowledge-bases/create",
      name: "knowledge-bases-create",
      component: KnowledgeBaseCreateView,
    },
  ],
});

export default router;
