$(document).ready(function(){
    $(".current-user-image").click(function(){
        alert("Test")
    })

    $(".current-user-image").hover(function(){
        $(this).css("filter", "brightness(50%)");
        $(this).siblings("button").show();
    },function(){
        $(this).css("filter", "brightness(100%)");
        $(this).siblings("button").hide();
    })

    $(".user-image-view-btn").hover(function(){
        $(this).css("filter", "brightness(50%)");
        $(this).siblings("button").show();
    },function(){
        $(this).css("filter", "brightness(100%)");
        $(this).siblings("button").hide();
    })
})