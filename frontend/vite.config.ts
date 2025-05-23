import { defineConfig, UserConfig } from "vite";
import react from "@vitejs/plugin-react";

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      "/items": "http://localhost:5000",
      "/cart": "http://localhost:5000",
      "/checkout": "http://localhost:5000",
      "/admin": "http://localhost:5000",
    },
  },
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: "./src/setupTests.ts",
  },
} as UserConfig);
