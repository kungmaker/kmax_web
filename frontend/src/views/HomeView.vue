<script setup lang="ts">
import { DataAnalysis, Files, Guide, Share } from "@element-plus/icons-vue";
import { storeToRefs } from "pinia";
import { onMounted } from "vue";

import { useHealthStore } from "@/stores/health";

const healthStore = useHealthStore();
const { error, health, loading } = storeToRefs(healthStore);

const capabilities = [
  {
    icon: Files,
    title: "知识库管理",
    description: "上传文档、切分文本、构建可检索的企业知识资产。",
  },
  {
    icon: DataAnalysis,
    title: "RAG 问答",
    description: "结合本地向量检索与大模型生成，输出可追溯答案。",
  },
  {
    icon: Share,
    title: "工作流编排",
    description: "通过可视化节点组织检索、推理、工具调用和响应流程。",
  },
  {
    icon: Guide,
    title: "多模型接入",
    description: "预留 OpenAI、Claude、通义千问等模型供应商配置入口。",
  },
];

onMounted(() => {
  void healthStore.fetchHealth();
});
</script>

<template>
  <main class="page-shell">
    <section class="hero-card">
      <div>
        <p class="eyebrow">Max Knowledge Brain</p>
        <h1>企业级智能体与 RAG 平台</h1>
        <p class="hero-copy">
          kmax_web 用于构建知识库问答、智能客服和可编排的 AI 工作流。
        </p>
        <div class="hero-actions">
          <RouterLink to="/knowledge-bases" class="router-link-button">
            <el-button type="primary" size="large">进入知识库管理</el-button>
          </RouterLink>
        </div>
      </div>
      <el-card class="status-card" shadow="never">
        <template #header>后端状态</template>
        <el-skeleton v-if="loading" :rows="2" animated />
        <el-alert
          v-else-if="error"
          :title="error"
          type="warning"
          show-icon
          :closable="false"
        />
        <el-result v-else-if="health" icon="success" title="API 正常">
          <template #sub-title
            >{{ health.service }} v{{ health.version }}</template
          >
        </el-result>
        <el-empty v-else description="未获取到状态" />
      </el-card>
    </section>

    <section class="capability-grid">
      <el-card
        v-for="item in capabilities"
        :key="item.title"
        shadow="hover"
        class="capability-card"
      >
        <el-icon :size="32"><component :is="item.icon" /></el-icon>
        <h2>{{ item.title }}</h2>
        <p>{{ item.description }}</p>
      </el-card>
    </section>
  </main>
</template>
