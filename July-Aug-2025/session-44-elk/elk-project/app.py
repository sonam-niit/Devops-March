import logging
import socket
import json

import time

HOST = "localhost"
PORT = 5044

# Configure logging
logger = logging.getLogger("python-app")
logger.setLevel(logging.INFO)

# Custom log handler to send logs to Logstash TCP
class LogstashHandler(logging.Handler):
    def emit(self, record):
        log_entry = self.format(record)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            s.sendall((log_entry + "\n").encode("utf-8"))
            s.close()
        except Exception as e:
            print(f"Error sending log: {e}")
# Attaching handler to logger
logger.addHandler(LogstashHandler())
# Create formatter to bind JSON data
formatter = logging.Formatter('{"message": "%(message)s", "level": "%(levelname)s"}')
# Attach formatter to your handler
logger.handlers[0].setFormatter(formatter)

# Generate logs
for i in range(10):
    logger.info(f"Hello from Python log #{i}")
    time.sleep(2)
