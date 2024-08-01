document.querySelectorAll('.nav-item.dropdown').forEach(function (element) {
    element.addEventListener('mouseenter', function () {
        this.querySelector('.dropdown-menu').style.display = 'block';
    });
    element.addEventListener('mouseleave', function () {
        this.querySelector('.dropdown-menu').style.display = 'none';
    });
});