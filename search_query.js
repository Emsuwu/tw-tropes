function makeQuery(){
    const searchBar = document.getElementById("search_bar");
    if (searchBar.value === "") return

    const query = document.getElementById('search_bar').value
    console.log("Making query for " + query)
    window.location = `search.html?query=${query}`;
}

window.onload = function () {
    const searchButton = document.getElementById("search_button")
    searchButton.addEventListener("click", makeQuery);
    
    const searchBar = document.getElementById("search_bar");
    searchBar.addEventListener("keyup", function(event) {
        if (event.key === "Enter") {
            makeQuery()
        }
    });
};

