document.addEventListener('DOMContentLoaded', function () {
    AOS.init();

    function initVanta() {
        if (window.vantaEffect) {
            window.vantaEffect.destroy(); 
        }

        if (window.innerWidth > 576) {
            window.vantaEffect = VANTA.WAVES({
                el: "#mainContent",
                mouseControls: true,
                touchControls: true,
                gyroControls: false,
                minHeight: 200.00,
                minWidth: 200.00,
                scale: 1.00,
                scaleMobile: 1.00,
                color: 0x43d54,
                shininess: 150.00,
                waveHeight: 25.00,
                waveSpeed: 1.35,
                zoom: 0.65
            });
        } else {
            document.getElementById('mainContent').style.backgroundColor = '#243282';
        }
    }

    initVanta();

    window.addEventListener('resize', initVanta);
});