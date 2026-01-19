from django.db import models
from apps.core.models.base_model import BaseModel
from apps.core.constants.default_values import DAYS_OF_WEEK

class Availability(BaseModel):
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='fk_doctor_availabilities_doctor_id'
    )
    date = models.DateField(db_index=True)
    is_available = models.BooleanField(default=True)
    day_of_week = models.CharField(max_length=9 , choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'availabilities'
        unique_together = ('doctor', 'day_of_week', 'start_time')
        ordering = ['day_of_week', 'start_time']

    def __str__(self):
        return f"{self.doctor.doctor.get_full_name()} - {self.day_of_week} {self.start_time}-{self.end_time}"
