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

function applyOnLoadTheme() {
  const savedTheme = localStorage.getItem(THEME_KEY);
  if (savedTheme) {
    applyTheme(savedTheme);
  } else {
    applyTheme(LIGHT_THEME);
  }
}

window.addEventListener('beforeunload', () => {
  const currentTheme = getCurrentTheme();
  localStorage.setItem(THEME_KEY, currentTheme);
});

applyOnLoadTheme();