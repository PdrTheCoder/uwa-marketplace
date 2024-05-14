function searchItems() {
    const query = document.getElementById('search-input').value;
    // Implementing AJAX requests to update product listings
    console.log('Searching for:', query);
}

function sortItems() {
    const sortValue = document.getElementById('sort-select').value;
    // Implement AJAX requests to update the product list based on the selected sorting options
    console.log('Sorting by:', sortValue);
}

document.addEventListener('DOMContentLoaded', function() {
    // Perform initialisation after the page has loaded
    searchItems(); // Initial loading of product list
    sortItems();   // Initial load sorting
});
