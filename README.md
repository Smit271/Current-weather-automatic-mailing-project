# Current-weather-automatic-mailing-project
### This project contains uses of python3, API of openweather.org and some libraries of python3.

- First you need to install all libraries that are not in built using pip3 or pip command. ##like pip3 install <library/module name>
- then download all files in repository in one folder and make changes indicated in code.
- finally run it using any  IDE or python console.
### For automation of sending emails or running script i used crontab in linux or Task Scheduler in windows..
####For linux how to use crontab
- for details visit : https://opensource.com/article/17/11/how-use-cron-linux
- how i used :
-     crontab -e (run in terminal)
-     opened vi editor
-     add following command
-     15 10 * * * /PathToPython.exe /PathOfYourScript >> /PathOfTxtFileInWhichOutputWillbeSaved
