document.addEventListener('DOMContentLoaded', function() {
    const desktopNavLinks = document.querySelectorAll('nav.desktop ul li a');
    const mobileNavLinks = document.querySelectorAll('.mobile-dropdown li a');
    const navIcon = document.querySelector('#nav-icon3');
    const mobileDropdown = document.querySelector('.mobile-dropdown');
    const bodyElement = document.querySelector('body');
    const header = document.querySelector('header');
    const headerHeight = header.offsetHeight;

    function scrollToSection(event, targetElement) {
        event.preventDefault();
        const targetBottom = targetElement.offsetTop + targetElement.offsetHeight;
        const viewportHeight = window.innerHeight;
        const scrollToPosition = targetBottom - viewportHeight;

        window.scrollTo({
            top: scrollToPosition,
            behavior: 'smooth'
        });
    }

    function handleNavLinkClick(event) {
        const targetId = this.getAttribute('href').substring(1);
        const targetElement = document.getElementById(targetId);
        scrollToSection(event, targetElement);

        // Hide the mobile menu if it's open
        if (mobileDropdown.classList.contains('show')) {
            navIcon.classList.remove('open');
            mobileDropdown.classList.remove('show');
            bodyElement.style.overflow = '';
        }
    }

    desktopNavLinks.forEach(link => {
        link.addEventListener('click', handleNavLinkClick);
    });

    mobileNavLinks.forEach(link => {
        link.addEventListener('click', handleNavLinkClick);
    });

    navIcon.addEventListener('click', function() {
        navIcon.classList.toggle('open');
        mobileDropdown.classList.toggle('show');
        if (mobileDropdown.classList.contains('show')) {
            bodyElement.style.overflow = 'hidden';
        } else {
            bodyElement.style.overflow = '';
        }
    });

    // Scroll to Home on load
    const homeSection = document.getElementById('hero');
    if (homeSection) {
        const homeBottom = homeSection.offsetTop + homeSection.offsetHeight;
        const viewportHeight = window.innerHeight;
        const scrollToHomePosition = homeBottom - viewportHeight;

        window.scrollTo({
            top: scrollToHomePosition,
            behavior: 'smooth'
        });
    }
});
