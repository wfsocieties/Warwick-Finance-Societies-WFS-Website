document.addEventListener('DOMContentLoaded', function() {
    // Initialise AOS
    AOS.init();

    // Debug: Check if mainContent element exists
    var mainContent = document.getElementById('mainContent');
    if (mainContent) {
        console.log('mainContent element found.');
        console.log('mainContent dimensions:', mainContent.clientWidth, mainContent.clientHeight);
    } else {
        console.error('mainContent element not found.');
    }

    // Initialise VANTA
    /*
    VANTA.NET({
        el: "#mainContent",
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        color: 0xb15013,
        backgroundColor: 0x330a9a,
        points: 18.00,
        maxDistance: 18.00,
        spacing: 13.00
    })*/

    /*
    VANTA.DOTS({
        el: "#mainContent",
        mouseControls: true,
        touchControls: true,
        gyroControls: false,
        minHeight: 200.00,
        minWidth: 200.00,
        scale: 1.00,
        scaleMobile: 1.00,
        backgroundColor: 0x30a6a,
        size: 4.30,
        spacing: 41.00
    })*/


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