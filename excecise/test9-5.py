class User():
    def __init__(self,first_name,last_name,login_attempts=0,**userinfos):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=login_attempts
        self.userinfo={}
        for key,value in userinfos.items():
            self.userinfo[key]=value

    def describe_user(self):
        print(self.first_name+" "+self.last_name)
        print(self.userinfo)

    def greet_user(self):
        print('Hello, '+self.first_name+" "+self.last_name)

    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempts(self):
        self.login_attempts=0

a=User('ZHIYIN','ZHU',age=18,sex='male')
a.describe_user()
a.greet_user()
