/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Poppins', 'sans-serif'],
      },
      fontSize: {
        'xs': '.75rem', // Extra small (12px)
        'sm': '.875rem', // Small (14px)
        'base': '1rem', // Base (16px)
        'lg': '1.125rem', // Large (18px)
        'xl': '1.25rem', // Extra large (20px)
        '2xl': '1.5rem', // Double extra large (24px)
        '3xl': '1.875rem', // Triple extra large (30px)
        '4xl': '2.25rem', // Quadruple extra large (36px)
        '5xl': '3rem', // Quintuple extra large (48px)
      },
    },
  },
  plugins: [],
}

