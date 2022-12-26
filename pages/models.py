from django.db import models

# Create your models here.
class Car(models.Model):
    years = [("2013","2013"),("2014","2014"),("2015","2015")]
    name = models.CharField(max_length=50 , default= "car" , verbose_name="Title")
    price = models.DecimalField(max_digits=7, decimal_places=2)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photos/%y/%m/%d')
    description = models.TextField(null = True , blank= True)
    model = models.CharField(default="default", choices=years , max_length=50)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['-name']
        verbose_name = "my car"
