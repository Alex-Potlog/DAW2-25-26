import js from '@eslint/js'; // Importa el plugin d'ESLint per JS
import globals from 'globals'; // Importa definicions globals per diferents entorns (browser, node, etc.)
import { defineConfig } from 'eslint/config'; // Importa la funció per definir la configuració d'ESLint
export default defineConfig([
{
  files: ['**/*.{js,mjs,cjs}'], // Aplica la configuració a tots els fitxers JS dins de qualsevol subcarpeta del projecte
  plugins: { js }, // Activa el plugin de JavaScript
  extends: ['js/recommended'], // Configuració recomanada
  languageOptions: {
    globals: globals.browser, // Defineix globals del navegador, com window, document, etc.
  },
    rules: {
      semi: ['error', 'always'], // Punt i coma obligatori
      quotes: ['error', 'single'], // Cometes simples
      'no-unused-vars': 'warn', // Avis per variables no utilitzades
    },
  },
]);