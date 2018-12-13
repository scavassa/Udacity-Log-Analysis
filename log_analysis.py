#!/usr/bin/python3

import psycopg2
from tabulate import tabulate

DBNAME = "news"
connection = psycopg2.connect(database=DBNAME)
cursor = connection.cursor()

# The first query that fetches the 3 most popular articles
print("\n\n\n1. What are the most popular three articles of all time?\n")
sql = "SELECT articles.title, count(articles.title) AS views \
        FROM articles, log \
        WHERE log.path = concat('/article/',articles.slug) \
        AND log.method='GET' \
        AND log.status \
        LIKE '%200%' \
        GROUP BY articles.title \
        ORDER BY views DESC LIMIT 3;"
cursor.execute(sql)
print(tabulate(cursor.fetchall(), headers=['Articles', 'Views'],
               tablefmt='psql'))

# The second query that fetches the 3 most popular authors
print("\n\n\n2. Who are the most popular article authors of all time?\n")
sql = "SELECT authors.name, count(articles.author) AS views \
        FROM articles, log, authors \
        WHERE log.path = '/article/' || articles.slug \
        AND authors.id = articles.author \
        AND log.method='GET' \
        AND log.status \
        LIKE '%200%' \
        GROUP BY authors.name \
        ORDER BY views DESC;"
cursor.execute(sql)
print(tabulate(cursor.fetchall(), headers=['Authors', 'Views'],
               tablefmt='psql'))

# The third query that tells wich days had more than 1% error requests
print("\n\n\n3. On which days did more than 1% of requests lead to errors?\n")
sql = "WITH \
        requests AS (SELECT date(log.time) AS day, count(date(log.time)) \
        FROM log \
        GROUP BY date(log.time) \
        ORDER BY date(log.time)), \
        errors AS (SELECT date(log.time) AS day, count(date(log.time)) \
        FROM log WHERE status NOT LIKE '%200%' \
        GROUP BY date(log.time) \
        ORDER BY date(log.time)), \
        error_rate AS (SELECT requests.day, \
        cast(errors.count AS float) / cast(requests.count AS float) * 100 \
        AS percent \
        FROM requests, errors \
        WHERE requests.day = errors.day) \
        SELECT error_rate.day, \
        round(cast(error_rate.percent AS decimal), 2) || '%' \
        FROM error_rate \
        WHERE percent > 1"
cursor.execute(sql)
print(tabulate(cursor.fetchall(), headers=['Days', 'Percent'],
               tablefmt='psql'))

connection.close()
