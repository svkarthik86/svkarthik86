class student:
    def __init__(self):
        self.stdName=""
        self.stdReg=""
        self.stdAdress="chennai"
    def set_value(self,name,Reg,Add):
        self.stdReg=Reg
        self.stdName=name
        self.stdAdress=Add
    def disply(self):
        print("RNO:"+ self.stdReg+"  " +"S.NAME:"+self.stdName+" "+"S.ADD:"+self.stdAdress)

s1=student()
s1.disply()

s2=student()
s2.disply()
# s1.stdReg="1011"
# s1.stdName="jhon"
# s1.stdAdress="chennai"
# s1.disply()
# s2=student()
