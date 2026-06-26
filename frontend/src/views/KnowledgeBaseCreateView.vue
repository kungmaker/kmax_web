<script setup lang="ts">
import { ElMessage } from "element-plus";
import { reactive } from "vue";
import { useRouter } from "vue-router";

import {
  useKnowledgeBaseStore,
  type KnowledgeBase,
} from "@/stores/knowledgeBases";

const router = useRouter();
const knowledgeBaseStore = useKnowledgeBaseStore();

const form = reactive({
  name: "",
  description: "",
  status: "active" as KnowledgeBase["status"],
});

const statusOptions = [
  { label: "启用", value: "active" },
  { label: "草稿", value: "draft" },
  { label: "归档", value: "archived" },
] as const;

async function submitForm() {
  const name = form.name.trim();

  if (!name) {
    ElMessage.warning("请输入知识库名称");
    return;
  }

  try {
    await knowledgeBaseStore.createKnowledgeBase({
      name,
      description: form.description.trim(),
      status: form.status,
    });
    ElMessage.success("知识库已创建");
    await router.push("/knowledge-bases");
  } catch {
    ElMessage.error("创建失败，请检查表单或稍后重试");
  }
}
</script>

<template>
  <main class="page-shell narrow-page">
    <section class="section-card">
      <div class="section-header">
        <div>
          <p class="eyebrow">Create</p>
          <h1 class="section-title">创建知识库</h1>
          <p class="section-copy">
            先建立知识库容器，后续可继续接入文件上传、切分和向量化流程。
          </p>
        </div>
      </div>

      <el-alert
        v-if="knowledgeBaseStore.error"
        :title="knowledgeBaseStore.error"
        type="warning"
        show-icon
        :closable="false"
        class="content-alert"
      />

      <el-form
        label-position="top"
        class="knowledge-form"
        @submit.prevent="submitForm"
      >
        <el-form-item label="知识库名称" required>
          <el-input
            v-model="form.name"
            maxlength="120"
            show-word-limit
            placeholder="例如：产品手册"
          />
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="form.description"
            type="textarea"
            :rows="5"
            placeholder="描述知识库覆盖的资料范围、业务场景或维护负责人"
          />
        </el-form-item>
        <el-form-item label="状态">
          <el-select v-model="form.status" class="status-select">
            <el-option
              v-for="option in statusOptions"
              :key="option.value"
              :label="option.label"
              :value="option.value"
            />
          </el-select>
        </el-form-item>
        <div class="form-actions">
          <el-button @click="router.push('/knowledge-bases')">取消</el-button>
          <el-button
            type="primary"
            native-type="submit"
            :loading="knowledgeBaseStore.creating"
          >
            保存知识库
          </el-button>
        </div>
      </el-form>
    </section>
  </main>
</template>
