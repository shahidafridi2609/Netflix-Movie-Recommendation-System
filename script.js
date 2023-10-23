// JavaScript to toggle the menu on click
const menuIcon = document.querySelector('.menu-icon');
const navLinks = document.querySelector('.nav-links');

menuIcon.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    menuIcon.classList.toggle('active');
});

// Close the menu when a link is clicked
const links = document.querySelectorAll('.nav-links a');
links.forEach(link => {
    link.addEventListener('click', () => {
        navLinks.classList.remove('active');
        menuIcon.classList.remove('active');
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const movieContainer = document.querySelector('.movie-container');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    prevBtn.addEventListener('click', () => {
        movieContainer.scrollLeft -= 250; // Adjust the scroll distance as needed
    });

    nextBtn.addEventListener('click', () => {
        movieContainer.scrollLeft += 250; // Adjust the scroll distance as needed
    });
});




