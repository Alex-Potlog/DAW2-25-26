document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');
    const themeToggleMobile = document.getElementById('themeToggleMobile');
    const body = document.body;
    const hamburger = document.getElementById('hamburger');
    const closeMenu = document.getElementById('closeMenu');
    const mobileMenu = document.getElementById('mobileMenu');
    
    //
    function setTheme(theme) {
        if (theme === 'dark') {
            body.classList.add('dark-mode');
            themeToggle.classList.add('dark-mode-active');
            themeToggle.textContent = '☀️ Mode Clar';
            if (themeToggleMobile) {
                themeToggleMobile.classList.add('dark-mode-active');
                themeToggleMobile.textContent = '☀️ Mode Clar';
            }
        } else {
            body.classList.remove('dark-mode');
            themeToggle.classList.remove('dark-mode-active');
            themeToggle.textContent = '🌙 Mode Fosc';
            if (themeToggleMobile) {
                themeToggleMobile.classList.remove('dark-mode-active');
                themeToggleMobile.textContent = '🌙 Mode Fosc';
            }
        }
    }
    
    // Comprovar preferència guardada
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        setTheme('dark');
    }
    
    // Event listeners per als botons de tema
    themeToggle.addEventListener('click', function() {
        const newTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
        setTheme(newTheme);
        localStorage.setItem('theme', newTheme);
    });
    
    if (themeToggleMobile) {
        themeToggleMobile.addEventListener('click', function() {
            const newTheme = body.classList.contains('dark-mode') ? 'light' : 'dark';
            setTheme(newTheme);
            localStorage.setItem('theme', newTheme);
            closeMobileMenu(); // Tanca el menú després de canviar el tema
        });
    }
    
    // ===== MENÚ MÒBIL =====
    function openMobileMenu() {
        mobileMenu.classList.add('active');
        hamburger.classList.add('active');
        document.body.style.overflow = 'hidden'; // Evita scroll
    }
    
    function closeMobileMenu() {
        mobileMenu.classList.remove('active');
        hamburger.classList.remove('active');
        document.body.style.overflow = ''; // Restaura scroll
    }
    
    // Event listeners per al menú mòbil
    hamburger.addEventListener('click', openMobileMenu);
    closeMenu.addEventListener('click', closeMobileMenu);
    
    // Tanca el menú en fer clic a un enllaç
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
        link.addEventListener('click', closeMobileMenu);
    });
    
    // Tanca el menú en fer clic fora
    mobileMenu.addEventListener('click', function(e) {
        if (e.target === mobileMenu) {
            closeMobileMenu();
        }
    });
    
    // Tanca el menú amb la tecla ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            closeMobileMenu();
        }
    });
});