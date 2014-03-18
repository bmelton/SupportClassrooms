$(document).ready(function() { 
    // Construct pagination block
    var total_pages = $("*[data-slider='content']").children().length;
    var construct_paginator = function() { 
        var slider_pagination = $("<ul></ul>").addClass("pagination");
        for(var i = 1; i <= total_pages; i++) { 
            $("<li><a data-slider-page='" + i + "' class='cycler' href='#'>" + i + "</a></li>").appendTo(slider_pagination);
        };
        var slider_pagination_container = $("<div></div>");
        slider_pagination_container
            .addClass("container");
        
        var slider_pagination_row = $("<div></div>");
        slider_pagination_row
            .addClass("row")
            .addClass("text-right")
            .css("margin", "-80px 0 100px 0")
            ;
         
        $(slider_pagination).appendTo(slider_pagination_row);
        $(slider_pagination_row).appendTo(slider_pagination_container);
        $(slider_pagination_container).insertAfter("#teaser");
    }
    construct_paginator();
    

    $("#teaser_container h1").addClass("on");

    $("#teaser_container div").css("min-height", "366px");

    $(".cycler").click(function(event) { 
        event.preventDefault();
        var page = $(this).attr("data-slider-page");
        console.log(page);
        for(var i = 0; i < total_pages; i++) { 
            if(i < page-1)
                $($("#teaser").children().children()[i]).css("display", "none");
        }
        var el = $(this).attr("href");
        el = el.replace("#", "");
        $("#teaser").removeClass();
        $("#teaser").addClass(el);
        
        $("#teaser_container h1").removeClass();
        $("#teaser_container h1").addClass("off");
        window.setTimeout(function() { 
            $("#teaser_container h1").removeClass();
            $("#teaser_container h1").addClass("on");
        }, 280);
    });
});
