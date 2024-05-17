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
  // this is the general patch function
  async function patchListing(url = "", data = {}) {
    const response = await fetch(url, {
      method: "PATCH",
      credentials: "include",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
      redirect: "follow",
    });
    return response.json();
  }

  // bind modal show and pass key data to modal
  $(".mark-sold").on("click", function (e) {
    e.preventDefault();
    let listingID = $(this).attr("listingId");
    $("#confirmSold").data("listingId", listingID).modal("show");
  });

  // click on the btn-yes-sold
  $("#btn-yes-sold").click(function () {
    let soldId = $("#confirmSold").data("listingId");
    patchListing(`/mylisting/listings/${soldId}`, { sold: true })
      .then((res) => {
        if (res.code === 0) {
          console.log(res.msg);
        } else {
          console.log(res.msg);
        }
        window.location.replace("/mylisting/listings");
      })
      .catch((err) => {
        console.log(err);
      });
  });
});
