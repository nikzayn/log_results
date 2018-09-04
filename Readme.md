Log Analysis Project
This is a project for Udacity's Full Stack Web Developer Nanodegree

Project Description:
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

Questions to Answer:
What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
Who are the most popular article authors of all time? That is, when you sum up all of the articles each author has written, which authors get the most page views? Present this as a sorted list with the most popular author at the top.
On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.
This Project Requires a Bit of Setup:
This project is run in a virutal machine created using Vagrant so there are a few steps to get set up:

Installing the dependencies and setting up the files:
Install Vagrant
Install VirtualBox
Download the vagrant setup files from Udacity's Github These files configure the virtual machine and install all the tools needed to run this project.
Download the database setup: data
Unzip the data to get the newsdata.sql file.
Put the newsdata.sql file into the vagrant directory
Download this project: log analysis
Upzip as needed and copy all files into the vagrant directory into a folder called log_result
Start the Virtual Machine:
Open Terminal and navigate to the project folders we setup above.
cd into the vagrant directory
Run vagrant up to build the VM for the first time.
Once it is built, run vagrant ssh to connect.
cd into the correct project directory: cd /vagrant/log_result
Load the data into the database:
Load the data using the following command: psql -d news -f newsdata.sql
Note: Checkout Udacity's FAQ page if you are running into any errors here.
Run The Project Already!
You should already have vagrant up and be connected to it.
If you aren't already, cd into the correct project directory: cd /vagrant/log_result
Run python logresults.py
Generating this information will take several seconds, but will now start loading.

Expected Output:
Calculating Results...
TOP THREE ARTICLES BY PAGE VIEWS:
    (1) "Candidate is jerk, alleges rival" with 338647 views
    (2) "Bears love berries, alleges bear" with 253801 views
    (3) "Bad things gone, say good people" with 170098 views
TOP THREE AUTHORS BY VIEWS:
    (1) Ursula La Multa with 507594 views
    (2) Rudolf von Treppenwitz with 423457 views
    (3) Anonymous Contributor with 170098 views
DAYS WITH MORE THAN 1% ERRORS:
    July 17, 2016 -- 2.3% errors
