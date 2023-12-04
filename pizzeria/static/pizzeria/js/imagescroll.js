const boxes = document.querySelectorAll('.box');

function checkBoxes()
{
    const trigger = (window.innerHeight)/5*3 ;
    for (const box of boxes)
    {
        const topOfBox = box.getBoundingClientRect().top;
        if(topOfBox < trigger)
        {
            box.classList.add('show');
        }
        else
        {
            box.classList.remove('show');
        }
    }
}
window.addEventListener('scroll', checkBoxes);