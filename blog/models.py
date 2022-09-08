from django.db import models

# Create your models here.


class Post(models.Model):
	# id = models.IntegerField(unique=True)
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    content = models.TextField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    # last_update = models.DateTimeField(auto_now=True)
    # image = 
    # status = 
	


    def __str__(self):
        return f"{self.title}" 
