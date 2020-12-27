$(document).ready(function(){
    $(".current-user-image").hover(function(){
        $(this).css("filter", "brightness(50%)");
        $(this).siblings("button").show();
    },function(){
        $(this).css("filter", "brightness(100%)");
        $(this).siblings("button").hide();
    })

    // Add Flower Form
    $("input[id='is_wildflower']").click(function() {
        if($(this).is(":checked")){
            $(".location").addClass("d-block")
            $(".location").removeClass("d-none")
            $(".occasions").addClass("d-none")
            $(".occasions").removeClass("d-block")
        } else {
            $(".location").addClass("d-none")
            $(".location").removeClass("d-block")
            $(".occasions").addClass("d-block")
            $(".occasions").removeClass("d-none")
        }
    })
})