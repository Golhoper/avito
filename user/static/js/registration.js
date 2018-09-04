$("#check_name_button").click(function () {
    $.ajax({
        type: "GET",
        url: "registration_check/",
        data: {
            "login": $("#login").val(),
            "first_name": $("#first_name").val(),
            "last_name": $("#last_name").val(),
            "password": $("#password").val(),
            "password_r": $("#password_r").val(),
            "email": $("#email").val(),
        },
        dataType: "text",
        cache: false,
        success: function (omg) {
            var ggwp = JSON.parse(omg)
            if (ggwp.login == "back to login") {
                head = "http://"
                host = document.location.host
                go_to = "/user/login/"
                document.location.href = head + host + go_to;
            }
            if (ggwp.login == "free") {
                document.getElementById("logincheck").innerHTML = "<i class=\"far fa-check-circle\"></i>";
            }
            else if (ggwp.login == "busy") {
                document.getElementById("logincheck").innerHTML = "<i class=\"far fa-times-circle\"></i>";
            }
            else if (ggwp.login == "error") {
                document.getElementById("logincheck").innerHTML = "<i class=\"fas fa-exclamation-circle\"></i>";
            }

            if (ggwp.password == "not equal") {
                document.getElementById("passwordcheck").innerHTML = "<i class=\"far fa-times-circle\"></i>";
            }
            else if (ggwp.password == "equal") {
                document.getElementById("passwordcheck").innerHTML = "<i class=\"far fa-check-circle\"></i>";
            }

            if (ggwp.email == "correct") {
                document.getElementById("emailcheck").innerHTML = "<i class=\"far fa-check-circle\"></i>";
            }
            else {
                document.getElementById("emailcheck").innerHTML = "<i class=\"far fa-times-circle\"></i>";
            }
        }
    });
});
