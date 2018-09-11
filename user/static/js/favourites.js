function open_ajax(id) {
    delete_fav(id);
};
function delete_fav (id) {
    $.ajax({
        type: "GET",
        url: "delete_fav/",
        data: {
            "id": id,
        },
        dataType: "text",
        cache: false,
        success: function (omg) {
            var ggwp = JSON.parse(omg);
            document.getElementById(id).remove();
            alert(ggwp.answer);
        }
    });
};