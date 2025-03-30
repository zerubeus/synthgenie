import { defineConfig } from 'vite';
import tailwindcss from '@tailwindcss/vite';
import { reactRouter } from '@react-router/dev/vite';
import tsconfigPaths from 'vite-tsconfig-paths';

// https://vite.dev/config/
export default defineConfig(({ command }) => ({
  ssr: {
    noExternal: command === 'build' ? true : undefined,
  },
  plugins: [tailwindcss(), reactRouter(), tsconfigPaths()],
}));
