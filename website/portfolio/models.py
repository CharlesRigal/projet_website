from django.db import models

# Create your models here.


class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField("Objet", max_length=100)
    message = models.TextField("message")


class Cv(models.Model):
    cv = models.FileField("charles_rigal_cv.pdf", upload_to="portfolio/cv/")


class Skill(models.Model):
    name = models.CharField("Nom", max_length=50)
    subheading = models.TextField()
    wording = models.TextField()
    picture = models.ImageField(str(name) + "_skill", upload_to="skill/")

    def __str__(self):
        return self.name


class Projet(models.Model):
    name = models.CharField("Nom", max_length=50)
    wording = models.TextField()
    picture = models.ImageField(str(name) + "_picture", upload_to="projet/")
    skills = models.ManyToManyField(Skill, blank=True)

    def __str__(self):
        return self.name
