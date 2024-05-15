function searchItems() {
    const query = document.getElementById('search-input').value;
    const sort = document.getElementById('sort-select').value;
    console.log(`Searching for: ${query}, Sorting by: ${sort}`);
    fetchListings(1, query, sort);  // Reset to first page on new search
}

function sortItems() {
    const sort = document.getElementById('sort-select').value;
    const query = document.getElementById('search-input').value;
    console.log(`Sorting by: ${sort}, Searching for: ${query}`);
    fetchListings(1, query, sort);  // Reset to first page on new sort
}

function fetchListings(page, query = '', sort = 'newest') {
    let url = `/showcase/?page=${page}&query=${encodeURIComponent(query)}&sort=${sort}`;
    console.log(`Fetching listings from: ${url}`);

    fetch(url)
        .then(response => response.text())
        .then(html => {
            document.querySelector('.container').innerHTML = html;
            console.log('Listings fetched and updated.');
        })
        .catch(error => console.warn('Error fetching listings:', error));
}

document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.btn-primary');
    searchButton.addEventListener('click', searchItems);

    const sortSelect = document.getElementById('sort-select');
    sortSelect.addEventListener('change', sortItems);
});
