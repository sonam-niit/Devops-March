from flask import Flask
import pymysql
import os

app= Flask(__name__)

db_host=os.environ["DB_HOST"]
db_user=os.environ["DB_USER"]
db_pass=os.environ["DB_PASS"]
db_name=os.environ["DB_NAME"]

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