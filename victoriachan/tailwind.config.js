/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    /**
     * HTML. Paths to Django template files that utilises Tailwind CSS classes.
     */
    "./frontend/**/*.{js,css}",
    "./home/templates/**/*.html",
    "./victoriachan/templates/**/*.html",
    "./templates/**/*.html",
  ],
  theme: {
    colors: {
      'blue': '#1fb6ff',
      'purple': '#7e5bef',
      'pink': '#ff49db',
      'orange': '#ff7849',
      'green': '#13ce66',
      'yellow': '#ffc82c',
      'gray-dark': '#273444',
      'gray': '#8492a6',
      'gray-light': '#d3dce6',
    },
    fontFamily: {
      sans: ['Graphik', 'sans-serif'],
      serif: ['Merriweather', 'serif'],
    },
    extend: {},
  },
  plugins: [],
}

