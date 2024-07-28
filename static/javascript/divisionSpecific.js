$(document).ready(function() {
    adjustImageHeight();
});

$(window).resize(function(){
    adjustImageHeight();
});

function adjustImageHeight() {
    var textHeight = $(".divisionBox .col-12.col-md-8").outerHeight();
    $(".divisionBox img").css("height", textHeight);
}