// Light/Dark Change
const themeSwitch = document.getElementById('theme-switch')

themeSwitch.addEventListener("click", () => {
	document.querySelector("html").classList.toggle("darkmode");
})

// Navbar
const navbar = document.getElementById('navbar')

function openSidebar() {
	navbar.classList.add('show')
}

function closeSidebar() {
	navbar.classList.remove('show')
}
