from django.db import models

# Create your models here.
class Report(models.Model):

    REPORT_TYPE_CHOICES = [
        ('H', 'Hole'),
        ('T', 'Trash'),
        ('S', 'Signalization')
    ]

    user_id = models.IntegerField()
    report_type = models.CharField(max_length=2, choices=REPORT_TYPE_CHOICES)
    description = models.TextField()
    upvotes = models.IntegerField(default=0)
    acknowledged = models.BooleanField(default=False)
    
