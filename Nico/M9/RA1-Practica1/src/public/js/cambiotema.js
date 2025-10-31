// Clase para manejar el tema en múltiples páginas
class ThemeManager {
    constructor(buttonId = 'CambioTema') {
        this.buttonId = buttonId;
        this.button = null;
        this.init();
    }

    // Inicializar el gestor de temas
    init() {
        // Aplicar el tema guardado ANTES de que se cargue la página
        this.applySavedTheme();

        // Cuando el DOM esté listo, configurar el botón
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.setupButton());
        } else {
            this.setupButton();
        }
    }

    // Aplicar el tema guardado inmediatamente
    applySavedTheme() {
        const savedTheme = localStorage.getItem('theme');
        if (savedTheme === 'dark') {
            document.documentElement.classList.add('dark-mode');
        }
    }

    // Configurar el botón existente
    setupButton() {
        this.button = document.getElementById(this.buttonId);

        if (!this.button) {
            console.warn(`Botón con id "${this.buttonId}" no encontrado`);
            return;
        }

        // Actualizar el texto/icono del botón según el tema actual
        this.updateButtonContent();

        // Agregar el evento click
        this.button.addEventListener('click', () => this.toggleTheme());
    }

    // Cambiar entre modo claro y oscuro
    toggleTheme() {
        const isDark = document.documentElement.classList.toggle('dark-mode');

        // Guardar en localStorage
        localStorage.setItem('theme', isDark ? 'dark' : 'light');

        // Actualizar el botón
        this.updateButtonContent();

        // Disparar evento personalizado
        this.dispatchThemeChangeEvent(isDark);
    }

    // Actualizar el contenido del botón
    updateButtonContent() {
        if (!this.button) return;

        const isDark = document.documentElement.classList.contains('dark-mode');

        // Cambiar el texto o icono del botón
        if (this.button.querySelector('.icon')) {
            this.button.querySelector('.icon').textContent = isDark ? '☀️' : '🌙';
        } else {
            this.button.textContent = isDark ? '☀️ Modo Claro' : '🌙 Modo Oscuro';
        }

        // Cambiar atributo aria para accesibilidad
        this.button.setAttribute('aria-label',
            isDark ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro'
        );
    }

    // Disparar evento personalizado cuando cambia el tema
    dispatchThemeChangeEvent(isDark) {
        const event = new CustomEvent('themeChanged', {
            detail: { theme: isDark ? 'dark' : 'light' }
        });
        document.dispatchEvent(event);
    }

    // Obtener el tema actual
    getCurrentTheme() {
        return document.documentElement.classList.contains('dark-mode') ? 'dark' : 'light';
    }

    // Establecer un tema específico
    setTheme(theme) {
        if (theme === 'dark') {
            document.documentElement.classList.add('dark-mode');
        } else {
            document.documentElement.classList.remove('dark-mode');
        }
        localStorage.setItem('theme', theme);
        this.updateButtonContent();
    }
}

// Inicializar automáticamente
const themeManager = new ThemeManager('CambioTema');

// Debug opcional
document.addEventListener('themeChanged', (e) => {
    console.log('Tema cambiado a:', e.detail.theme);
});
