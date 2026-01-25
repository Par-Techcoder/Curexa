from django.shortcuts import render
from django.views import View
from apps.docbook.services import appointment_services, availability_services
from apps.doctors.services import department_services
from apps.doctors.services import doctor_services
from apps.core.utilities.decorators import admin_required
from datetime import timedelta
from datetime import time


@admin_required(login_url="/admin/login/")
class DoctorsSchedulesView(View):
    def get(self, request):
        # ---------------------------
        # KPIs
        # ---------------------------
        todays_appointments = appointment_services.todays_appointments_count_for_all_doctors()
        doctor_on_duty = availability_services.today_active_doctors_count()
        available_time_slots = availability_services.today_doctor_available_slots()
        emergency_cases = appointment_services.todays_emergency_appointments_count()

        # ---------------------------
        # Filters & Types
        # ---------------------------
        departments = department_services.get_all_departments()
        appointment_types_status = appointment_services.get_all_appointment_types_status()

        # ---------------------------
        # Dates & Ranges
        # ---------------------------
        start_date, end_date = availability_services.get_current_week_range()

        # ---------------------------
        # Doctors & Appointments
        # ---------------------------
        doctors = doctor_services.get_all_doctors()
        doctors_appointments_today = appointment_services.doctors_appointments_today()
        doctors_appointments_by_week = appointment_services.doctors_appointments_in_current_week(
            start_date=start_date,
            end_date=end_date
        )

        # ---------------------------
        # Time Slots
        # ---------------------------
        all_times = [
            time(8, 0), time(8, 30), time(9, 0), time(9, 30),
            time(10, 0), time(10, 30), time(11, 0), time(11, 30),
            time(12, 0), time(12, 30), time(13, 0), time(13, 30),
            time(14, 0), time(14, 30), time(15, 0), time(15, 30),
            time(16, 0), time(16, 30), time(17, 0), time(17, 30),
            time(18, 0)
        ]

        # ---------------------------
        # DAILY SCHEDULE LOOKUP
        # ---------------------------
        schedule_lookup = {doctor["id"]: {} for doctor in doctors}
        for doc_id, doc in doctors_appointments_today.items():
            for appt in doc["appointments"]:
                schedule_lookup[doc_id][appt["start_time"]] = appt

        # ---------------------------
        # WEEKLY SCHEDULE
        # ---------------------------
        week_days = []
        current = start_date
        while current <= end_date:
            week_days.append(current)
            current += timedelta(days=1)

        weekly_schedule = {
            day: {t: {"count": 0, "appointments": []} for t in all_times}
            for day in week_days
        }

        for doc in doctors_appointments_by_week.values():
            for appt in doc["appointments"]:
                day = appt["date"]
                start_time = appt["start_time"]
                weekly_schedule[day][start_time]["count"] += 1
                weekly_schedule[day][start_time]["appointments"].append(appt)

        # ---------------------------
        # Build timeline for each doctor
        # ---------------------------
        doctors_today = []
        for doctor in doctors:
            doctor_id = doctor["id"]
            timeline = []

            for t in all_times:
                appt = schedule_lookup.get(doctor_id, {}).get(t)

                # Lunch break example
                if time(12, 0) <= t < time(13, 0):
                    timeline.append({
                        "type": "break",
                        "time": t,
                        "label": "Lunch Break"
                    })
                elif appt:
                    timeline.append({
                        "type": "appointment",
                        "time": t,
                        "patient": appt["patient_name"],
                        "badge": appt.get("appt_type_short", "C"),
                        "badge_class": appt.get("appt_type_css", "checkup"),
                    })
                else:
                    timeline.append({
                        "type": "free",
                        "time": t
                    })

            doctors_today.append({
                "doctor": {
                    "id": doctor["id"],
                    "code": doctor["id"],
                    "full_name": f'{doctor["doctor__first_name"]} {doctor["doctor__last_name"]}',
                    "avatar": doctor.get("profile_picture"),
                    "phone": doctor.get("phone"),
                    "email": doctor.get("email"),
                    "department": {
                        "name": doctor["specialization__name"] or "General",
                        "slug": doctor["specialization__name"] or "general",
                    }
                },
                "status": {
                    "label": "Available",  # derive from availability if needed
                    "css": "success"
                },
                "timeline": timeline
            })

        # ---------------------------
        # Context
        # ---------------------------
        context = {
            "todays_appointments": todays_appointments,
            "doctor_on_duty": doctor_on_duty,
            "available_time_slots": available_time_slots,
            "emergency_cases": emergency_cases,
            "doctors": doctors,
            "departments": departments,
            "doctors_appointments_today": doctors_appointments_today,
            "doctors_appointments_by_week": doctors_appointments_by_week,
            "appointment_types": appointment_types_status["types"],
            "appointment_status": appointment_types_status["statuses"],
            "all_times": all_times,
            "schedule_lookup": schedule_lookup,
            "week_days": week_days,
            "weekly_schedule": weekly_schedule,
            "doctors_today": doctors_today
        }

        return render(request, "admin/doctors/doctor_schedules.html", context)


    
     

@admin_required(login_url="/admin/login/")
class DoctorSchedulesView(View):
    def get(self, request, pk):
        return render(request, "admin/doctors/doctor_schedules.html")