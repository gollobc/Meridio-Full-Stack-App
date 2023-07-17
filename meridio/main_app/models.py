from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.name} - {self.address}'

class Post(models.Model):
    item = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    description = models.TextField(max_length=250)
    date = models.DateField.auto_now()
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.item} - {self.date}'

class Comment(models.Model):
    content = models.TextField(max_length=150)
    accepted = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post}'


class Contact(models.Model):
    transaction = models.DateField()
    phone_number = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.comment}'