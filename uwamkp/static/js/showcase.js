function searchItems() {
    const query = document.getElementById('search-input').value;
    const page = 1;  // Reset to first page on new search
    fetchListings(page, query);
}

function sortItems() {
    const sortValue = document.getElementById('sort-select').value;
    const page = 1;  // Reset to first page on new sort
    fetchListings(page, null, sortValue);
}

function fetchListings(page, query = null, sort = null) {
    let url = `/showcase/?page=${page}`;
    if (query) {
        url += `&query=${query}`;
    }
    if (sort) {
        url += `&sort=${sort}`;
    }

    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.querySelector('.container').innerHTML = html;
        })
        .catch(error => console.warn('Error fetching listings:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    searchItems(); // Initial loading of product list
    sortItems();   // Initial load sorting
});
