function searchItems() {
    const query = document.getElementById('search-input').value;
    // 实现 AJAX 请求，更新商品列表
    console.log('Searching for:', query);
}

function sortItems() {
    const sortValue = document.getElementById('sort-select').value;
    // 实现 AJAX 请求，根据选择的排序选项更新商品列表
    console.log('Sorting by:', sortValue);
}
