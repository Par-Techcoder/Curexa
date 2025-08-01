<p align="center">
  <img src="static/images/curexa_logo.jpg" alt="Curexa Logo" width="100"/>
</p>

<h1 align="center">Curexa</h1>
<p align="center">💊 Online Pharmacy & 🩺 Doctor Appointment System</p>
<p align="center">
  <a href="https://github.com/Par-Techcoder/Curexa">GitHub</a> • 
  <a href="#features">Features</a> • 
  <a href="#getting-started">Install</a> • 
  <a href="#contact">Contact</a>
</p>

<br>

Curexa is a full-stack web application that provides an online platform for purchasing medicines and booking doctor appointments. Built with Django and PostgreSQL, it offers a seamless experience for patients and integrates pharmacy services with healthcare.

## Features

### 🏥 Core Functionalities
- **User Authentication System** with role-based access (Patients, Doctors, Admins)
- **Medicine E-commerce Platform** with shopping cart functionality
- **Doctor Appointment Booking System** with scheduling
- **Order Management** with payment processing

### 💊 Medistore Module
- Browse and search medicines by category
- Detailed product pages with images and descriptions
- Shopping cart with quantity adjustment

### 🩺 Doctor Module
- Doctor profiles with specialization details
- Appointment scheduling with time slots
- Patient history tracking
- Telemedicine integration (future scope)

### 📦 Orders Module
- Order tracking system
- Multiple payment gateway integration
- Invoice generation
- Delivery status updates

## Technology Stack

### Backend
- **Django** - Python web framework
- **Django REST Framework** - For API endpoints
- **PostgreSQL** - Relational database

### Frontend
- **HTML5, CSS3, JavaScript**
- **Bootstrap** - Responsive design
- **jQuery** - DOM manipulation

## Getting Started

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Par-Techcoder/Curexa.git
   cd Curexa
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows   
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   Create a `.env` file in the project root with the following variables:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_NAME=curexa_db
   DB_USER=db_user
   DB_PASSWORD=db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to `http://localhost:8000`

## Project Structure

```
Curexa/
├── apps/
│   ├── accounts/            # User authentication and role management
│   ├── medistore/           # Medicine e-commerce functionality
│   ├── docbook/             # Appointment scheduling system
│   ├── doctors/             # Doctor profiles and management
│   ├── orders/              # Order processing and payments
│   ├── core/                # Shared utilities and base functionality
├── config/                  # Django project configuration
├── templates/               # HTML templates
├── static/                  # Static files (CSS, JS, images)
├── venv/                    # Virtual environment
├── manage.py                # Django management script
├── .env                     # Environment variables
├── env_config.py            # Load environment variables from a .env
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Contact

For inquiries or support, please contact:
- Your Name - partha.sutradharmy@gmail.com
- Project Link: https://github.com/Par-Techcoder/Curexa

<!-- ## Screenshots -->
