from django.contrib.auth.backends import ModelBackend

class MyModelBackend(ModelBackend):

    def __init__(self):
        super(MyModelBackend, self).__init__()

    def authenticate(self,username=None,password=None):
        print "my logic"
        return super(MyModelBackend,self).authenticate(username=username,password=password)
