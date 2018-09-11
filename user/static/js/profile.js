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
            var ggwp = JSON.parse(omg);
            alert(ggwp.answer);
        }
    });
});
$("#button_delete").click(function () {
    $.ajax({
        type: "GET",
        url: "profile_delete/",
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
            var ggwp = JSON.parse(omg);

            if (ggwp.answer == "deleted") {
                document.getElementById("birthday").value = ""
                document.getElementById("country").value = ""
                document.getElementById("city").value = ""
                document.getElementById("street").value = ""
                document.getElementById("house_number").value = ""
                document.getElementById("house_block").value = ""
                alert("Ваши данные были удалены!")
            }
        }
    });
});
function read(id) {
    $.ajax({
        type: "GET",
        url: "read_mes/",
        data: {
             "id": id,
            },
        dataType: "text",
        cache: false,
        success: function (omg) {
            document.getElementById(id).remove();
        }
    });
};