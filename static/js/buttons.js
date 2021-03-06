//Animation for clicking on carets that show and hide collapsible displays
$(".collapse-button").click(function() {
    var collapsible=$(this).attr("data-target");
    if($(collapsible).hasClass("show")) {
        $("i", this).addClass("fa-caret-down");    
        $("i", this).removeClass("fa-caret-up");  
    }
    else {
        $("i", this).addClass("fa-caret-up");    
        $("i", this).removeClass("fa-caret-down"); 
         $("html, body").animate({ scrollTop: $(collapsible).height()+"50px" }, 250);
    }
});

//Function to clear and reset search form
$("#resetSearch").click(function() {
    $('#filterModal textarea').each(function() {
        $(this).text('');
    });
    $('#filterModal input[type="number"]').each(function() {
        $(this).attr("value", "");
    });
    $('#filterModal input[type="checkbox"]').attr("checked", false);
    $('#filterModal input[name="category"]').each(function() {
        $(this).attr("checked",true);
    });
    $('#filterModal input[name="type"]').each(function() {
        $(this).attr("checked",true);
    });  
});

//Function to submit search form from name search and sort by
$(".submit-search").click(function() {
    var name = $("#search-form-input-name").val()
    var sortBy = $("#search-form-input-sort-by").val()
    $("#id_name").val(name)
    $("#id_sort_by").val(sortBy)
    $("#search-form").submit()
})

//Function to switch selection on clicking opposing options in search form
$('.opposite-switch').change(function() {
    var checked = $(this).prop("checked"); 
    var thisId = $(this).attr("id");
    var oppositeButton=$("input[value="+thisId+"]");
    if(checked==true && oppositeButton.prop("checked")==true) {
        oppositeButton.prop("checked",false);
    }    
});

//Bootstrap - tooltip display function
$(function () {
  $('[data-toggle="tooltip"]').tooltip();
});