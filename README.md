# etl-demo
Airflow - Data pipeline

This project is to perform basic analytics with the customers and orders tables. Orders table is in MySQL DB and Customers table is in PostgreSQL.

Setup the environment to build a data pipeline. Refer https://github.com/harithavytla/retail-data-pipeline-ETL

**SetUp Airflow**

1. Create directory by name airflow  ``` mkdir airflow ```. Get into the directory  ``` cd airflow ```
2. Here is the command to create virtual environment - ``` python -m venv airflow-env ```
3. Activate the virtual environment  ``` source airflow-env/bin/activate ```
4. Install AirFlow - ``` pip install apache-airflow ```
5. Run  ``` airflow initdb ``` to intialize the database and add configuration files. All the databases and configuration files will be created in our working directory airflow.

By default it uses sqlite database.

6. Run following commands to start airflow webserver and scheduler.

```airflow webserver -p 8080 -D```

```airflow scheduler -D```

7. Access Web UI http://ipaddress:8080

***Using MySQL***

In Non Development environments we have to setup AirFlow using traditional RDBMS Databases. 

1. Make sure to stop all the airflow processes.
```
cat airflow-scheduler.pid | xargs kill
cat airflow-webserver.pid|xargs kill
ps -ef|grep airflow
```

2. Install mysql-connector-python so that we can use MySQL Database - ``` pip install mysql-connector-python ```

``` 
docker run \
    --name mysql_airflow \
    -e MYSQL_ROOT_PASSWORD=''\
    -d \
    -p 4306:3306 \
    mysql
```
3. Connect to MySQL and create database as well as username for airflow database -``` docker exec -it mysql_airflow mysql -u root -p ```
``` 
CREATE DATABASE airflow;
CREATE USER airflow IDENTIFIED BY '';
GRANT ALL ON airflow.* TO airflow;
FLUSH PRIVILEGES; 
```
4. Set executor to LocalExecutor.

We can also use other Executors.
5. Update sql_alchemy_conn with MySQL URL.
``` 
sql_alchemy_conn = mysql+mysqlconnector://airflow:<password>y@localhost:4306/airflow?use_pure=True
```
6. Make sure some of the properties related to concurrency is adjusted to lower numbers.
``` 
parallelism = 8
dag_concurrency = 4
max_active_runs_per_dag = 4
workers = 4
worker_concurrency = 4
worker_autoscale = 4,2 
```
7. Run ``` airflow initdb ``` to initialize MySQL Database.
8. Start webserver and scheduler in the background.
