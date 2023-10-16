// Получаем ссылку на элемент, который нужно прокрутить
var targetElement = document.getElementById('markscroll');

// Получаем ссылку на навигационную панель
var nav = document.querySelector('.sticky-nav');

// Устанавливаем начальные стили для навигационной панели
nav.style.position = 'sticky';
nav.style.top = '1';
nav.style.opacity = 1;

// Отслеживаем событие прокрутки
window.addEventListener('scroll', function() {
    // Получаем координаты целевого элемента
    var targetRect = targetElement.getBoundingClientRect();

    // Получаем текущее положение прокрутки
    var scrollPosition = window.scrollY;

    // Определяем момент начала изменения стилей
    var scrollThreshold = targetRect.bottom; // Начинать изменение стилей после прохождения целевого элемента

    if (scrollPosition > scrollThreshold) {
        // Изменяем стили при прокрутке после целевого элемента
        nav.style.position = 'fixed';
        nav.style.top = '0';
        nav.style.opacity = 0.7; // Устанавливаем прозрачность 0.7
    } else {
        // Возвращаем начальные стили, если прокрутка находится выше целевого элемента
        nav.style.position = 'sticky';
        nav.style.top = '1';
        nav.style.opacity = 1; // Возвращаем нулевую прозрачность
    }
});
