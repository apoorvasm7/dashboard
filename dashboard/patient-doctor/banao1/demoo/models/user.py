from django.db import models


class User(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='profiles/',null=True, blank=True)
    uname = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    usertype = models.CharField(max_length=20, default='patient')

    def register(self):
        self.save()

    @staticmethod
    def uname_login(uname):
        try:
            return User.objects.get(uname=uname)
        except:
            return False
    
    @staticmethod
    def get_user_by_id(ids):
        return User.objects.filter(id=ids)
