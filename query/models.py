from django.db import models

# Create your models here.
class Message(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    content = models.TextField(max_length=500)

class Meta:
    db_table=u'Message'

def __unicode__(self):
        return u"%d %s %s %s %d" % (self.pk, self.first_name, self.last_name, self.email,self.content)