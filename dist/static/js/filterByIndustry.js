function isChecked(event) {
    let div = document.getElementById(`${event.target.id}-div`);

    if (event.target.checked) {
        div.style.display = "block";
        console.log("display " + event.target.id)
    }
    else {
        div.style.display = "none";
        console.log("hide " + event.target.id)
    }
}

document.getElementById("retail").addEventListener("click", isChecked);
document.getElementById("logistics").addEventListener("click", isChecked);
document.getElementById("hospitality").addEventListener("click", isChecked);