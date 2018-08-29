$("#button_save").click(function () {
    $.ajax({
        type: "GET",
        url: "profile_check/",
        data: {
            "birthday": $("#birthday").val(),
            "country": $("#country").val(),
            "city": $("#city").val(),
            "street": $("#street").val(),
            "house_number": $("#house_number").val(),
            "house_block": $("#house_block").val(),
        },
        dataType: "text",
        cache: false,
        success: function (omg) {
            console.log("gg");
            // var ggwp = JSON.parse(omg);
            // if (ggwp.login == "go to profile") {
            //     head = "http://";
            //     host = document.location.host;
            //     go_to = "/user/profile/";
            //     document.location.href = head + host + go_to;
            // }
            // if (ggwp.login == "empty") {
            //     document.getElementById("logincheck").innerHTML = "<div id=\"logincheck\"> Пусто </div></i>";
            // }
            // else if (ggwp.login == "busy") {
            //     document.getElementById("logincheck").innerHTML = "<div id=\"logincheck\"> Занят </div></i>";
            // }
            // else if (ggwp.login == "unknown") {
            //     document.getElementById("logincheck").innerHTML = "<div id=\"logincheck\"> Ошибка введенного поля </div></i>";
            // }

        }
    });
});