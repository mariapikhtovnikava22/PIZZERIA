const imageContainer = document.getElementById("imageContainer");
const animationTimeInput = document.getElementById("animationTime");
const storedAnimationTime = localStorage.getItem("animationTime");

document.addEventListener("DOMContentLoaded", function() {
  // Получаем значение из localStorage, если оно там есть
    const storedAnimationTime = localStorage.getItem("animationTime");
    console.log(storedAnimationTime);

  // Если значение есть, устанавливаем переменную в CSS
  if (storedAnimationTime) {
    document.documentElement.style.setProperty("--animation-time", storedAnimationTime);
  }
});

if (imageContainer) {
    const images = imageContainer.childNodes;
    images.forEach(image =>
    {
        image.addEventListener("click", function ()
        {
        window.location.href = "http://127.0.0.1:8000/#promo";
        });
    });

    // Проверка на наличие фокуса страницы
    window.addEventListener("focus", function()
    {
        images.forEach(i => {
            if(i.style) i.style.animationPlayState = "running";
        });
    });
     window.addEventListener("blur", function()
    {
        images.forEach(i => {
            if(i.style) i.style.animationPlayState = "paused";
        });
    });
}

if (animationTimeInput) {

    const storedAnimationTime = localStorage.getItem("animationTime");

    // Если значение есть, устанавливаем его в input
    if (storedAnimationTime) {
    animationTimeInput.value = storedAnimationTime.replace('s', ''); // убираем 's' для ввода в input
    // Устанавливаем переменную в CSS
    document.documentElement.style.setProperty("--animation-time", storedAnimationTime);
    }

    animationTimeInput.addEventListener("input", function () {
        const animationTime = animationTimeInput.value + "s";
        document.documentElement.style.setProperty("--animation-time", animationTime);
        localStorage.setItem("animationTime", animationTime);
    });
}