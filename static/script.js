document.addEventListener("DOMContentLoaded", function () {
    const toggle = document.getElementById("dark-mode-toggle");

    // Load the saved theme from localStorage
    const darkModeEnabled = localStorage.getItem("dark-mode") === "enabled";
    if (darkModeEnabled) {
        document.body.classList.add("dark-mode");
        toggle.checked = true;
    }

    // Toggle dark mode
    toggle.addEventListener("change", function () {
        if (toggle.checked) {
            document.body.classList.add("dark-mode");
            localStorage.setItem("dark-mode", "enabled");
        } else {
            document.body.classList.remove("dark-mode");
            localStorage.setItem("dark-mode", "disabled");
        }
    });
});