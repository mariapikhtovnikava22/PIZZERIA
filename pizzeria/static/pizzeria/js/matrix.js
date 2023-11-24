// Получаем ссылку на контейнер div с id="cont"
var div = document.getElementById("cont");

// Создаем элемент таблицы
var randomTable = document.createElement("table");
randomTable.setAttribute('id', "random_table");

// Добавляем таблицу в контейнер div
div.appendChild(randomTable);

// Функция для добавления новой строки в таблицу
function addRow() {
    const row = document.createElement("tr");

    const rowSize = randomTable.rows.length
        ? randomTable.rows.item(0).cells.length
        : 1;

    // Создаем ячейки для новой строки
    for (var i = 0; i < rowSize; i++) {
        const cell = createCell(null);
        row.appendChild(cell);
    }

    // Добавляем строку в таблицу
    randomTable.appendChild(row);
}

// Функция для добавления нового столбца в таблицу
function addColumn() {
    const rows = randomTable.rows;

    if (rows.length) {
        // Если есть строки, добавляем ячейки в каждую строку
        Array.prototype.forEach.call(rows, row => {
            const cell = createCell(null);
            row.appendChild(cell);
        });
    } else {
        // Если нет строк, добавляем новую строку и затем в нее ячейку
        addRow();
    }
}

// Функция для транспонирования таблицы
function transpose() {
    const rows = randomTable.rows;

    if (!rows) {
        return;
    }

    const rowCount = rows.length;
    const colCount = rows.item(0).cells.length;

    const newRows = {};

    // Заполняем новый объект данными из текущей таблицы
    for (var i = 0; i < rowCount; i++) {
        for (var j = 0; j < colCount; j++) {
            const cell = rows.item(i).cells.item(j);
            newRows[[j, i]] = [cell.innerText, cell.classList.contains("selected")];
        }
    }

    // Очищаем текущую таблицу
    randomTable.innerText = "";

    // Заполняем таблицу новыми данными
    for (var i = 0; i < colCount; i++) {
        const row = document.createElement("tr");

        for (var j = 0; j < rowCount; j++) {
            const cell = createCell(newRows[[i, j]][0]);

            if (newRows[[i, j]][1]) {
                cell.classList.add("selected");
            }

            row.appendChild(cell);
        }

        randomTable.appendChild(row);
    }
}

// Функция для создания таблицы заданного размера
function createTable(height, width) {
    randomTable.innerText = "";

    // Добавляем строки в таблицу
    while (height--) {
        addRow();
    }

    // Добавляем столбцы в таблицу
    while (width --> 1) {
        addColumn();
    }
}

// Функция для создания ячейки таблицы
function createCell(content) {
    const cell = document.createElement("td");
    // Если не задан контент, заполняем случайным числом
    cell.textContent = content ?? Math.floor(Math.random() * 10);

    // Добавляем обработчики событий для мыши
    cell.addEventListener('mouseover', onCellMouseOver);
    cell.addEventListener("click", onCellMouseClick);

    return cell;
}

// Обработчик события для наведения мыши на ячейку
function onCellMouseOver(e) {
    const cell = e.target;

    if (
        isLmbDown && !cell.classList.contains("selected")   // paint
        || isRmbDown && cell.classList.contains("selected")      // erase
    ) {
        selectCell(cell);
    }
}

// Обработчик события для клика на ячейку
function onCellMouseClick(e) {
    const cell = e.target;
    selectCell(cell);
}

// Функция для выделения ячейки согласно условиям
function selectCell(cell) {
    const maxSelection = document.getElementById("maxSelect").value;

    // Добавленные строки
    const selectedCellsInRow = Array.from(cell.parentElement.cells).filter(c => c.classList.contains("selected"));
    // Добавленные столбцы
    const selectedCellsInColumn = Array.from(randomTable.rows).map(r => r.cells[cell.cellIndex]).filter(c => c.classList.contains("selected"));

    // Проверка, чтобы нельзя было выделить соседей слева и справа
    const cellIndex = cell.cellIndex;
    if (
        cellIndex > 0 && cell.parentElement.cells[cellIndex - 1].classList.contains("selected") ||
        cellIndex < cell.parentElement.cells.length - 1 && cell.parentElement.cells[cellIndex + 1].classList.contains("selected")
    ) {
        return;
    }

    // Выделяем ячейку, если она еще не выделена, и не превышено максимальное количество выделений
    if (
        cell.classList.contains("selected") ||
        selectedCellsInRow.length < maxSelection &&
        selectedCellsInColumn.length < maxSelection
    ) {
        cell.classList.toggle("selected", !cell.classList.contains("selected"));
    }
}

// Функция для проверки, есть ли соседи с выделением
function hasNeighborSelected(cells, i) {
    return i > 0 && cells.item(i - 1).classList.contains("selected")
           || i < cells.length - 1 && cells.item(i + 1).classList.contains("selected");
}

// Переменные для отслеживания состояния кнопок мыши
var isLmbDown = false;
var isRmbDown = false;

// Обработчики событий для нажатия и отпускания кнопок мыши
document.addEventListener('mousedown', function(event) {
    if (event.button === 0) {
        isLmbDown = true;
    }

    if ("which" in event && event.which === 3) {
        isRmbDown = true;
    } else if ("button" && event.button === 2) {
        isRmbDown = true;
    }
});

document.addEventListener('mouseup', function(event) {
    if (event.button === 0) {
        isLmbDown = false;
    }

    if ("which" in event && event.which === 3) {
        isRmbDown = false;
    } else if ("button" && event.button === 2) {
        isRmbDown = false;
    }
});

// Отключаем контекстное меню при правом клике
randomTable.addEventListener("contextmenu", e => e.preventDefault());
