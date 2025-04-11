# 11/04/2025
- I might change how i store job ads, rather than storing it in a json file I might just use a local sqlite database since I used it before for my blackjack project (And to improve my profiecency)
- Even though im not collecting data, im going to add a privacy policy for good measure
- Also a TOS soon
- Right now i just styled the website even further
- Also made it so by default, entering the site displays all the jobs in all industries

# 10/04/2025
- I was testing the webpage and i realised that job links that had land/ad instead of details would redirect to page not found
- I was comparing links properly, like before trimming it and after trimming, it works when it wasnt trimmed
- I trimmed it because it was using my API ID, and since its my first time using APIs, i was cautious about using it in the link
- I researched online and apparently its not dangerous, its the API key thats critical, which I made sure to include in my gitgnore file before pushing it to the repo
- I went ahead and looked up job board design and i found one i liked in particular, its nice and slick
- Filters on the left, job ads on the right
- Im also going to try and make it so that the date would say 'Today/One day ago' etc rather than giving the actual date out for better user experience
- I've changed the job location to only east as well since jobs not in east are like hours away from me
- Ive started to design the webpage now using CSS

# 09/04/2025
- Theres a bit of a problem, i read on their page that adzuna api limits requests to only 250 a day, i can easily hit the rate limit from the way im fetching job ads
- i researched techniques to deal with this and i came across a technique
- you fetch the job data once a day, store it in a json file and then serve it through flask
- i can use json to read/write from the file once its been created
- since i plan to deploy this app using railway as my host, i can use something called cronjob that allows for schedules
- il deal with that later
- Im also going to change the way i fetch jobs, instead of placing it in a list of lists (which is confusing to read) ill use a hashmap (or dict in python) and place that inside the job lists
- meaning i dont have to use jobs[0] to grab the title for instance, instead i can use the key directly job["title"] 
- makes it easier to understand and follow

# 08/04/2025
- Its getting tedious to go on numerous job boards seperatly to find my first job to get experience, its worse when their sort by functions dont work, or id search for retail assistant positions in london but then it shows me delivery driver positions outside of london
- So im making a web app thats gonna try to solve these issues, which could also be beneficial for other students like me
- Im targetting entry level jobs specifically because I have no experience myself, and targetting those in London (since I am in london)
- Jobs in retail and hospitality will be prioritised because they have almost no barrier to entry
- Only jobs not older than 3 days will be posted because you'd typically have a higher chance to hear back
- So far Ive added the basics of fetching job data via aduzna api, i used it because its free
- I need to style the page using css later because right now its an eyesore to read job posts on the page
- I also need to allow to categorise jobs by industry, and add a sort by function later