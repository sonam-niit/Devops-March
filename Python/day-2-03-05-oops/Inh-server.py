class Server:
    def __init__(self,name):
        self.name=name
        
    def start(self):
        return f"{self.name} is starting......."
    
class WebServer(Server):
    def deploy(self):
        return f"Deploying web app on {self.name}"
    
class ApplicationServer(Server):
    def deploy(self):
        return f"Deploying Application on {self.name}"
    
ws1=WebServer("Webserver01")
print(ws1.start())
print(ws1.deploy())
ws2=ApplicationServer("Webserver02")
print(ws2.start())
print(ws2.deploy())