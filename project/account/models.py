from django.db import models

class User(models.Model):
  username = models.CharField(max_length=150, unique=True)
  email = models.EmailField(unique=True)
  password=models.CharField(max_length=50)
  date_of_birth = models.DateField()

  def __str__(self):
    return self.username