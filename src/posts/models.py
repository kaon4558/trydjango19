from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add = False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=False)
    
    def __unicode__(self):
        return self.title

    def __str(self):
        return self.title

    def get_absolute_url(self):
    	return "/posts/%s/" %(self.id)