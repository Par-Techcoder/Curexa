from django.db import models
from apps.core.models.base_model import BaseModel

class PatientHistory(BaseModel):
    doctor = models.ForeignKey(
        'doctors.DoctorProfile',
        on_delete=models.CASCADE,
        related_name='fk_doctor_patient_history_doctor_id'
    )
    patient = models.ForeignKey(
        'accounts.PatientProfile',
        on_delete=models.CASCADE,
        related_name='fk_patient_patient_history_patient_id'
    )
    diagnosis_date = models.DateField(null=True, blank=True)

    # Major health condition categories (Boolean Flags)
    has_respiratory_issue = models.BooleanField(default=False)          # Covers cold, asthma, bronchitis, etc.
    has_cardiovascular_issue = models.BooleanField(default=False)       # Heart disease, hypertension
    has_diabetes = models.BooleanField(default=False)                   # Separate due to importance
    has_allergy = models.BooleanField(default=False)                    # Covers general allergies
    has_infectious_disease = models.BooleanField(default=False)         # Flu, viral infections, etc.
    has_digestive_issue = models.BooleanField(default=False)            # Ulcers, IBS, etc.
    has_musculoskeletal_issue = models.BooleanField(default=False)      # Arthritis, back pain
    has_neurological_issue = models.BooleanField(default=False)         # Seizures, migraines
    has_mental_health_issue = models.BooleanField(default=False)        # Depression, anxiety
    had_surgery = models.BooleanField(default=False)

    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'patient_history'
        verbose_name = "Patient History"
        verbose_name_plural = "Patient Histories"
        ordering = ['-created_at']

    def __str__(self):
        return f"History of {self.patient.get_full_name()} | Active: {self.is_active}"
