from django.db import models
from django.db.models import Q
class Reservation(models.Model):
    start=models.DateTimeField()
    end=models.DateTimeField()

    @classmethod
    def find_available(cls, start, end):
        conflicts=cls.objects.filter(
            Q(start_lt=end) & Q(end__gt=start)
        )
        if conflicts.exists():
            return False
        return True       