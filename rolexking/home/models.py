from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import pytz
# Create your models here.

Warning_CHOICES = [
    ('WAIT', 'WAIT'),
    ('END', 'END'),
    ('DECLARE', 'DECLARE'),
    ('CLOSE', 'CLOSE'),
    ('OPEN', 'OPEN'),
]

MONTH_CHOICES = [
    ('Jan', 'January'),
    ('Feb', 'February'),
    ('Mar', 'March'),
    ('Apr', 'April'),
    ('May', 'May'),
    ('Jun', 'June'),
    ('Jul', 'July'),
    ('Aug', 'August'),
    ('Sep', 'September'),
    ('Oct', 'October'),
    ('Nov', 'November'),
    ('Dec', 'December'),
]

YEAR_CHOICES = [(str(year), str(year)) for year in range(2020, 2031)]

WEEK_CHOICES = [
    ('Mon', 'Monday'),
    ('Tue', 'Tuesday'),
    ('Wed', 'Wednesday'),
    ('Thu', 'Thursday'),
    ('Fri', 'Friday'),
    ('Sat', 'Saturday'),
    ('Sun', 'Sunday'),
]

class Rolex_Number(models.Model):
    No_id = models.AutoField(primary_key=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Today_Number = models.IntegerField()
    Sign = models.CharField(max_length=7, choices=Warning_CHOICES)
    Description = models.TextField(max_length=50)
    Created_at = models.DateTimeField(editable=True)
    Upload_to = models.DateTimeField(editable=False)
    Month = models.CharField(max_length=3, choices=MONTH_CHOICES, blank=True)
    Year = models.CharField(max_length=4, choices=YEAR_CHOICES, blank=True)
    Week = models.CharField(max_length=3, choices=WEEK_CHOICES, blank=True)

    def save(self, *args, **kwargs):
        india_tz = pytz.timezone('Asia/Kolkata')
        print(india_tz)
        now = timezone.now().astimezone(india_tz)
        print(now)
        if not self.Created_at:
            self.Created_at = now
        if not self.Upload_to:
            self.Upload_to = now
        if not self.Month:
            self.Month = now.strftime('%b')
        if not self.Year:
            self.Year = now.strftime('%Y')
        if not self.Week:
            self.Week = now.strftime('%a')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.Description
