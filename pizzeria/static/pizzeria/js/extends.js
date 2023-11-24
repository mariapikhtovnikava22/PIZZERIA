// Базовый класс Pizzeria
function PizzeriaBase(name, location) {
    this.name = name;
    this.location = location;
}

PizzeriaBase.prototype.getName = function () {
    return this.name;
};

PizzeriaBase.prototype.getLocation = function () {
    return this.location;
};

// Класс-наследник PizzaPlace
function PizzaPlace(name, location, pizzaType) {
    PizzeriaBase.call(this, name, location);
    this.pizzaType = pizzaType;
}

// Наследование
PizzaPlace.prototype = Object.create(PizzeriaBase.prototype);
PizzaPlace.prototype.constructor = PizzaPlace;

// Добавляем новые методы и геттеры/сеттеры
PizzaPlace.prototype.getPizzaType = function () {
    return this.pizzaType;
};

PizzaPlace.prototype.setPizzaType = function (type) {
    this.pizzaType = type;
};

// Декоратор
function decoratedMethod(originalMethod) {
    return function () {
        alert('Decorated Method Alert!');
        return originalMethod.apply(this, arguments);
    };
}

// Применяем декоратор к методу
PizzaPlace.prototype.getName = decoratedMethod(PizzaPlace.prototype.getName);

// Создаем объекты и демонстрируем их возможности
const pizzeria = new PizzeriaBase('Generic Pizzeria', 'Downtown');
const pizzaPlace = new PizzaPlace('Delicious Pizza', 'Midtown', 'Margherita');


// Базовый класс Pizzeria
class PizzeriaBase2 {
    constructor(name, location) {
        this.name = name;
        this.location = location;
    }

    getName() {
        return this.name;
    }

    getLocation() {
        return this.location;
    }
}

// Класс-наследник PizzaPlace
class PizzaPlace2 extends PizzeriaBase2 {
    constructor(name, location, pizzaType) {
        super(name, location);
        this.pizzaType = pizzaType;
    }

    getPizzaType() {
        return this.pizzaType;
    }

    setPizzaType(type) {
        this.pizzaType = type;
    }

    // Декоратор
    getName() {
        alert('Decorated Method Alert!');
        return super.getName();
    }
}

// Создаем объекты
const pizzeria2 = new PizzeriaBase2('Generic Pizzeria', 'Downtown');
const pizzaPlace2 = new PizzaPlace2('Delicious Pizza', 'Midtown', 'Margherita');

function ShowResExtends()
{

    console.log(pizzeria.getName()); // Generic Pizzeria
    console.log(pizzaPlace.getName()); // (появится alert) и затем вывод в консоль "Delicious Pizza"
    alert(pizzeria2.getName()); // Generic Pizzeria
    alert(pizzaPlace2.getName()); // (появится alert) и затем вывод в консоль "Delicious Pizza"
}

