$("#modal-url").on("submit", ".js-book-create-form", function () {

    $(".js-create-url").click(function () {
        $.ajax({
        url: '/urls/create/',
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
            $("#modal-url").modal("show");
        },
        success: function (data) {
            $("#modal-url .modal-content").html(data.html_form);
        }
        });
    });

});