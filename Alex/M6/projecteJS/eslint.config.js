import js from "@eslint/js";
import globals from "globals";
import pluginVue from "eslint-plugin-vue";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs,vue}"],
    plugins: { js }, extends: ["js/recommended"],
    languageOptions: { globals: { ...globals.browser, ...globals.node } },
  },

  {
    rules: {
      camelcase: ["error", { properties: "always" }],
      "no-unused-vars": ["error", { argsIgnorePattern: "^_", varsIgnorePattern: "^_" }],
      "no-warning-comments": ["warn", { terms: ["todo", "fixme"], location: "anywhere" }],
      "prefer-const": ["error", { destructuring: "all" }],
      semi: ["error", "always"],
      quotes: ["error", "double", { avoidEscape: true }],
      "quote-props": ["error", "as-needed"],
      "comma-dangle": ["error", "always-multiline"],
      "object-curly-spacing": ["error", "always"],
      "array-bracket-spacing": ["error", "never"],
      "block-spacing": ["error", "always"],
      "space-in-parens": ["error", "never"],
      "space-before-blocks": ["error", "always"],
      "space-before-function-paren": [
        "error",
        { anonymous: "always", named: "never", asyncArrow: "always" },
      ],
      indent: ["error", 2, { SwitchCase: 1 }],
      "key-spacing": ["error", { beforeColon: false, afterColon: true }],
      "no-multiple-empty-lines": ["error", { max: 1, maxEOF: 0 }],
      "eol-last": ["error", "always"],
      "newline-per-chained-call": ["error", { ignoreChainWithDepth: 1 }],
    },
  },

  pluginVue.configs["flat/essential"],
]);
