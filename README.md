# WMATA Watcher
A study of tweets and their correlation to delays in public transportation.  In recent months, service issues on Washington DC's MetroRail have been on the uptick:

<img src="https://github.com/andrewyue/WMATAWatcher/blob/master/Fig1.jpg">

This project was motivated by a discovery I found in searching through the combination of <a href="https://twitter.com/search?q=%40wmata%20OR%20%23wmata%20OR%20%40unsuckdcmetro%20OR%20%23unsuckdcmetro%20OR%20%40fixwmata%20OR%20%40dcmetrosucks%20OR%20%40metrorage%20OR%20%40overhaulmetro%20OR%20%23metrorailinfo%20OR%20%40metrorailinfo%20OR%20%23metrofailinfo%20OR%20%40metrofailinfo%20OR%20%40drgridlock">Tweets</a>, the <a href="http://www.wmata.com/rail/service_reports/viewReportArchive.cfm">Metro Daily Service Archives</a>, and Official Alerts from <a href="https://twitter.com/MetroRailInfo">@MetroRailInfo</a>.

I discovered that, on two afternoon rush hours, MetroRailInfo failed to provide any notice to riders about delays that were later acknowledged by Metro.  In that same timeframe, Tweet activity spiked:

<img src="https://github.com/andrewyue/WMATAWatcher/blob/master/Fig2.jpg">

From here, I gathered several months of Tweets and scraped the Service Archive.  This allowed me to construct a training set:

<img src="https://github.com/andrewyue/WMATAWatcher/blob/master/WMATAWatcher.png">

The features used were the Tweet volume, Tweet day of week and hour of day, and the fraction of Tweets that could be classified into categories by their word content.

The estimator used was a class-weighted random forest.
