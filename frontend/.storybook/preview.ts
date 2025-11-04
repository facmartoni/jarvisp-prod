import type { Preview } from '@storybook/react-vite'
import { themes } from 'storybook/internal/theming'
import React from 'react'
import '../src/index.css'

const preview: Preview = {
  parameters: {
    docs: {
      theme: themes.dark,
    },
    controls: {
      matchers: {
       color: /(background|color)$/i,
       date: /Date$/i,
      },
    },

    backgrounds: {
      options: {
        dark: { name: 'dark', value: '#000000' },
        light: { name: 'light', value: '#ffffff' }
      }
    },

    a11y: {
      // 'todo' - show a11y violations in the test UI only
      // 'error' - fail CI on a11y violations
      // 'off' - skip a11y checks entirely
      test: 'todo'
    }
  },

  decorators: [
    (Story, context) => {
      // Don't apply wrapper in Docs view
      if (context.viewMode === 'docs') {
        return React.createElement(Story);
      }
      // Apply dark background wrapper in Canvas view
      return React.createElement('div', { 
        style: { 
          backgroundColor: '#000000',
          width: '100vw',
          minHeight: '100vh',
          margin: 0,
          padding: '2rem',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          position: 'fixed',
          top: 0,
          left: 0,
          right: 0,
          bottom: 0
        } 
      }, React.createElement(Story));
    },
  ],

  initialGlobals: {
    backgrounds: {
      value: 'dark'
    }
  }
};

export default preview;