$(document).ready(function (){
	$(document).scroll(function () {
        var scroll = $(this).scrollTop();
        var navPosition = $("header").position();
        var contentPosition = $("content").position();
        if (scroll >= navPosition.top) {
            $('nav').addClass("navbar-fixed-top");
        }
        if (scroll < contentPosition.top) {
            $('nav').removeClass("navbar-fixed-top");
        }
    });
});