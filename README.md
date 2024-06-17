The intention was to create a tool which can analyse historic data (wins vs odds) from various sports to find the most efficient sport i.e. the sport in which the favourite wins most often.

Given that we're working with historic data which doesn't change, I first wanted to download the data from the API so I didn't need to continue call it; this is just to save paying the ongoing fee.

Since embarking on this project it's come to light that the API provider only holds historic odds for 7 days, therefore I pivoted.

Leaving the historic data download portion of the project now dormant but functioning, I wrote the code to regularly download completed games & odds. This data can then be analysed for trends.
