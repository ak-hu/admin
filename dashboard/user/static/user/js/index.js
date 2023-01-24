$(document).ready(function () {
  $('.delete').on('click', () => {
    const $this = $(this);
    const _user_id = $(this).data('answer');
    $.ajax({
      url: "/delete",
      type: "get",
      data: {
        'user_id': _user_id,
      },
      dataType: "json",
      success: (res)=> {
        if (res.bool) {
          $this.parents(".content").remove();
          alert(res.message);
        } else {
          alert(res.message);
        }
        
      }
    });
  });
});