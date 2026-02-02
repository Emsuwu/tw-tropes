const urlParams = new URLSearchParams(window.location.search)
const titleID = urlParams.get("title")


function readAndSetData(targetID) { 
    const csvURL = 'https://raw.githubusercontent.com/Emsuwu/tw-tropes/refs/heads/main/Data/260202-backup.csv'

    console.log(`Loading contents of ${targetID}`)
    Papa.parse("csvURL", {
        download: true,
        header: true,
        skipEmptyLines: true, 
        complete: function(results) {
            const data = results.data;
            console.log(`Data: ${data}`)
            const match = data.find(row => row.id === targetID);
            console.log(`Match: ${match}`)
            if (match) {
                let rating = 10
                let synopsis = 'Line 1 of synopsis! Some more.\nLine 2 of synopsis!\nEtc.'
                synopsis = '<p>' + synopsis.replaceAll('\n', '</p><p>') + '</p>'
                let provider_url = 'https://myanimelist.net/anime/226/Elfen_Lied'
                let provider_name = 'MyAnimeList'

                document.getElementById("title").textContent = match["title_en"];
                document.getElementById("medium").innerHTML = `<strong>Medium: </strong>${match["medium"]}<br>`
                document.getElementById("rating").innerHTML = `<strong>Rating: </strong>${10}<br>`
                document.getElementById("thumbnail").innerHTML = `<img src="Images/Thumbnails/${match["thumbnail"]}" class="media-description-thumbnail">`
                document.getElementById("synopsis").innerHTML = synopsis
                document.getElementById("synopsis_attribution").innerHTML = `Synopsis provided by <a href="${provider_url}" target="_blank">${provider_name}</a>.`
                
                console.log(match["trigger_warnings"])
                let formattedTWs = ''
                if (match["trigger_warnings"] != ""){
                    formattedTWs = '<li>' + match["trigger_warnings"].replaceAll(';;','</li><li>') + '</li>';
                }
                else{
                    formattedTWs = '';
                }
                
                document.getElementById("trigger_warnings").innerHTML = formattedTWs

                let nrs = match["negative_representations"].split(';;');
                let formattedNrs = []
                let und = false
                for (let nr of nrs) {
                    let split = nr.split(':')
                    formattedNrs.push(`<p><span class="text-content-subheading">${split[0]}</span><br>${split[1]}</p>`)
                    if (split[0] == undefined || split[1] == undefined){
                        und = true
                        break;
                    }
                }
                formattedNrs = formattedNrs.join('')
                if (!und) document.getElementById("negative_representations").innerHTML = formattedNrs
                else document.getElementById("negative_representations").innerHTML = ''

            } else {
                console.log("No match found for: " + targetID);
            }
        }
    });
}

readAndSetData(titleID)