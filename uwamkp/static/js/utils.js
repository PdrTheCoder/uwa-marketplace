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
