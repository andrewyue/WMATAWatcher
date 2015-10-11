# WMATA Watcher
A study of tweets and their correlation to delays in public transportation.

In recent quarters, service issues on Washington DC's MetroRail have been on the uptick:

<img src="https://github.com/andrewyue/WMATAWatcher/blob/master/Fig1.jpg">

This project was motivated by a discovery I found in searching through the combination of <a href="https://twitter.com/search?q=%40wmata%20OR%20%23wmata%20OR%20%40unsuckdcmetro%20OR%20%23unsuckdcmetro%20OR%20%40fixwmata%20OR%20%40dcmetrosucks%20OR%20%40metrorage%20OR%20%40overhaulmetro%20OR%20%23metrorailinfo%20OR%20%40metrorailinfo%20OR%20%23metrofailinfo%20OR%20%40metrofailinfo%20OR%20%40drgridlock">Tweets</a>, the <a href="http://www.wmata.com/rail/service_reports/viewReportArchive.cfm">Metro Daily Service Archives</a>, and Official Alerts from <a href="https://twitter.com/MetroRailInfo">@MetroRailInfo</a>.  The data is plotted in Fig. 2.  In just one week's worth of data, I discovered that MetroRailInfo failed to provide any notice (in blue) to riders about delays during two afternoon rush hours.  These delays were later acknowledged by Metro (in red).  In that same timeframe, Tweet activity (in black) spiked, suggesting that there may be valuable information contained within.

<img src="https://github.com/andrewyue/WMATAWatcher/blob/master/Fig2.jpg">

From here, I gathered several months of Tweets and scraped the Service Archive.  This allowed me to construct a training set:

<img src="https://github.com/andrewyue/WMATAWatcher/blob/master/WMATAWatcher.png">

As shown in the sketchnote, a "bag of words" approach was used to construct features initially.  Word content of the tweets (both 1 and 2-grams) were vectorized and normalized by term-frequency inverse document-frequency.  Classification by Random Forest and SVM both sacrificed far too much absolute accuracy to boost the precision (predicting a delay in each time bin), and so were not useful for deployment to an app.

A more coarse-grain model was built to categorize Tweets based on their word content:
<ol>
<li>Delay-related Tweets - containing words such as "delay" or "offloading"</li>
<li>Line-related Tweets - containing specific mention of the line colors of Metro</li>
<li>Service OK-related Tweets - containing specific mention of words related to service resuming</li>
</ol>

Additional features used were the Tweet volume, Tweet day of week, hour of day, month, and week of the year.  A recall of 0.5 is achieved using a Random Forest.
