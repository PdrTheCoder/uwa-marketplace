function searchItems() {
    const query = document.getElementById('search-input').value;
    const sort = document.getElementById('sort-select').value;
    const url = `/showcase?query=${query}&sort=${sort}`;
    window.location.href = url;
}

function sortItems() {
    const query = document.getElementById('search-input').value;
    const sort = document.getElementById('sort-select').value;
    const url = `/showcase?query=${query}&sort=${sort}`;
    window.location.href = url;
}

document.addEventListener('DOMContentLoaded', function() {
    const searchButton = document.querySelector('.btn-primary');
    searchButton.addEventListener('click', searchItems);

    const sortSelect = document.getElementById('sort-select');
    sortSelect.addEventListener('change', sortItems);
});
