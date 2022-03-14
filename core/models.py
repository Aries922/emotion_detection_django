from django.db import models

# Create your models here.


class Photo(models.Model):
    image = models.ImageField()



class Song(models.Model):

    TYPES = (
        ('happy','happy'),
        ('sad','sad'),
        ('fear','fear'),
        ('angry','angry'),
        ('disgust','disgust'),
        ('surprise','surprise'),
        ('neutral','neutral'),

    )

    name = models.CharField(max_length=150);
    type = models.CharField(choices= TYPES,max_length= 50);
    link = models.CharField(max_length= 1000)

    def __str__(self):
        return self.type + " " + self.name;    


class Conditions(models.Model):

    TYPES = (
        ('happy','happy'),
        ('sad','sad'),
        ('fear','fear'),
        ('angry','angry'),
        ('disgust','disgust'),
        ('surprise','surprise'),
        ('neutral','neutral'),

    )
    condition = models.CharField(max_length=150);
    type = models.CharField(choices= TYPES,max_length= 50);

    def __str__(self):
        return self.type + " " + self.condition;        


class Emotion(models.Model):
    emotion = models.CharField(max_length=50)
