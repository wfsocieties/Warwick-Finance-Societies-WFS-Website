document.addEventListener('DOMContentLoaded', function () {
    AOS.init();

    function initVanta() {
        if (window.vantaEffect) {
            window.vantaEffect.destroy(); 
        }

        var mainContent = document.getElementById('mainContent');

        // Ensure dimensions are accurate before initializing VANTA
        var width = mainContent.offsetWidth;
        var height = mainContent.offsetHeight;

        if (window.innerWidth > 576) {
            mainContent.style.backgroundColor = 'transparent';

            // Use requestAnimationFrame to ensure proper initialization
            window.requestAnimationFrame(function() {
                window.vantaEffect = VANTA.WAVES({
                    el: mainContent,
                    mouseControls: true,
                    touchControls: true,
                    gyroControls: false,
                    minHeight: height,
                    minWidth: width,
                    scale: 1.00,
                    scaleMobile: 1.00,
                    color: 0x43d54,
                    shininess: 150.00,
                    waveHeight: 25.00,
                    waveSpeed: 1.35,
                    zoom: 0.65
                });
            });
        } else {
            mainContent.style.backgroundColor = '#243282';
            if (window.vantaEffect) {
                window.vantaEffect.destroy();
            }
        }
    }

    initVanta();

    window.addEventListener('resize', function() {
        initVanta(); // Reinitialize VANTA effect on resize
    });

    // Initialize on window load to ensure all layout is complete
    window.addEventListener('load', function() {
        initVanta();
    });
});

