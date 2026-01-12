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

function applyTheme(theme) {
  const root = document.documentElement;

  if (theme === DARK_THEME) {
    root.classList.add('dark-mode');
    root.classList.remove('light-mode');
    isDark = true;
    const themeBtn = document.querySelector('#theme');
    if (themeBtn) themeBtn.textContent = 'Light Mode';
  } else {
    root.classList.add('light-mode');
    root.classList.remove('dark-mode');
    isDark = false;
    const themeBtn = document.querySelector('#theme');
    if (themeBtn) themeBtn.textContent = 'Dark Mode';
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

function initHamburger() {
  const hamburger = document.getElementById('hamburger');
  const nav = document.getElementById('header-nav');
  const overlay = document.getElementById('overlay');

  hamburger.addEventListener('click', function (e) {
    e.preventDefault();
    hamburger.classList.toggle('active');
    nav.classList.toggle('active');
    overlay.classList.toggle('active');
    document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
  });

  overlay.addEventListener('click', function () {
    hamburger.classList.remove('active');
    nav.classList.remove('active');
    overlay.classList.remove('active');
  });

  const navLinks = nav.querySelectorAll('a');
  navLinks.forEach(link => {
    link.addEventListener('click', function () {
      hamburger.classList.remove('active');
      nav.classList.remove('active');
      overlay.classList.remove('active');
    });
  });
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', function () {
    applyOnLoadTheme();
    initHamburger();
  });
} else {
  applyOnLoadTheme();
  initHamburger();
}