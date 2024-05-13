function searchItems() {
    const query = document.getElementById('search-input').value;
    // Implement AJAX request to update product list
    console.log('Searching for:', query);
}

function sortItems() {
    const sortValue = document.getElementById('sort-select').value;
    // Implement an AJAX request to update the product list according to the selected sorting option.
    console.log('Sorting by:', sortValue);
}
