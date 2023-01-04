from django.db import models

# Create your models here.
class Mobile_cards(models.Model):
    image = models.ImageField(upload_to="mobiles")
    name = models.CharField(max_length=30)
    ram = models.IntegerField()
    rom = models.IntegerField()
    camera = models.IntegerField()
    battary = models.IntegerField()
    charging_speed = models.IntegerField()
    processor = models.IntegerField()
    
    
class SimpleUser(models.Model):
    name = models.CharField(max_length=10)
    total_cards = models.IntegerField(default=0)

    def __str__(self):
        return self.name+str(self.id)