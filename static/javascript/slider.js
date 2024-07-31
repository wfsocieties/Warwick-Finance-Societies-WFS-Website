document.addEventListener('DOMContentLoaded', function() {
    let items = document.querySelectorAll('.execSlider .execItem');
    let next = document.getElementById('execNext');
    let prev = document.getElementById('execPrev');
    
    let active = 2; 

    function loadShow() {
        let stt = 0;
        items.forEach((item, index) => {
            item.style.transform = 'none';
            item.style.zIndex = 1;
            item.style.filter = 'none';
            item.style.opacity = 1;
        });
        
        items[active].style.transform = `none`;
        items[active].style.zIndex = 1;
        items[active].style.filter = 'none';
        items[active].style.opacity = 1;

        for (let i = 1; i <= 2; i++) {
            let nextIndex = (active + i) % items.length;
            items[nextIndex].style.transform = `translateX(${120 * i}px) scale(${1 - 0.2 * i}) perspective(16px) rotateY(-1deg)`;
            items[nextIndex].style.zIndex = -i;
            items[nextIndex].style.filter = 'blur(5px)';
            items[nextIndex].style.opacity = 0.6;
        }

        for (let i = 1; i <= 2; i++) {
            let prevIndex = (active - i + items.length) % items.length;
            items[prevIndex].style.transform = `translateX(${-120 * i}px) scale(${1 - 0.2 * i}) perspective(16px) rotateY(1deg)`;
            items[prevIndex].style.zIndex = -i;
            items[prevIndex].style.filter = 'blur(5px)';
            items[prevIndex].style.opacity = 0.6;
        }
    }

    loadShow();

    next.onclick = function() {
        active = (active + 1) % items.length;
        loadShow();
    };

    prev.onclick = function() {
        active = (active - 1 + items.length) % items.length;
        loadShow();
    };
});