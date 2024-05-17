// search event
function get_url() {
  let query = $("#listing-search-input").val();
  let sort = $("#listing-sort-select").val();
  let show_sold = $("#toggleSold").is(":checked")? 'on':'off';
  return `/mylisting/listings?query=${query}&sort=${sort}&show_sold=${show_sold}`
}

function goQuery(){
  // get the query url and query
  let url = get_url();
  window.location.href = url;
}

$(function () {
  // bind modal show and pass key data to modal
  $(".mark-sold").on("click", function (e) {
    e.preventDefault();
    let markUrl = $(this).attr("markUrl");
    $("#confirmSold").data("markUrl", markUrl).modal("show");
  });

  // click on the btn-yes-sold
  $("#btn-yes-sold").click(function () {
    let markUrl = $("#confirmSold").data("markUrl");
    let redirectUrl = $('#redirectUrl').val();
    patchListing(markUrl, { sold: true })
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
