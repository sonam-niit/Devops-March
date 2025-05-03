class Server:
    # Object initialization
    # member variables serverId,name,ip,status,memory_usage
    def __init__(self,serverId,name,ip):
        self.serverId=serverId
        self.name=name
        self.ip=ip
        self.status= "offline"
        self.memory_usage=0
    ## Methods
    def ping(self):
        return f"pinging {self.ip}......."
    def getStatus(self):
        return f"{self.name} status is {self.status}"
    def updateStatus(self):
        if self.status=="offline":
            self.status= "online"
        else:
            self.status = "offline"
        print(f'{self.name} status updated successfully')
    
## Creating objects
web_server1 = Server("SI123456789","Webserver1","192.168.1.10")
result1=web_server1.ping()
print(result1)
web_server2 = Server("SI123456710","Webserver2","192.168.1.11")
print(web_server2.ping())
print(web_server1.getStatus())
web_server1.updateStatus()
print(web_server1.getStatus())