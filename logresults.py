#!/usr/bin/python
# -*- coding: utf-8 -*-

#Importing the postegre library
import psycopg2


DBNAME = 'news'

# Define the postgre query which connects, pass and returns
def run_query(query):
    """Connects to the database, runs the query passed to it,
    and returns the results"""

    db = psycopg2.connect('dbname=' + DBNAME)
    c = db.cursor()
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows

#1. Define the top 3 articles
def fetch_top_articles():
    """Returns top 3 most read articles"""

    #1.1 Building the Query

    query = \
        """
        SELECT articles.title, COUNT(*) AS num
        FROM articles
        JOIN log
        ON log.path LIKE concat('/article/%', articles.slug)
        GROUP BY articles.title
        ORDER BY num DESC
        LIMIT 3;
    """

    #1.2 Running the Query

    result = run_query(query)

    #1.3 Display the Results

    print '\nTOP 3 ARTICLES:'
    count = 1
    for i in result:
        number = '(' + str(count) + ') "'
        title = i[0]
        views = '" with ' + str(i[1]) + ' views'
        print number + title + views
        count += 1

#2. Define the top 3 authors
def fetch_top_authors():
    """returns top 3 most popular authors"""

    #2.1 Building the Query

    query = \
        """
        SELECT authors.name, COUNT(*) AS num
        FROM authors
        JOIN articles
        ON authors.id = articles.author
        JOIN log
        ON log.path like concat('/article/%', articles.slug)
        GROUP BY authors.name
        ORDER BY num DESC
        LIMIT 3;
    """

    #2.2 Running Query

    result = run_query(query)

    #2.3 Display the Results

    print '\nTOP 3 AUTHORS:'
    count = 1
    for i in result:
        print '(' + str(count) + ') ' + i[0] + ' with ' + str(i[1]) \
            + ' views'
        count += 1

#3. Define the errors recieved through days
def fetch_day_errors():
    """returns days with more than 1.5% errors"""

    #3.1 Building the Query

    query = \
        """
        SELECT total.day,
          ROUND(((errors.error_requests*1.0) / total.requests), 3) AS percent
        FROM (
          SELECT date_trunc('day', time) "day", count(*) AS error_requests
          FROM log
          WHERE status LIKE '404%'
          GROUP BY day
        ) AS errors
        JOIN (
          SELECT date_trunc('day', time) "day", count(*) AS requests
          FROM log
          GROUP BY day
          ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.error_requests*1.0) / total.requests), 3) > 0.01)
        ORDER BY percent DESC;
    """

    #3.2 Running the Query

    result = run_query(query)

    #3.3 Display the Results

    print '\nDAYS WITH MORE THAN 1.5% ERRORS:'
    for i in result:
        date = i[0].strftime('%B %d, %Y')
        errors = str(round(i[1] * 100, 1)) + '%' + ' errors'
        print date + ' -- ' + errors


print 'Fetching Results...\n'
fetch_top_articles()
fetch_top_authors()
fetch_day_errors()
