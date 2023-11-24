// Функция для обновления отсчета
function updateCountdown() {
    // Получаем текущее время
    const now = new Date().getTime();

    // Получаем время начала отсчета из Local Storage
    let startTime = localStorage.getItem('startTime');

    // Если время начала еще не установлено или прошло более 1 часа, сбрасываем его
    if (!startTime || Math.abs(now - startTime) >= 3600000) {
        startTime = now;
        localStorage.setItem('startTime', startTime);
    }

    // Вычисляем оставшееся время в миллисекундах (1 час = 3600000 миллисекунд)
    const remainingTime = 3600000 - (now - startTime);

    const hours = Math.floor(remainingTime / (1000 * 60 * 60));
    const minutes = Math.floor((remainingTime % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((remainingTime % (1000 * 60)) / 1000);

    // Обновляем текст на странице
    document.getElementById('countdown').innerHTML = `${hours}ч ${minutes}м ${seconds}с`;
}

// Обновляем отсчет каждую секунду
setInterval(updateCountdown, 1000);

window.onload = updateCountdown;
