from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    status = (
        (1, 'admin'),
        (2, 'user')
    )
    status = models.IntegerField(choices=status, default=2, null=True, blank=True)



class Information(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField()
    description = models.TextField()
    googleplay = models.CharField(max_length=255)
    appstore = models.CharField(max_length=255)


class AdImage(models.Model):
    photo = models.ImageField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField()


class Region(models.Model):
    name = models.CharField(max_length=255)


class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Ads(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    photo = models.ManyToManyField(AdImage)
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    description = models.TextField()
    price = models.IntegerField()
    status = models.IntegerField(choices=(
        (1, 'in admin'),
        (2, 'accepted'),
        (3, 'rejected'),
        (4, 'sold'),
    ), default=1)
    is_top = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=True)

class how_to_sale_and_buy(models.Model):
    txt = models.TextField()


class safety_regulations(models.Model):
    text = models.TextField()

class Theme(models.Model):
    theme= models.CharField(max_length=255)


class Feedback(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    message = models.TextField()
    phone = models.BigIntegerField()
    email = models.EmailField()
    attach = models.FileField(null=True, blank=True)

class privacy_policy(models.Model):
    txt = models.TextField()


class Reklama(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img = models.ImageField(upload_to="Reklama/")
    link = models.URLField()
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=1, choices=((1, "in work"), (2, "deleted")))


class About(models.Model):
    logo = models.ImageField(upload_to='logo/')
    txt = models.TextField()