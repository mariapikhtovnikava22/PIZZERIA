window.addEventListener('scroll', function() {
    var targetElement = document.getElementById('imageContainer');
    var nav = document.querySelector('.sticky-nav');

    var targetRect = targetElement.getBoundingClientRect();
    var scrollPosition = window.scrollY;
    var scrollThreshold = targetRect.bottom;

    if (scrollPosition >= 850) {
        nav.style.position = 'fixed';
        nav.style.top = '0';
        nav.style.opacity = 0.7;
    } else {
        nav.style.position = 'sticky';
        nav.style.top = '1';
        nav.style.opacity = 1;
    }
});

