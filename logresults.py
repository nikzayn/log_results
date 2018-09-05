#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importing the postegre library
import psycopg2

#Connect the database to news
DBNAME = 'news'

# Define the postgre query which connects, pass and returns
def start_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""
    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    logs = c.fetchall()
    db.close()
    return logs

#1. Query for - "Top 3 articles of all time"
first_query = """
        SELECT title, COUNT(*) AS num
        FROM articles,log
        WHERE log.path = CONCAT('/article/', articles.slug)
        GROUP by articles.title
        ORDER by num DESC
        LIMIT 3;
    """

#2. Query for - "Top 3 most popular authors of all time"
second_query = """
        SELECT authors.name, COUNT(*) AS num
        FROM authors JOIN articles
        ON authors.id = articles.author
        JOIN log ON log.path = CONCAT('/article/', articles.slug)
        GROUP by authors.name
        ORDER by num DESC
        LIMIT 3;
    """

#3. Query for - "Days on which % of error are more"
third_query = """
        SELECT * FROM(SELECT date(time),
        round(100.0*sum(case log.status
        when '200 OK' then 0 else 1 end)/
        COUNT(log.status),3)
        AS error FROM log
        GROUP by date(time)
        ORDER by error DESC) as subq
        WHERE error > 1; 
    """

#4. Define the first query for finding out the top 3 articles. 
def print_first_query_results(query):
    output = start_query(query)
    print('\n1. What are the most popular three articles of all time?\n')
    for fetch in output:
        """Output of the results from the database of the string of articles"""
        print ('\t' + str(fetch[0]) + ' - ' + str(fetch[1]) + ' views')

#5. Define the second query for finding out the top 3 authors of all time.
def print_second_query_results(query):
    output = start_query(query)
    print('\n2. Who are the most popular article authors of all time?\n')
    for fetch in output:
        """Output of the results from the database of the string of authors"""
        print ('\t' + str(fetch[0]) + ' - ' + str(fetch[1]) + ' views')

#6. Define the third query for finding out days in which error leads.
def print_third_query_results(query):
    output = start_query(query)
    print('\n3. On which days did more than 1% of requests lead to errors?\n')
    for fetch in output:
        """Output of the results from the database of the string of errors"""
        print ('\t' + str(fetch[0]) + ' - ' + str(fetch[1]) + ' %')

#7. Print out the results from the defined queries:
if __name__ == '__main__':
    print('Fetching Results from the Database...')
    print_first_query_results(first_query)
    print_second_query_results(second_query)
    print_third_query_results(third_query)
