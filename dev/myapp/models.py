from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    start_month = models.DateField()
    end_month = models.DateField()
    start_year = models.DateField()
    end_year = models.DateField()

    def __str__(self) -> str:
        return str(self.name)
