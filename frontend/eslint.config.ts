import js from "@eslint/js";
import prettier from "@vue/eslint-config-prettier";
import {
  defineConfigWithVueTs,
  vueTsConfigs,
} from "@vue/eslint-config-typescript";
import pluginVue from "eslint-plugin-vue";

export default defineConfigWithVueTs(
  {
    ignores: ["dist/**", "node_modules/**"],
  },
  js.configs.recommended,
  ...pluginVue.configs["flat/recommended"],
  vueTsConfigs.recommended,
  prettier,
);
