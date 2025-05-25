// vite.config.js
import { defineConfig } from 'vite'

export default defineConfig({
  root: '.', 
  build: {
    outDir: 'static/frontend/dist',  
    emptyOutDir: true,              
    rollupOptions: {
      input: 'static/frontend/js/main.js',  
    },
    assetsDir: 'assets',            
  },
  base: '/static/frontend/dist/',  
})
