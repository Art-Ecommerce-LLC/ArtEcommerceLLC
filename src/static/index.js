// static/index.js
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('nav ul li a');
    const header = document.querySelector('header');
    const headerHeight = header.offsetHeight;

    navLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetElement = document.getElementById(targetId);
            const targetPosition = targetElement.offsetTop - headerHeight;
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        });
    });

    // Scroll to Home on load
    const homeSection = document.getElementById('hero');
    if (homeSection) {
        const homePosition = homeSection.offsetTop - headerHeight;
        window.scrollTo({
            top: homePosition,
            behavior: 'smooth'
        });
    }
});