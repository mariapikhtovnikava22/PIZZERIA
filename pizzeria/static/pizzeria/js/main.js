function updateSizeField(select, id)
{
    var selectedSize = select.options[select.selectedIndex].value;
    document.getElementById(id).value = selectedSize;
}

function handleFormSubmit(event) {
  // Просим форму не отправлять данные самостоятельно
  event.preventDefault();

  // Получаем форму, которая вызвала событие
  const form = event.target;

  // Создаем объект FormData, чтобы собрать данные формы
  const formData = new FormData(form);

  // Используем Fetch API для отправки данных на сервер
  fetch(form.action, {
    method: form.method,
    body: formData,
  })
 .then(response => {
    // Обрабатываем ответ от сервера, если нужно
    return response.json();
  })
  .then(data => {
    // Обрабатываем данные, полученные от сервера
    console.log('Received data:', data);

    // Обновляем значение count
    const count = data.count;

    // Обновляем содержимое элементов <a>
    const links = document.querySelectorAll('.Lst a');
    links.forEach(link => {
        link.innerHTML = `Cart (${count})`;
    });
  })
  .catch(error => {
    // Обрабатываем ошибки, если есть
    console.error('Error:', error);
  });
}

// Выбираем все формы с классом 'pizza-form'
const forms = document.querySelectorAll('.pizza-form');

// Добавляем обработчик события ко всем выбранным формам
forms.forEach(function(form) {
  form.addEventListener('submit', handleFormSubmit);
});







