from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import DAYS_OF_WEEK

class Availability(BaseModel):
    doctor = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='fk_doctor_availabilities_user_id')
    day_of_week = models.CharField(max_length=9 , choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'availability'
        unique_together = ('doctor', 'day_of_week', 'start_time')
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f"{self.doctor.user.get_full_name()} - {self.day_of_week} {self.start_time}-{self.end_time}"
