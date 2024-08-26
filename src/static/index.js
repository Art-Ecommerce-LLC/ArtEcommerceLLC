// document.addEventListener('DOMContentLoaded', function() {
//     const navLinks = document.querySelectorAll('nav ul li a');
//     const header = document.querySelector('header');
//     const headerHeight = header.offsetHeight;

//     navLinks.forEach(link => {
//         link.addEventListener('click', function(event) {
//             event.preventDefault();
//             const targetId = this.getAttribute('href').substring(1);
//             const targetElement = document.getElementById(targetId);
//             const targetBottom = targetElement.offsetTop + targetElement.offsetHeight;
//             const viewportHeight = window.innerHeight;
//             const scrollToPosition = targetBottom - viewportHeight;

//             window.scrollTo({
//                 top: scrollToPosition,
//                 behavior: 'smooth'
//             });
//         });
//     });

//     // Scroll to Home on load
//     const homeSection = document.getElementById('hero');
//     if (homeSection) {
//         const homeBottom = homeSection.offsetTop + homeSection.offsetHeight;
//         const viewportHeight = window.innerHeight;
//         const scrollToHomePosition = homeBottom - viewportHeight;

//         window.scrollTo({
//             top: scrollToHomePosition,
//             behavior: 'smooth'
//         });
//     }
// });
