function isChecked(event) {
    let unspecifiedJobs = document.querySelectorAll(".job-container.None");
    let fullTimeJobs = document.querySelectorAll(".job-container.full_time");
    let partTimeJobs = document.querySelectorAll(".job-container.part_time");

    if (event.target.id == "unspecified" && event.target.checked) {
        unspecifiedJobs.forEach(function(container) {
            container.style.display = "block";
        })
    }
    else if (event.target.id == "full_time" && event.target.checked) {
        fullTimeJobs.forEach(function(container) {
            container.style.display = "block";
        })
    }
    else if (event.target.id == "part_time" && event.target.checked) {
        partTimeJobs.forEach(function(container) {
            container.style.display = "block";
        })
    }
    else if(event.target.id == "unspecified" && !event.target.checked) {
        unspecifiedJobs.forEach(function(container) {
            container.style.display = "none";
        })
    }
    else if(event.target.id == "full_time" && !event.target.checked) {
        fullTimeJobs.forEach(function(container) {
            container.style.display = "none";
        })
    }
    else if(event.target.id == "part_time" && !event.target.checked) {
        partTimeJobs.forEach(function(container) {
            container.style.display = "none";
        })
    }
}

document.getElementById("full_time").addEventListener("click", isChecked);
document.getElementById("part_time").addEventListener("click", isChecked);
document.getElementById("unspecified").addEventListener("click", isChecked);
