import logging
from flask import Flask

LOGSTASH_HOST = "localhost"
LOGSTASH_PORT = 5044

app = Flask(__name__)

#Configure logging to file
logging.basicConfig(
    filename="/var/log/myapp/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
    
)
@app.route("/hello")
def hello():
    app.logger.info("hello Endpoint was hit")
    return "Hello, CloudWatch!"

@app.route("/error")
def error():
    app.logger.error("Something went wrong")
    return "Error, logged..!", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
