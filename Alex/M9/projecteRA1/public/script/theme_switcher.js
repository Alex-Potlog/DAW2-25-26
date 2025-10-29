const THEME_KEY = 'preferred-theme';
const DARK_THEME = 'dark';
const LIGHT_THEME = 'light';
let isDark = false;

function getCurrentTheme() {
  if (isDark) {
    return DARK_THEME;
  }
  return LIGHT_THEME;
}

// Apply the theme to the document
function applyTheme(theme) {
  const root = document.documentElement;

  if (theme === DARK_THEME) {
    root.classList.add('dark-mode');
    root.classList.remove('light-mode');
    isDark = true;
    document.querySelector('#theme').textContent = 'Light Mode';
  } else {
    root.classList.add('light-mode');
    root.classList.remove('dark-mode');
    isDark = false;
    document.querySelector('#theme').textContent = 'Dark Mode';
  }
}

function toggleTheme() {
  const current = getCurrentTheme();
  const newTheme = current === DARK_THEME ? LIGHT_THEME : DARK_THEME;
  applyTheme(newTheme);
  return newTheme;
}

// Initialize light mode by default when page loads
document.addEventListener('DOMContentLoaded', function () {
  applyTheme(LIGHT_THEME);
});