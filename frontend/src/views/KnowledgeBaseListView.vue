<script setup lang="ts">
import { Plus, Refresh } from "@element-plus/icons-vue";
import { storeToRefs } from "pinia";
import { onMounted } from "vue";
import { useRouter } from "vue-router";

import { useKnowledgeBaseStore } from "@/stores/knowledgeBases";

const router = useRouter();
const knowledgeBaseStore = useKnowledgeBaseStore();
const { error, items, loading } = storeToRefs(knowledgeBaseStore);

const statusLabels = {
  active: "启用",
  draft: "草稿",
  archived: "归档",
};

function statusLabel(status: keyof typeof statusLabels) {
  return statusLabels[status];
}

function formatDate(value: string) {
  return new Intl.DateTimeFormat("zh-CN", {
    dateStyle: "short",
    timeStyle: "short",
  }).format(new Date(value));
}

onMounted(() => {
  void knowledgeBaseStore.fetchKnowledgeBases();
});
</script>

<template>
  <main class="page-shell">
    <section class="section-card">
      <div class="section-header">
        <div>
          <p class="eyebrow">Knowledge Bases</p>
          <h1 class="section-title">知识库列表</h1>
          <p class="section-copy">
            创建并管理企业文档、FAQ 和产品资料的知识入口。
          </p>
        </div>
        <div class="section-actions">
          <el-button @click="router.push('/')">返回首页</el-button>
          <el-button
            :icon="Refresh"
            :loading="loading"
            @click="knowledgeBaseStore.fetchKnowledgeBases()"
          >
            刷新
          </el-button>
          <el-button
            type="primary"
            :icon="Plus"
            @click="router.push('/knowledge-bases/create')"
          >
            创建知识库
          </el-button>
        </div>
      </div>

      <el-alert
        v-if="error"
        :title="error"
        type="warning"
        show-icon
        :closable="false"
        class="content-alert"
      />

      <el-table v-loading="loading" :data="items" empty-text="暂无知识库">
        <el-table-column prop="name" label="名称" min-width="180" />
        <el-table-column
          prop="description"
          label="描述"
          min-width="260"
          show-overflow-tooltip
        />
        <el-table-column label="状态" width="120">
          <template #default="scope">
            <el-tag>{{ statusLabel(scope.row.status) }}</el-tag>
          </template>
        </el-table-column>
        <el-table-column
          prop="document_count"
          label="文档数"
          width="100"
          align="right"
        />
        <el-table-column label="更新时间" width="180">
          <template #default="scope">{{
            formatDate(scope.row.updated_at)
          }}</template>
        </el-table-column>
      </el-table>
    </section>
  </main>
</template>
