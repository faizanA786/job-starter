# 14/04/2025
- Jusst going to now polish everything up before pushing to master
- So things like adding mobile support for the website
- And then ill deploy using Netlify
- The plan is to use github actions to automate the job fetching once a day by running the prefetch scripts
- And then netlify will rebuild the site with the new information
- Or i might use github pages, because of netlifys limited build minutes
- I added a new header to the website to hold nav links instead of throwing it inside the left column

# 13/04/2025
- Just for the record, all the fonts/images I used for the website holds a creative commons license (So not copyrighted), and the wallpaper for the website i generated using an AI image generator.
- What i want to do eventually is make it so that jobs are sorted depending on the context
- This means if full time filter is on, show full time jobs FIRST before showing anything else
- But today ill work on changing the date posted part, where instead of diplaying the literal date, ill instead show either 'today' if posted today, or 'yesterday' if posted yesterday etc
- Saying this, i should probably take a course on UX somewhere down the line
- I should also make use of HTML semantic tag elements like section instead of constantly using divs because its a bit lazy
- I also filled out the privacy policy and TOS using template(s) I found online and then just modifiyng it

# 12/04/2025
- For the filters, Im use checkboxes, where they will have event listners that will hide industry sections based of whether their checked or not using a combination of css style hidden and js
- I had to use display instead of visibility because simply hiding it doesnt actually take it out the html, it still taking up space but would just be invisible
- I just spent the last hour trying to figure out why my filter by contract time script wasnt working - id check fulltime checkbox, but then it would display part time jobs and hide full time?? I just realised its because the p tag within the html element was flipped
- If contract time was full, set p to part time and vice versa
- Silly mistake, but i know now to be more vigilant
- I used google maps URL scheme to now approximate distances between homes and work sites
- Ive also decided to move away from using railway as a host, id rather make this a static site otherwise id need a server to hold the backend, and no free alternative host to do that
- I can use netlify if I make it static instead
- So i made a new distrbution folder to hold the results of the creation of the html
- I also started to think about how i could use colours in the fonts to enhance UX

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