$(document).ready(function(){
    $(".current-user-image").hover(function(){
        $(this).css("filter", "brightness(50%)");
        $(this).siblings("button").show();
    },function(){
        $(this).css("filter", "brightness(100%)");
        $(this).siblings("button").hide();
    })
})