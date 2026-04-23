const version = "0.1.1";
console.log(`Roffl Version: ${version}`);

// Dropdown-Menü für den Benutzernamen
document.addEventListener("DOMContentLoaded", () => {
    const userBtn = document.getElementById("user_dropdown");
    const menu = document.getElementById("dropdown_menu");

    if (userBtn) {
        userBtn.addEventListener("click", (event) => {
            event.preventDefault(); // verhindert Springen nach oben
            menu.classList.toggle("show");

        });
    }

    // Klick außerhalb schließt das Menü
    document.addEventListener("click", (event) => {
        if (menu && !menu.contains(event.target) && event.target !== userBtn) {
            menu.classList.remove("show");
        }
    });
});

//SSE
const place = document.querySelector(".feed-container")
const source = new EventSource('/stream')
function onMessage(event) {
    console.log(event.data);
    d = JSON.parse(event.data)
    for (const entry of d){
        const imgs = entry.Image.map(url => `<img class="feed-image" src="${url}">`).join("");
        const html = `<div class="feed-item">
            <h3>${entry.Titel}</h3>
            <p>${entry.Text}</p>
            ${imgs}
        </div>`
        place.insertAdjacentHTML("afterbegin", html)
    }
}

source.onopen = function() {
    place.innerHTML = "";
}

source.onmessage = onMessage;


{/* <div class="feed-item">
            <h3>{{ entry.title }}</h3>
            <p>{{ entry.text }}</p>

            <!-- Bilder anzeigen -->
            {% for image in entry.images %}
                <img src="/image/{{ image.id }}" class="feed-image">
            {% endfor %}

            <small>Erstellt am: {{ entry.created_at }}</small>
            <small>Von: {{ entry.owner_user.username }} </small>

        </div> */}







