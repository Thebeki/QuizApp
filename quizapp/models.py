from django.db import models
from django.db.models.fields.related import ManyToManyField
from django.contrib.auth.models import User

# Create your models here.
class Quiz(models.Model):
    nom = models.CharField(max_length=50)
    batafsil = models.CharField(max_length=200)
    savollar_soni = models.PositiveSmallIntegerField()
    davomiyligi = models.PositiveSmallIntegerField(default=300)
    def __str__(self):
        return self.nom

class Savol(models.Model):
    matn = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    def __str__(self):
        return self.matn

class Foydalanuvchi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    natija = models.FloatField()
    def __str__(self):
        return f"{self.user.username} ({self.natija})"

class Javob(models.Model):
    matn = models.CharField(max_length=200)
    togri = models.BooleanField(max_length=200)
    savol = models.ForeignKey(Savol, on_delete=models.CASCADE)
    def __str__(self):
        return self.matn
