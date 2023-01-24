$(document).ready(() => {
  $('.delete').on('click', function () {
    const $my_doc = $(this);
    const _user_id = $(this).data('answer');
    $.ajax({
      url: "/delete",
      type: "get",
      data: {
        'user_id': _user_id,
      },
      dataType: "json",
      success: function (res) {
        if (res.bool) {
          $my_doc.parents(".content").remove(".content");
        } else {
          alert(res.message);
        }
      }
    });
  });
});