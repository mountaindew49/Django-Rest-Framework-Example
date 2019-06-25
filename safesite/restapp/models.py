from django.db import models

# Create your models here.

class Group(models.Model):
    group_name = models.CharField(max_length=20)
    user = models.ForeignKey('User', related_name='groups', on_delete=models.PROTECT)

    def __str__(self):
        return self.group_name


class User(models.Model):
    user_id = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_id
