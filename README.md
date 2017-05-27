# Logs Analysis

> Dustin D'Avignon

## About

This is the third project for the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project mimics building an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

## To Run

You will need to have PostgreSQL setup to run this project as you will need to load the site's data into your database.

To load the data, use the command `psql -d news -f newsdata.sql` to connect a database and run the necessary SQL statements.

To execute the program, run `python3 newsdata.py` from the command line.