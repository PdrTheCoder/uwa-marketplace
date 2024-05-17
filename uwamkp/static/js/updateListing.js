$(function () {
  // toggle modal when click delete btn
  $("#btn-deleteListing").on("click", function (e) {
    e.preventDefault();
    let deleteUrl = $(this).attr("deleteUrl");
    $("#confirmDelete").data("deleteUrl", deleteUrl).modal("show");
  });


  $("#btn-yes-delete").click(function () {
    let deleteUrl = $("#btn-deleteListing").attr("deleteUrl");
    let redirectUrl = $("#redirectUrl").val();
    patchListing(deleteUrl, { deleted: true })
      .then((res) => {
        if (res.code === 0) {
          console.log(res.msg);
        } else {
          console.log(res.msg);
        }
        window.location.replace(redirectUrl);
      })
      .catch((err) => {
        console.log(err);
      });
  });
});
