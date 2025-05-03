class Server:
    def __init__(self,name):
        self.name=name
        
    def start(self):
        return f"{self.name} is starting......."
    def deploy(self):
        return f"Deploying web app using Parent Method"

#Apache Tomcat
class WebServer(Server):
    def deploy(self):
        return f"Deploying web app using Child Method"
    
ws = WebServer("WebServer01")
print(ws.start())
print(ws.deploy()) #child is overriding the parent method