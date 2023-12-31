function calculateAgeAndVerify() {
  // Запрашиваем у пользователя дату рождения через prompt
    const dobString = prompt('Введите дату рождения в формате DD-MM-YY:');

    // Проверяем, что пользователь не нажал "Отмена" или ввел пустую строку
    if (!dobString) {
        alert('Вы не ввели дату рождения. Попробуйте еще раз.');
        return;
    }

    // Разбиваем введенную строку на составляющие
    const [day, month, year] = dobString.split('-').map(Number);

    // Проверяем, что введенные значения являются корректными числами
    if (isNaN(day) || isNaN(month) || isNaN(year)) {
        alert('Пожалуйста, введите корректную дату рождения в формате DD-MM-YY.');
        return;
    }

    // Создаем объект Date из введенных значений
    const dob = new Date(year < 100 ? 2000 + year : year, month - 1, day);

    // Проверяем, что дата рождения была корректно введена и существует
    if (isNaN(dob) || dob.getDate() !== day || dob.getMonth() + 1 !== month || dob.getFullYear() !== (year < 100 ? 2000 + year : year)) {
        alert('Пожалуйста, введите корректную и существующую дату рождения в формате DD-MM-YY.');
        return;
    }

    // Проверяем, не превышает ли введенная дата текущую дату
    const now = new Date();
    if (dob > now) {
        alert('Дата рождения не может быть в будущем. Пожалуйста, введите корректную дату.');
        return;
    }


    // Рассчитываем возраст
    let age = now.getFullYear() - dob.getFullYear();
    if (dob.getDate() > now.getDate())
    {
        age = age - 1;
    }

    // Определяем день недели
    const daysOfWeek = ['воскресенье', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота'];
    const dayOfWeek = daysOfWeek[dob.getDay()];

        // Проверяем, является ли пользователь совершеннолетним
        if (age >= 18) {
            alert(`Ваш возраст: ${age} лет. День недели вашего рождения: ${dayOfWeek}. Добро пожаловать на сайт!`);
            window.location.href = "http://127.0.0.1:8000/infos";
        } else {
            // Пользователь несовершеннолетний, запрашиваем разрешение родителей
            const parentalConsent = confirm(`Вы несовершеннолетний. Вам нужно разрешение родителей для использования сайта. Согласны?`);
            if (parentalConsent) {
                alert(`Спасибо за разрешение, ${age}-летний пользователь! День недели вашего рождения: ${dayOfWeek}. Добро пожаловать на сайт!`);
                window.location.href = "http://127.0.0.1:8000/infos";
            } else {
                alert('Извините, но вы не можете использовать сайт без разрешения родителей.');
            }
        }
    }