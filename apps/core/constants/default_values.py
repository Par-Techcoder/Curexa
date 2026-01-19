from enum import Enum

class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3

class Role(Enum):
    SUPERUSER = 0
    ADMIN = 1
    PATIENT = 2
    DOCTOR = 3
    
class AppointmentType(Enum):
    CONSULTATION = 1
    FOLLOW_UP = 2
    EMERGENCY = 3

class AppointmentStatus(Enum):
    PENDING = 1
    CONFIRMED = 2
    CANCELLED = 3
    COMPLETED = 4

class PaymentStatus(Enum):
    PENDING = 1
    SUCCESS = 2
    FAILED = 3
    REFUNDED = 4
    
class PaymentMethod(Enum):
    CREDIT_CARD = 1
    ONLINE = 2
    CASH_ON_DELIVERY = 3

class OrderStatus(Enum):
    PROCESSING = 1
    SHIPPED = 2
    DELIVERED = 3
    CANCELLED = 4
    
class DosageForm(Enum):
    TABLET = 1
    CAPSULE = 2
    SYRUP = 3
    OINTMENT = 4
    
class AGE_GROUP(Enum):
    CHILD = 1
    ADULT = 2
    SENIOR = 3
    
class InventoryAction(Enum):
    ADDED = 1
    REMOVED = 2
    RETURNED = 3
    DAMAGED = 4

class ResponseMessageType(Enum):
    SUCCESS = "success"
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"

class TestBookingStatus(Enum):
        PENDING = 1
        COMPLETED =2
        CANCELLED = 3

DAYS_OF_WEEK = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]    

TEST_CATEGORY = [
    ('blood', 'Blood Test'),
    ('urine', 'Urine Test'),
    ('imaging', 'Imaging'),
    ('other', 'Other'),
]
