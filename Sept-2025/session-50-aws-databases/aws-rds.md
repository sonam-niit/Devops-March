# Create Instance Using AWS RDS

1. Login AWS Console
2. Search for RDS --> open RDS Dashboard
3. create database --> standard create --> Engine MYSQL --> Edition- mySQL Comm
4. Version --> 8.0.43 --> Template Go with Free tier
5. Settings --> Type Name of Database --> pw
6. credentials set username admin, set your own password don't include @
7. others keep with the default settings and create Database.
8. IN RDS database make sure the security group has the port open 3306

# Create Ubuntu instanse with default sg 22 port open

1. connect with the instance with SSH
2. install mysql-client
    sudo apt update && sudo apt install mysql-client -y
3. let's connect with RDS DB:
    mysql -h <enter_end_point_db> -u admin -p
4. enter your generated password
5. you will be connected with RDS from instance
6. you can execute some queries

    show databases;
    create database pw;
    select NOW();

7. check outputs.

# Connect Python App to RDS Database

## Python App Code 
```python
from flask import Flask
import pymysql

app= Flask(__name__)

db_host="<ENDPOINT_RDS>"
db_user="<master_user_name>"
db_pass="<Master_password>"
db_name="<DB_NAME>"

@app.route("/")
def home():
    try:
        conn= pymysql.connect(host=db_host,user=db_user,password=db_pass,
                              database=db_name)
        cursor=conn.cursor()
        cursor.execute("SELCT NOW()")
        result=cursor.fetchone()
        conn.close()
        return f"Connected to RDS! Current Time: {result}"
    except Exception as e:
        return f"Error: {e}"
    

if __name__=="__main__":
    app.run(host="0.0.0.0",port=80)
```

1. Save above file in app.py inside myapp folder
2. move to folder and setup dependencies
```bash
cd myapp
sudo apt install python3 python3-pip
sudo apt install python3.12-venv
```
3. Setup Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate
pip install flask pymysql
```
4. Run application
```bash
python3 app.py
```