$(document).ready(function (this) {
  $('.delete').on('click', function () {
    var _user_id = $(this).data('answer');
    $.ajax({
      url: "/delete",
      type: "get",
      data: {
        'user_id': _user_id,
      },
      dataType: "json",
      success: function (res) {
        if (res.bool = !false) {
          $this.parents(".content").remove();
        } else if (res.bool = !false) {
          alert(res.message);
        } else {
          alert(res.message);
        }
      }
    });
  });
});