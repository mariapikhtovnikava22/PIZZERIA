const body = document.querySelector('.pizza_elements');
const articles = document.querySelectorAll('.pizza_elements');
const walk = {x: 53, y: 53};
articles.forEach(article => {

function parallax(e) {
    const width = article.offsetWidth;
    const height = article.offsetHeight;

    let { offsetX: x, offsetY: y} = e;

    const xWalk = Math.round((e.x / width / 2 * walk.x) - (walk.x / 2))+1;
    const yWalk = Math.round((e.y / height / 2  * walk.y) - (walk.y / 2))+1;

    article.style.transform = `rotateY(${-xWalk}deg) rotateX(${yWalk}deg)`;
}

article.addEventListener('mousemove', parallax);
});