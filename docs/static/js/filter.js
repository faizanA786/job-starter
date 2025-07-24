function triggerAnimation() {
    let element = document.getElementById("fadeDown");

    element.classList.remove("fade-down");
    void element.offsetWidth; 
    element.classList.add("fade-down");
}

function isCheckedType(event) { // JOB TYPE
    triggerAnimation();
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

function isCheckedIndustry(event) { // INDUSTRY 
    triggerAnimation();
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

function matchTitle(event) {
    let jobContainers = document.querySelectorAll(".job-container");
    let searchInput = event.target.value.trim().toLowerCase();

    if (searchInput === "") {
        //show all jobs if input is empty
        jobContainers.forEach(container => {
            container.style.display = "block";
        });
        return;  
    }

    triggerAnimation();

    jobContainers.forEach(container => {
        const jobTitle = container.querySelector("#job-title b").textContent.toLowerCase();
        const match = searchInput.split(" ").some(word => jobTitle.includes(word));
        container.style.display = match ? "block" : "none";
    });
}

document.getElementById("searchEntry").addEventListener("input", matchTitle);

document.getElementById("retail").addEventListener("click", isCheckedIndustry);
document.getElementById("logistics").addEventListener("click", isCheckedIndustry);
document.getElementById("hospitality").addEventListener("click", isCheckedIndustry);

document.getElementById("full_time").addEventListener("click", isCheckedType);
document.getElementById("part_time").addEventListener("click", isCheckedType);
document.getElementById("unspecified").addEventListener("click", isCheckedType);
