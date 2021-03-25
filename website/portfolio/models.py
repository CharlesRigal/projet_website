from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Index_wording(models.Model):
    wording= models.TextField()


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
    fk_category = models.ForeignKey(Category, verbose_name="projet categoriser", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
