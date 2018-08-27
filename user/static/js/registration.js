$("#check_name_button").click(function () {
    $.ajax({
        type: "GET",
        url: "registration_check/",
        data: {
            "login": $("#log").val(),
        },
        dataType: "text",
        cache: false,
        success: function (data) {
            if (data == "free") {
                document.getElementById("demo").innerHTML = "<i class=\"far fa-check-circle\"></i>";
            }
            else if (data == "busy") {
                document.getElementById("demo").innerHTML = "<i class=\"far fa-times-circle\"></i>";
            }
        }
    });
});
