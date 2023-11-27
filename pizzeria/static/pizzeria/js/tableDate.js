const today = new Date();
const dd = String(today.getDate()).padStart(2, '0');

const mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!

const yyyy = today.getFullYear();

const formattedToday = `${yyyy}-${mm}-${dd}`;

// Устанавливаем максимальную дату для input
document.getElementById('date').max = formattedToday;
document.getElementById('date').value = formattedToday;

// Ассоциативный массив для хранения дат
const dates = [];

// Функция для добавления даты в массив
function addDate() {
    const dateInput = document.getElementById('date');
    const dateString = dateInput.value;

    // Парсим введенную строку с датой
    const parts = dateString.split('/');
    const day = parseInt(parts[0]);
    const month = parseInt(parts[1]);
    const year = parseInt(parts[2]);

    // Проверяем корректность введенной даты
    if (!isNaN(day) && !isNaN(month) && !isNaN(year)) {
        dates.push({ day, month, year });
        dateInput.value = ''; // Очищаем поле ввода
        displayInputDates(); // Обновляем вывод входных данных
    } else {
        alert('Invalid date format. Please use DD/MM/YYYY.');
    }
}

// Функция для поиска самой поздней даты
function findLatestDate() {
    if (dates.length === 0) {
        alert('Please add dates first.');
        return;
    }

    // Находим максимальную дату среди добавленных
    const latestDate = dates.reduce((latest, current) => {
        if (!latest || current.year > latest.year ||
            (current.year === latest.year && current.month > latest.month) ||
            (current.year === latest.year && current.month === latest.month && current.day > latest.day)) {
            return current;
        } else {
            return latest;
        }
    });

    // Выводим результат
    const resultElement = document.getElementById('result');
    resultElement.textContent = `The latest date is: ${latestDate.day}/${latestDate.month}/${latestDate.year}`;
}

// Функция для отображения входных данных
function displayInputDates() {
    const datesList = document.getElementById('datesList');
    datesList.innerHTML = ''; // Очищаем текущий список

    dates.forEach(date => {
        const listItem = document.createElement('li');
        listItem.textContent = `${date.day}/${date.month}/${date.year}`;
        datesList.appendChild(listItem);
    });
}
