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

function matchTitle(event) { // SEARCH
    let jobContainers = document.querySelectorAll(".job-container");
    let entry = document.getElementById("searchEntry").value;

    if (event.key == "Enter") {
        triggerAnimation();

        if (entry.trim() == "") {
            console.log("Returning default job list");

            jobContainers.forEach(function(container) {
                container.style.display = "block";
            });
        }
        else {
            entry = entry.trim().split(" ");

            jobContainers.forEach(function(container) {
                container.style.display = "none";

                let job = container.querySelector("#job-title");
                let title = job.querySelector("b").textContent;
                let keywords = title.split(" ");

                for (let i=0; i<entry.length; i++) { // N^2 time complexity, improve this later!
                    let hide = false;
                    for (let j=0; j<keywords.length; j++) {
                        if (keywords[j].toLowerCase() == entry[i].toLowerCase()) {
                            container.style.display = "block";
                            hide = true;
                            break;  
                        }
                        if (hide) {
                            break;
                        }
                    }
                }
            });
        }
    }
}

document.getElementById("searchEntry").addEventListener("keydown", matchTitle)

document.getElementById("retail").addEventListener("click", isCheckedIndustry);
document.getElementById("logistics").addEventListener("click", isCheckedIndustry);
document.getElementById("hospitality").addEventListener("click", isCheckedIndustry);

document.getElementById("full_time").addEventListener("click", isCheckedType);
document.getElementById("part_time").addEventListener("click", isCheckedType);
document.getElementById("unspecified").addEventListener("click", isCheckedType);
