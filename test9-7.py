class User():
    def __init__(self,first_name,last_name,**userinfos):
        self.first_name=first_name
        self.last_name=last_name
        userinfo={}
        for key,value in userinfos.items():
            self.userinfo[key]=value

    def describe_user(self):
        print(self.first_name+" "+self.last_name)
        print(self.userinfo)

    def greet_user(self):
        print('Hello, '+self.first_name+" "+self.last_name)

a=User("ZHIYIN","ZHU",age="18",sex="male")
a.describe_user()
a.greet_user()