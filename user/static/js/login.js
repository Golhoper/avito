$("#check_name_button").click(function () {
    $.ajax({
        type: "GET",
        url: "login_check/",
        data: {
            "login": $("#login").val(),
            "password": $("#password").val(),
        },
        dataType: "text",
        cache: false,
        success: function (omg) {
            console.log(omg);
            var ggwp = JSON.parse(omg);
            if (ggwp.login == "empty") {
                document.getElementById("logincheck").innerHTML = "<div id=\"logincheck\"> Пусто </div></i>";
            }
            else if (ggwp.login == "busy") {
                document.getElementById("logincheck").innerHTML = "<div id=\"logincheck\"> Занят </div></i>";
            }
            else if (ggwp.login == "unknown") {
                document.getElementById("logincheck").innerHTML = "<div id=\"logincheck\"> Ошибка введенного поля </div></i>";
            }

            if (ggwp.password == "empty") {
                document.getElementById("passwordcheck").innerHTML = "<div id=\"passwordcheck\"> Пусто </div></i>";
            }
            else if (ggwp.password == "busy") {
                document.getElementById("passwordcheck").innerHTML = "<div id=\"passwordcheck\"> Занят </div></i>";
            }
            else if (ggwp.password == "unknown") {
                document.getElementById("passwordcheck").innerHTML = "<div id=\"passwordcheck\"> Ошибка введенного поля </div></i>";
            }
        }
    });
});
