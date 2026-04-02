# kmax_kkk 开发文档

## 📋 目录

1. [项目概述](#项目概述)
2. [技术栈详解](#技术栈详解)
3. [开发环境搭建](#开发环境搭建)
4. [项目结构](#项目结构)
5. [核心模块详解](#核心模块详解)
6. [API 开发规范](#API-开发规范)
7. [前端开发规范](#前端开发规范)
8. [数据库设计](#数据库设计)
9. [调试与测试](#调试与测试)
10. [部署指南](#部署指南)

---

## 项目概述

kmax_web = Max Knowledge Brain，是一个开源的企业级智能体平台，基于 RAG（检索增强生成）技术，支持构建智能客服、知识库问答等应用场景。

### 核心特性
- **RAG 检索增强生成**：本地知识库 + 大模型问答
- **工作流引擎**：可视化编排 AI 流程
- **多模型支持**：支持主流大模型（OpenAI、Claude、通义千问等）
- **多模态**：支持文本、图像、音频、视频
- **MCP 工具调用**：支持外部工具集成

---

## 技术栈详解

### 后端技术栈

#### 核心框架
- **Python**: 3.11.0+
- **Django**: 5.2.11 - Web 框架
- **Django REST Framework**: API 开发
- **LangChain**: 1.2.10 - LLM 应用开发框架

#### 数据库
- **PostgreSQL**: 主数据库
- **pgvector**: 向量相似度检索
- **Redis**: 缓存、任务队列

#### 任务队列
- **Celery**: 5.5.3 - 分布式任务队列
- **django-celery-beat**: 2.8.1 - 定时任务

#### AI 相关
- **LangChain**: LLM 应用开发框架
- **LangGraph**: 1.0.10 - 工作流编排
- **DeepAgents**: 0.4.5 - Agent 框架
- **Sentence Transformers**: 5.0.0 - 文本向量化
- **PyTorch**: 2.8.0 - 深度学习框架

#### 文档处理
- **PyMuPDF**: 1.26.3 - PDF 处理
- **python-docx**: 1.2.0 - Word 文档
- **openpyxl**: 3.1.5 - Excel 处理
- **html2text**: 2025.4.15 - HTML 转文本

#### 向量模型集成
- **阿里云百炼** (dashscope)
- **智谱 AI** (zhipuai)
- **百度千帆** (qianfan)
- **腾讯云** (tencentcloud-sdk-python)
- **AWS Bedrock** (boto3)
- **火山引擎** (volcengine-python-sdk)

#### 其他核心依赖
- **drf-spectacular**: 0.28.0 - API 文档生成
- **django-redis**: 6.0.0 - Redis 缓存
- **django-db-connection-pool**: 1.2.6 - 数据库连接池
- **django-mptt**: 0.17.0 - 树形结构
- **psycopg**: 3.2.9 - PostgreSQL 驱动
- **gunicorn**: 23.0.0 - WSGI 服务器
- **websockets**: 15.0.1 - WebSocket 支持

### 前端技术栈

#### 核心框架
- **Vue.js**: 3.5.13 - 渐进式 JavaScript 框架
- **TypeScript**: 5.8.0 - 类型安全
- **Vite**: 6.2.4 - 构建工具
- **Pinia**: 3.0.1 - 状态管理
- **Vue Router**: 4.5.0 - 路由管理

#### UI 组件库
- **Element Plus**: 2.12.0 - Vue 3 组件库
- **@vueuse/core**: 13.3.0 - Vue 组合式 API 工具集

#### 可视化
- **ECharts**: 5.6.0 - 图表库
- **@antv/layout**: 0.3.1 - 图形布局
- **@logicflow/core**: 1.2.27 - 流程图
- **Mermaid**: 11.12.0 - 图表绘制

#### 编辑器
- **md-editor-v3**: 5.8.2 - Markdown 编辑器
- **vue-codemirror**: 6.1.1 - 代码编辑器
- **@codemirror/**: 语言支持包

#### HTTP 客户端
- **Axios**: 1.8.4 - HTTP 请求库

#### 工具库
- **Moment**: 2.30.1 - 日期处理
- **File-saver**: 2.0.5 - 文件保存
- **html2canvas**: 1.4.1 - 页面截图
- **jspdf**: 4.1.0 - PDF 生成
- **highlight.js**: 11.11.1 - 代码高亮
- **marked**: 12.0.2 - Markdown 解析
- **katex**: 0.16.10 - 数学公式渲染

#### 拖拽排序
- **vue-draggable-plus**: 0.6.0
- **sortablejs**: 1.15.6

#### 国际化
- **vue-i18n**: 11.1.3
- 支持中文（zh）、英文（en）

#### 开发工具
- **ESLint**: 9.22.0 - 代码检查
- **Prettier**: 3.5.3 - 代码格式化
- **vue-tsc**: 2.2.8 - TypeScript 类型检查

## 开发环境搭建

### 系统要求

- **操作系统**: Linux / Windows / macOS
- **Python**: 3.11.0
- **Node.js**: 18.0+
- **PostgreSQL**: 14+ (需安装 pgvector 扩展)
- **Redis**: 6.0+
- **Docker**: (可选，用于容器化部署)

### 后端环境搭建

#### 1. 克隆项目
```bash
git clone https://github.com/kungmaker/kmax_web.git
cd kmax_web-v2
