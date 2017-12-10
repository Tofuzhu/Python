class User():
    def __init__(self,first_name,last_name,**userinfos):
        self.first_name=first_name
        self.last_name=last_name
        for key,value in userinfos.items():
            self.userinfo[key]=value

    def describe_user(self):
        print(self.first_name+" "+self.last_name)
        while

    def greet_user(self):
