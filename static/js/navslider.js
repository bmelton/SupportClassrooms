$(document).ready(function() { 
    var appended = false;
    $(window).scroll(function() { 
        var this_id = $("*[data-sliderBar='true']").attr("data-sliderBarID");
        var a = $(window).scrollTop();
        var b = $("#" + this_id).offset().top;
        if(a > b) {
            // Scrolled below
            if(!appended) {
                var c = $("#" + this_id).clone().attr("id", "sliderBar").css("height", "0").appendTo("body");
                appended = true;
                window.setTimeout(function() { 
                    $(".logo.sneak").addClass("unsneak");
                    $(".logo.sneak").removeClass("sneak");
                    $("#sliderBar").addClass("on");
                }, 100);
                $.event.trigger("sliderDown", [this_id]);
            }
        }
        if(b > a || b == 0) {
            if(appended) {
                $("#sliderBar").remove();
                appended = false;
                $.event.trigger("sliderUp", [this_id]);
            }
            $(".logo.unsneak").addClass("sneak");
            $(".logo.unsneak").removeClass("unsneak");
        }
    });

    $(document).on("sliderDown", function(event, id) { 
        /*
        var el = $("<li></li>");
        el.html("<img class='logo unsneak' src='./images/logo.png'>");
        el.attr("id", "#sliderLogo");
        $("ul.nav.navbar-nav").prepend(el);
        */
    });

    $(document).on("sliderUp", function(event, id) { 
        /*
        $("#sliderLogo").remove();
        console.log(id);
        */
    });
});
