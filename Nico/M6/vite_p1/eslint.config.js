import js from "@eslint/js";
import globals from "globals";
import { defineConfig } from "eslint/config";

export default defineConfig([
  {
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { js },
    extends: ["js/recommended"],
    languageOptions: { globals: globals.browser },
    rules: {
      "eqeqeq": "error", // Enforce strict equality
      "no-unused-vars": ["warn", { "argsIgnorePattern": "^_" }], // Warn on unused variables, ignore those starting with _
      "curly": "error", // Require curly braces for all control statements
      "semi": ["error", "always"], // Enforce semicolons


      "quotes": ["error", "double", { "avoidEscape": true }], // Enforce double quotes



      "indent": ["error", 2], // Enforce 2-space indentation
      "comma-dangle": ["error", "always-multiline"], // Require trailing commas in multiline objects/arrays
      "no-console": "warn", // Warn on console usage
      "arrow-spacing": ["error", { "before": true, "after": true }], // Enforce spacing around arrow functions
    },
  },
]);