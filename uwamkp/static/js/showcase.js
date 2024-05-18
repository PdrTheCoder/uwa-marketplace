// Function to handle search
function searchItems() {
    const query = document.getElementById('search-input').value;
    const sort = document.getElementById('sort-select').value;
    const url = `/showcase?query=${query}&sort=${sort}`;
    window.location.href = url;
}

// Function to handle sorting
function sortItems() {
    const query = document.getElementById('search-input').value;
    const sort = document.getElementById('sort-select').value;
    const url = `/showcase?query=${query}&sort=${sort}`;
    window.location.href = url;
}

// Function to handle product link clicks and redirect based on login status
function handleProductClick(event) {
    event.preventDefault();
    const url = this.getAttribute('data-url');

    fetch('/auth/is_logged_in')
        .then(response => response.json())
        .then(data => {
            if (data.logged_in) {
                window.location.href = url;
            } else {
                window.location.href = `/auth/login?next=${encodeURIComponent(url)}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

// DOMContentLoaded event listener to initialize event handlers
document.addEventListener('DOMContentLoaded', function() {
    // Search and sort event handlers
    const searchButton = document.querySelector('.btn-primary');
    if (searchButton) {
        searchButton.addEventListener('click', searchItems);
    }

    const sortSelect = document.getElementById('sort-select');
    if (sortSelect) {
        sortSelect.addEventListener('change', sortItems);
    }

    // Product link click event handlers
    const productLinks = document.querySelectorAll('.product-link');
    productLinks.forEach(link => {
        link.addEventListener('click', handleProductClick);
    });
});
