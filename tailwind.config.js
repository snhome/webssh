/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./webssh/**/*.{html,js}"],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms'),
  ],
}
