$(document).ready(function () {
  $('.delete').on('click', function () {
    var _user_id = $(this).data('answer');
    $.ajax({
      url: "/delete",
      type: "get",
      data: {
        _user_id: _user_id,
      },
      dataType: "json",
      success: function (res) {
        if (res.bool) {
          $this.parents(".content").remove();
        } else {
          alert(res.message);
        }
      }
    });
  });
});