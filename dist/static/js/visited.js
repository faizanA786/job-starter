function visited(event) {
    link = event.target;
    if (link.id == "job-link") {
        link.style.textDecoration = "line-through";
        link.style.color = "gray";
    }
    else if(link.id == "map-link") {
        link.style.color = "gray";
    }
}

let jobLinks = document.querySelectorAll(".job-link");
let mapLinks = document.querySelectorAll(".map-link");
jobLinks.forEach(function(link) {
    link.addEventListener("click", visited);
})
mapLinks.forEach(function(link) {
    link.addEventListener("click", visited);
})