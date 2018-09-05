$("#notify_seller").click(function () {
    $.ajax({
        type: "GET",
        url: "send_msg_seller/",
        data: {
            "message": $("#message").val(),
            "id": $("#id").val(),
        },
        dataType: "text",
        cache: false,
        success: function (omg) {
            var ggwp = JSON.parse(omg);
            alert(ggwp.answer);
        }
    });
});
