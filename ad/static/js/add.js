$("#button_save").click(function () {
    $.ajax({
        type: "GET",
        url: "add_new_check/",
        data: {
            "title": $("#title").val(),
            "description": $("#description").val(),
            "price": $("#price").val(),
        },
        dataType: "text",
        cache: false,
        success: function (omg) {
            var ggwp = JSON.parse(omg);
            alert(ggwp.answer);
        }
    });
});