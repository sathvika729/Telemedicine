# Telemedicine
Butterfly Hospitals - Telemedicine Web Application

This is a Flask-based web application that facilitates *doctor appointment booking* and *online prescriptions* for Butterfly Hospitals. The system is designed to streamline patient access to medical services from multiple hospital branches like Chittoor, Tirupati, Chandragiri, and Vellore.

 User Login
- Simple login system for users (no registration backend).
- Predefined sample user credentials.

 Online Appointment Booking
- Users can:
  - Choose their location
  - Select a department (Cardiology, Orthopedic, etc.)
  - Pick a doctor (dynamically populated from JSON)
  - Choose an available time slot and date
  - Provide symptoms for consultation

- The backend maps doctor IDs to names and confirms the booking.

Online Prescription Submission
- Patients can submit:
  - Personal details (Name, DOB, Email, Phone)
  - Medical history (medications, allergies, conditions, surgeries)
  - Present symptoms (description, duration, severity)

 Submission Confirmation Pages
- After submission, patients are shown a confirmation page with all their submitted data.

 Technologies Used

- *Python (Flask)* – backend server
- *HTML5 & CSS* – frontend
- *JavaScript* – for dynamic doctor selection
- *Jinja2* – template rendering
- *JSON* – doctor data served via an endpoint

 Project Structure

project/ │ ├── static/ │   └── style.css                # Optional stylesheet │ ├── templates/ │   ├── Login.html              # Login screen │   ├── options.html            # Landing page after login │   ├── appointment.html        # Appointment booking form │   ├── confirmation.html       # Appointment confirmation page │   ├── prescription.html       # Prescription form │   ├── prsction_submit.html    # Prescription confirmation │ ├── app.py                      # Main Flask application ├── Logo.png                    # Hospital logo └── README.md                   # This file


 Sample User Credentials

| Username   | Password |
|------------|----------|
| radhika    | r123     |
| priya      | p123     |
| sathvika   | s123     |
| lavanya    | l123     |
| vasudha    | v123     |

