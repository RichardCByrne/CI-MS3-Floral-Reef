$(document).ready(function(){
    $(".current-user-image").hover(function(){
        $(this).css("filter", "brightness(60%)");
        $(this).siblings("a").removeClass("d-none");
        $(this).siblings("a").addClass("d-inline");
    },function(){
        $(this).css("filter", "brightness(100%)");
        $(this).siblings("a").removeClass("d-inline");
        $(this).siblings("a").addClass("d-none");
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