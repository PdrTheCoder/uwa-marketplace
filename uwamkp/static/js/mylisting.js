$(function() {
    $(".c-delete-listing").on("click", function(){
        // get the listing id first
        let listingID = $(this).attr("id").split("-")[1];

        // send fetch request
        fetch(`/mylisting/listings/${listingID}`, {
            method: "PATCH",
            credentials: "include",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify( {deleted: true }) ,
            redirect: "follow",
        }).then((res) => {
            let resJson = res.json();
            if (resJson.code === 0) {
                console.log(resJson.msg)
            } else {
                console.log(resJson.msg);
            }
            window.location.replace("/mylisting/listings")
        })
        .catch((err) => {
            console.log(err);
        })
    })
});