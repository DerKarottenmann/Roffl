const version = "0.1.0";
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


