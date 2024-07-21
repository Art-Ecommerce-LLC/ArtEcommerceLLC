document.addEventListener('DOMContentLoaded', function() {
    var navIcon = document.querySelector('#nav-icon3');
    var mobileDropdown = document.querySelector('.mobile-dropdown');
    var bodyElement = document.querySelector('body');
    var navLinks = document.querySelectorAll('.mobile-dropdown li a');

    navIcon.addEventListener('click', function() {
        navIcon.classList.toggle('open');
        mobileDropdown.classList.toggle('show');
        if (mobileDropdown.classList.contains('show')) {
            bodyElement.style.overflow = 'hidden';
        } else {
            bodyElement.style.overflow = '';
        }
    });

    navLinks.forEach(function(link) {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            var targetId = this.getAttribute('href').substring(1);
            var targetElement = document.getElementById(targetId);
            var headerHeight = document.querySelector('header').offsetHeight;
            var targetPosition = targetElement.offsetTop - headerHeight;

            // Hide the mobile menu
            navIcon.classList.remove('open');
            mobileDropdown.classList.remove('show');
            bodyElement.style.overflow = '';

            // Scroll to the correct section
            window.scrollTo({
                top: targetPosition,
                behavior: 'smooth'
            });
        });
    });
});
