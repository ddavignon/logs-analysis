#!/usr/bin/env python3
import psycopg2


DBNAME = "news"


def most_popular_articles():
    """Return 'What are the most popular three articles of all time?' """
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        "select articles.title, count(*) as views "
        "from articles inner join log on log.path "
        "like concat('%', articles.slug, '%') "
        "where log.status like '%200%' group by "
        "articles.title, log.path order by views desc limit 3")
    return cursor.fetchall()
    db.close()


def most_popular_authors():
    """Return 'Who are the most popular article authors of all time?' """
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        "select authors.name, count(*) as views from articles inner "
        "join authors on articles.author = authors.id inner join log "
        "on log.path like concat('%', articles.slug, '%') where "
        "log.status like '%200%' group "
        "by authors.name order by views desc")
    return cursor.fetchall()
    db.close()


def load_errors():
    """Return 'On which days did more than 1% of requests lead to errors?' """
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(
        "select day, perc from ("
        "select day, round((sum(requests)/(select count(*) from log where "
        "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
        "perc from (select substring(cast(log.time as text), 0, 11) as day, "
        "count(*) as requests from log where status like '%404%' group by day)"
        "as log_percentage group by day order by perc desc) as final_query "
        "where perc >= 1")
    return cursor.fetchall()
    db.close()

print ("What are the most popular three articles of all time?")
for index, each_article in enumerate(most_popular_articles()):
    print (
        index+1, "-", each_article[0],
        "\t - ", str(each_article[1]), "views")

print ("Who are the most popular article authors of all time?")
for index, each_author in enumerate(most_popular_authors()):
    print (index+1, "-", each_author[0], "\t\t - ", each_author[1], "views")

print ("On which days did more than 1% of requests lead to errors?")
for each_day in load_errors():
    print (each_day[0], "-", str(each_day[1]) + "% errors")
