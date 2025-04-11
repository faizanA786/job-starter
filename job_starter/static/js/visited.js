function visited(event) {
    link = event.target
    link.style.textDecoration = "line-through";
    link.style.color = "gray";

}

window.onload = function() {
    setTimeout(function() {

    }, 3000);  // Waits for 5 seconds
};

let jobLinks = document.querySelectorAll(".job-link")
jobLinks.forEach(function(link) {
    link.addEventListener("click", visited);
})
