import json, logging, socket, time, uuid
from datetime import datetime
from flask import Flask, request, jsonify

LOGSTASH_HOST = "localhost"
LOGSTASH_PORT = 5044

app = Flask(__name__)

class LogstashTCPHandler(logging.Handler):
    def emit(self, record):
        try:
            payload = self.format(record)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((LOGSTASH_HOST, LOGSTASH_PORT))
            s.sendall((payload + "\n").encode("utf-8"))
            s.close()
        except Exception as e:
            print("Log send error:", e)

logger = logging.getLogger("demo")
logger.setLevel(logging.INFO)
handler = LogstashTCPHandler()
# Our logs will be JSON with useful fields
class JSONFormatter(logging.Formatter):
    def format(self, record):
        base = getattr(record, "extra_fields", {})
        base.update({
            "message": record.getMessage(),
            "level": record.levelname,
            "timestamp": datetime.utcnow().isoformat() + "Z",
        })
        return json.dumps(base)
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)

def log_request(level, **fields):
    rec = logging.LogRecord(
        name="demo", level=getattr(logging, level),
        pathname=__file__, lineno=0, msg=fields.get("message",""),
        args=(), exc_info=None
    )
    rec.extra_fields = {k:v for k,v in fields.items() if k != "message"}
    logger.handle(rec)

@app.route("/hello")
def hello():
    t0 = time.time()
    name = request.args.get("name","world")
    resp = {"hello": name}
    duration = int((time.time()-t0)*1000)
    log_request("INFO",
        message="hello endpoint",
        path="/hello",
        method=request.method,
        status=200,
        duration_ms=duration,
        trace_id=str(uuid.uuid4()),
        client_ip=request.remote_addr,
        user_agent=request.headers.get("User-Agent")
    )
    return jsonify(resp), 200

@app.route("/boom")
def boom():
    # Simulate a server error
    t0 = time.time()
    duration = int((time.time()-t0)*1000)
    log_request("ERROR",
        message="boom endpoint simulated error",
        path="/boom",
        method=request.method,
        status=500,
        duration_ms=duration,
        trace_id=str(uuid.uuid4()),
        client_ip=request.remote_addr,
        user_agent=request.headers.get("User-Agent")
    )
    return jsonify({"error": "simulated"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
