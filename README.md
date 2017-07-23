Console Script
---------------
This is a script, in Python, that uses Jenkins' API to get a list of jobs and their status from a given jenkins instance. The status for each job should is stored in an sqlite database along with the time for when it was checked.

The Script is found in the jenkins_script.py file

Note: before jenkins api can work on this server you have to install jenkins installer, configure it to run as a service then create jobs, build the jobs.

Full App
-----------------
This is Django App, that adds a name / email address to the sqlite database. And also should validate input and show errors.

The App is found in the jenkens_job Directory



-----------------------------------------------------------------------------------------------------

Made by: Sintayehu Abaynhe(sinteco)