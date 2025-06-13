
import { withTheme } from 'tailwindcss-theme-variants';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default withTheme({
  content: [
    ['src/core/templates/**/*.html'],
  ],
  safelist: [
    'text-green',
    'bg-blue',
    'hover:underline',
  ],
    theme: {
      extend: {
        colors: {
          primary: '#fd8504',
          secondary: '#000000',
        },
        height: {
          'screen-minus-nav': 'calc(100vh - 57px)',
        },
        spacing: {
          1: 'var(--spacing-3)',
        },
        screens: {
          tablet: 'var(--breakpoint-tablet)',
        },
      },
    },
    plugins: [],
});
  