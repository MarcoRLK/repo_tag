from django.db import models

# Create your models here.


class User(models.Model):

    user_name = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.user_name

class Repository(models.Model):

    github_id = models.CharField(max_length = 20, primary_key=True, unique=True)
    owner = models.ForeignKey('User', on_delete=models.CASCADE)

class Tag(models.Model):
    
    tag_name  = models.CharField(max_length = 50)
    color = models.CharField(max_length = 20)
    creator = models.ForeignKey('User', on_delete=models.CASCADE)
    repos = models.ManyToManyField(Repository)

    def __str__(self):
        return self.tag_name
