from flask import Flask
import pymysql

app= Flask(__name__)

db_host="pw.c8xaeuki2r7w.us-east-1.rds.amazonaws.com"
db_user="admin"
db_pass="Sonam_skills.pw.live"
db_name="ecom"

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