# Log Analysis

This is a project from the **Fullstack Web Developer Nanodegree** from [Udacity](https://udacity.com/course/full-stack-web-developer-nanodegree--nd004).

It's a Python program that performs a log analysis, although it has a shebang line for running it using Python 3, this program was tested and works with Python versions: 2.7.12 and 3.5.2.

## Files

  * log_analysis.py

#### log_analysis.py
This file contains all the Python code and SQL queries needed to analyze the log data.

## Instructions

In order to build the lab environment you must install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).

#### VirtualBox
Execute `sudo apt install virtualbox` if you use a Linux distribution like Ubuntu.

#### Vagrant
Execute `sudo apt install vagrant` if you use a Linux distribution like Ubuntu.

#### Setting Up The Lab Environment
1. You can perform a git clone by typing `git clone https://github.com/udacity/fullstack-nanodegree-vm` or simply [download](https://github.com/udacity/fullstack-nanodegree-vm/archive/master.zip) it to your computer.

2. After cloning or downloading<em>(remember to extract it by `unzip master.zip`)</em>, access a folder called Vagrant and run `vagrant up`, you should see the virtual machine being prepared.

3. Now you can access it by running `vagrant ssh`.

4. Download the database content by typing `wget https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip`.

5. Extract the downloaded file by using unzip: `unzip newsdata.zip`. You should now have a file named `newsdata.sql`.

6. Import the data into the PostgreSQL database: `psql -d news -f newsdata.sql`

7. In order to execute the program there are few modules that must be present, install them by typing: `pip install psycopg2` and `pip install tabulate`, or if you are using Python 3, install them using: `pip3 install psycopg2` and `pip3 install tabulate`.

#### Running the program

Finally the best part, all you have to do now is run `python log_analysis.py` our `python3 log_analysis.py` depending the Python version you have, if you wish to run it direcly make sure the file has  the proper persmission to be executed, wish can be granted by `chmod +x log_analysis.py` and you can run int by simply typing `./log_analysis.py` as long as you have Python 3 installed in the following location: `/usr/bin/python3`

**Here is my output example:**
```
1. What are the most popular three articles of all time?

+----------------------------------+---------+
| Articles                         |   Views |
|----------------------------------+---------|
| Candidate is jerk, alleges rival |  338647 |
| Bears love berries, alleges bear |  253801 |
| Bad things gone, say good people |  170098 |
+----------------------------------+---------+



2. Who are the most popular article authors of all time?

+------------------------+---------+
| Authors                |   Views |
|------------------------+---------|
| Ursula La Multa        |  507594 |
| Rudolf von Treppenwitz |  423457 |
| Anonymous Contributor  |  170098 |
| Markoff Chaney         |   84557 |
+------------------------+---------+



3. On which days did more than 1% of requests lead to errors?

+------------+-----------+
| Days       | Percent   |
|------------+-----------|
| 2016-07-17 | 2.26%     |
+------------+-----------+

```
