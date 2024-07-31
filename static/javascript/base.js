document.addEventListener('DOMContentLoaded', function() {
    // Initialise AOS
    AOS.init();

    // Initialise VANTA
    VANTA.WAVES({
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
});