from django.db import models
import datetime
class UpcomingSpecialsManager(models.Manager):
    def Upcoming(self):
        today=datetime.date.today()
        return super().get_queryset().filter(date_gte=today)

class DailySpecial(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    decsription=models.TextField()

    objects=UpcomingSpecialsManager()
    def __str__(self):
        return self.name

        
        
         
