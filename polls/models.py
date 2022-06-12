from django.db import models

# Create your models here.
class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='upload/')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    desc = models.ForeignKey('Movie_desc', on_delete=models.CASCADE)
    video = models.OneToOneField('Video', on_delete=models.CASCADE)
    price = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def test1(self):
        return 10




class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie_desc(models.Model):
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description

class Customer(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='up/')
    phon_number = models.CharField(max_length=11)
    card_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    money = models.IntegerField()

    def __str__(self):
        return self.First_name
class Fon(models.Model):
    photo = models.ImageField(upload_to='upload/')


class Video(models.Model):
    caption = models.CharField(max_length=50)
    video = models.FileField()
    def __str__(self):
        return self.caption



