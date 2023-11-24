function updateStyles() {

    const fontCheckbox = document.getElementById('fontCheckbox');
    const colorCheckbox = document.getElementById('colorCheckbox');
    const backgroundCheckbox = document.getElementById('backgroundCheckbox');

    const content = document.getElementById('content');

    content.style.fontSize = '';
    content.style.color = '';
    content.style.backgroundColor = 'white';

    var colorInput = document.getElementById('colorInput');
    if (colorInput) {
        colorInput.remove();
    }
    var BackcolorInput = document.getElementById('BackcolorInput');
    if (BackcolorInput) {
        BackcolorInput.remove();
    }
    var textInput = document.getElementById('textInput');
    if (textInput) {
        textInput.remove();
    }


    if (fontCheckbox.checked) {

        let textInput = document.createElement("input");
        textInput.id="textInput"
        textInput.type = "number";
        textInput.min = "10";
        textInput.max = "100";
        textInput.onchange = function () {
            content.style.fontSize = `${this.value}px`;
        };

        var parent = document.getElementById("fontsizeinput");
        parent.insertAdjacentElement('afterend', textInput);
    }
    if (colorCheckbox.checked) {
        // Используйте let вместо var, чтобы создать новую переменную внутри блока
        let colorInput = document.createElement("input");
        colorInput.id="colorInput"
        colorInput.type = "color";
        colorInput.value = "#000000";
        colorInput.onchange = function () {
            content.style.color = this.value;
        };

        var parent = document.getElementById("textcolorinput");
        parent.insertAdjacentElement('afterend', colorInput);
    }
    if (backgroundCheckbox.checked) {
        let BackcolorInput = document.createElement("input");
        BackcolorInput.id="BackcolorInput"
        BackcolorInput.type = "color";
        BackcolorInput.value = "#ffffff";
        BackcolorInput.onchange = function () {
             content.style.background = this.value;
        };

        var parent = document.getElementById("backgroundinput");
        parent.insertAdjacentElement('afterend', BackcolorInput);
    }
}
