# omegaapplication

Omega application technical document :
-----------------------------------------------------

Step1 : Installed the django and environment
Step2 : created the environment and activated and Created the new project and new app using below commands
    django-admin startproject omeageapplication
    python manage.py startapp omega
Step3 :Installed the all requirements and installed the newspaper library from pip install newspaper3k
Step4 : using the url = 'https://news.google.com/news/rss' extracted the data.Getting the below response fields.
title,
link,
published date,
description and source.
Step5 :
	Stored the all above response data into one dictionary and using loop took the link and passed to the newspaper library and got the description.and again i have updated the dictionary.
i have to pass the description to the summary API and get the summary description.After  I need to store all this info in elastic search.
Step6 : Created the croptab for global news and it will run every 60min.
Currently working for local news extraction.
Step 7 :  After completion of the above work, i will store all the response data in elastic search.



From this Apllciation we are able get the global,india,usa,singapore,uk,uae news as the json data
