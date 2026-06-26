---
name: testing-kmax-web-scaffold
description: Test the kmax_web Django + Vue scaffold end-to-end. Use when verifying the home page, Vite proxy, or Django health endpoint integration.
---

# Testing kmax_web scaffold

## Devin Secrets Needed

- None for the local health-page smoke test. The Django health endpoint is unauthenticated and local development defaults to SQLite plus local memory cache.

## Local server setup

1. Start the Django backend from `backend/` with the project virtualenv active:
   ```bash
   python manage.py runserver 127.0.0.1:8000
   ```
2. Start the Vue/Vite frontend from `frontend/`:
   ```bash
   npm run dev -- --host 127.0.0.1
   ```
3. Verify readiness before browser testing:
   ```bash
   python - <<'PY'
   import urllib.request
   for url in ["http://127.0.0.1:8000/api/health/", "http://127.0.0.1:5173/"]:
       with urllib.request.urlopen(url, timeout=10) as response:
           print(url, response.status)
   PY
   ```

## Browser test flow

1. Open `http://127.0.0.1:5173/` in Chrome.
2. Confirm the hero title `企业级智能体与 RAG 平台` appears.
3. Confirm the backend status card shows `后端状态`, `API 正常`, and `kmax_web v0.1.0`.
4. Confirm no warning alert is visible.
5. Confirm the four capability cards are each visible once: `知识库管理`, `RAG 问答`, `工作流编排`, `多模型接入`.
6. Capture a full-page/desktop screenshot showing the hero, status card, and capability cards.

## Notes

- The eyebrow source text may be `Max Knowledge Brain` while CSS renders it visually as uppercase text. Check both DOM text and visual output if case is important.
- Browser console should normally only show Vite connection debug messages during local development.
