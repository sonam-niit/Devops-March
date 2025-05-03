class Parent:
    def __init__(self,name):
        self.name=name
    def parentMethod(self):
        print(f"Parent Called {self.name}")
        
class Child(Parent):
    def childMethod(self):
        print('Child Called',self.name) 
        #can access parent variable
        
childobj= Child('MyParent')
#creating object
childobj.parentMethod() 
# child can access method of parent class
childobj.childMethod()