# Log Analysis Project
Udacity's Nanodegree Last Project
## Project Description:
Your task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
### Questions to Answer:
1. **What are the most popular three articles of all time?** Which articles have been 
accessed the most? Present this information as a sorted list with the most popular 
article at the top.
1. **Who are the most popular article authors of all time?** That is, when you sum up 
all of the articles each author has written, which authors get the most page views? 
Present this as a sorted list with the most popular author at the top.
1. **On which days did more than 1% of requests lead to errors?**  The log table 
includes a column status that indicates the HTTP status code that the news site sent 
to the user's browser. 

## Project Setup:
This project is running in a virutal machine created using Vagrant so there are a few steps to get set up:
#### Installing the dependencies and setting up the files:
1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
These files configure the virtual machine and install all the tools needed to run this project.
1. Download the database setup: [data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
1. Unzip the data to get the newsdata.sql file.
1. Put the newsdata.sql file into the vagrant directory
1. Download this project: [log results](https://github.com/nikzayn/log_results)
1. Upzip as needed and copy all files into the vagrant directory into a folder called log_analysis
#### How to run the program in virtual machine:
1. Open Terminal and navigate to the project folders we setup above.
1. cd into the vagrant directory
1. Run ``` vagrant up ``` to build the VM for the first time.
1. Once it is built, run ``` vagrant ssh ``` to connect.
1. cd into the correct project directory: ``` cd /vagrant/log_results ```
#### Load the data into the database:
1. Load the data using the following command: ``` psql -d news -f newsdata.sql ```


## Run The Project Already!
1. You should already have vagrant up and be connected to it. 
1. If you aren't already, cd into the correct project directory: ``` cd /vagrant/log_results ```
1. Run ``` python logresults.py ```

Loading will take some time!!! 

## Expected Output: 
vagrant@vagrant:/vagrant/forum$ python logresults.py
Fetching Results from the Database...


1. What are the most popular three articles of all time?

        Candidate is jerk, alleges rival - 338647 views
        Bears love berries, alleges bear - 253801 views
        Bad things gone, say good people - 170098 views

2. Who are the most popular article authors of all time?

        Ursula La Multa - 507594 views
        Rudolf von Treppenwitz - 423457 views
        Anonymous Contributor - 170098 views

3. On which days did more than 1% of requests lead to errors?

        2016-07-17 - 2.000 %

