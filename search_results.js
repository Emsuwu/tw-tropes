const urlParams = new URLSearchParams(window.location.search)
const query = urlParams.get("query")

function performFuzzySearch(searchTerm){

}

function createResultElement(data){
    const titleID = data["id"]
    const titleEn = data["title_en"]
    const thumbnail = data["thumbnail"]
    const shortSynopsis = "This is a synopsis"
    const template = `
    <div class="search-page-result">
        <div>
            <a href="media.html?title=${titleID}"><img src="Images/Thumbnails/${thumbnail}"></a>
        </div>
        <div>
            <p>
                <a href="media.html?title=${titleID}">${titleEn}</a>
                <br>
                ${shortSynopsis}
            </p>
        </div>
    </div>
    `
    return template;
}

function readAndSetResults(searchID) { 
    const csvURL = 'https://raw.githubusercontent.com/Emsuwu/tw-tropes/refs/heads/main/Data/tw_database.csv'
    const csvPath = 'Data/tw_database.csv'

    console.log(`Loading contents of ${searchID}`)

    if (typeof Papa === 'undefined') {
        console.error("PapaParse library not found. Retrying in 500ms...")
        setTimeout(readAndSetResults, 500)
        return
    }

    Papa.parse(csvURL, {
        download: true,
        header: true,
        skipEmptyLines: true, 
        complete: function(results) {
            const searchResultsElement = document.getElementById("results")

            const data = results.data; // the whole ass table
            const match = data.find(row => row.id === searchID); // search in row "id" for searchID

            let resultsCount = 0

            if (match) {
                // Exact ID matches should come first
                console.log("Match found")
                searchResultsElement.innerHTML += createResultElement(match);
                resultsCount++
            } 
            
            /* 
            
            TODO: Perform fuzzy search based on all entries' 
            id, title_en, title_jp, title_romaji

            Rank in terms of accuracy

            Then perform fuzzy search based on all entries'
            trigger_warnings, negative_representations

            Count results with resultsCount

            If resultsCount === 0 at the end, run
            searchResultsElement.innerHTML += "<h4>No results :(</h4>";
            
            */

            if (resultsCount == 0) searchResultsElement.innerHTML += "<h4>No results :(</h4>";
            
        }
    });
}

readAndSetResults(query)