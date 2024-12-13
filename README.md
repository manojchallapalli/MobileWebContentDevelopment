# SERVICEVERSE

SERVICEVERSE is a web-based platform designed to manage and facilitate a wide variety of user services. This platform is built using Django, leveraging its robust framework for scalability, modular design, and effective handling of dynamic content.

## Team Members
- **Manoj Challapalli** : mc86676n@pace.edu
- **Tejaswi Talluru** : tt48868n@pace.edu
- **Manjusha Domala** : md13277n@pace.edu


## Features

- **User Management**: Comprehensive account management including registration, login, and user profile features.
- **Media Handling**: Facilitates user-uploaded files stored in the `media` directory for efficient retrieval.
- **Responsive Design**: Incorporates dynamic templates for a user-friendly, responsive interface.
- **Asset Management**: Efficient static file handling for CSS, JavaScript, and image files.
- **Database Integration**: SQLite is used for seamless and lightweight data management.

## Project Structure

### Root Directory
- **manage.py**: Command-line utility for running and managing the Django application.
- **db.sqlite3**: SQLite database file containing the data for the application.

### Directories

1. **.vs**
   - Contains Visual Studio-specific configuration files.
   - Subfolder **v16** holds version-specific `.suo` files for project settings.

2. **accounts**
   - Handles user-related functionality like authentication and profile management.
   - **Files**:
     - `admin.py`: Admin panel customization.
     - `apps.py`: Application configuration.
     - `models.py`: Defines data models for user accounts.
     - `urls.py`: URL routing for the accounts module.
     - `views.py`: Handles logic for user-related views.

3. **assets**
   - Contains static assets such as CSS, JavaScript, and images.
   - Subdirectories include:
     - `admin`: Admin-related assets such as fonts and stylesheets.
     - `img`: Images for frontend display.
     - `js`: JavaScript files for interactivity.

4. **main**
   - Core logic of the application, including primary views and models.
   - **Files**:
     - `admin.py`: Admin panel configuration for core application models.
     - `forms.py`: Custom forms for user input.
     - `models.py`: Application data models.
     - `urls.py`: URL routing for the main application.
     - `views.py`: Logic for rendering pages and processing requests.

5. **SERVICEVERSE**
   - Main Django configuration folder.
   - **Files**:
     - `settings.py`: Project settings including database and installed apps.
     - `urls.py`: Global URL configuration.
     - `asgi.py` and `wsgi.py`: ASGI and WSGI configurations for deployment.

6. **media**
   - Directory for storing user-uploaded files categorized under subdirectories such as `carpenter`, `paint`, and `houseshift`.

7. **static**
   - Houses static files served by the application.
   - **Files**:
     - `home.css`, `service.css`: Stylesheets for the frontend.
     - `script.js`: JavaScript for user interactivity.

8. **templates**
   - Contains HTML templates for various application pages.
   - **Files**:
     - `404.html`: Custom error page displayed when a page is not found.
     - `booking.html`: Form for users to book services.
     - `bookingconfromation_mail.html`: Template for booking confirmation emails.
     - `bot.html`: A chatbot or automated assistant page.
     - `cancelbooking_email.html`: Template for booking cancellation emails.
     - `carpenter-service.html`: Information and booking page for carpenter services.
     - `catering-service.html`: Information and booking page for catering services.
     - `construction-service.html`: Information and booking page for construction services.
     - `editbooking.html`: Allows users to modify their service bookings.
     - `edit_mail.html`: Email template for booking modifications.
     - `enquiry.html`: Form for user inquiries and questions.
     - `faq.html`: Frequently Asked Questions page.
     - `graphs.html`: Displays graphical data, likely for admin insights.
     - `houseshifting-service.html`: Information and booking page for house-shifting services.
     - `interiordesign-service.html`: Information and booking page for interior design services.
     - `laundary-service.html`: Information and booking page for laundry services.
     - `login.html`: Login page for user authentication.
     - `main.html`: Main landing page of the application.
     - `mechanic-service.html`: Information and booking page for mechanic services.
     - `paint-service.html`: Information and booking page for painting services.
     - `parlour-service.html`: Information and booking page for beauty parlor services.
     - `password_reset.html`: Page for resetting user passwords.
     - `password_reset_done.html`: Confirmation page after password reset request.
     - `password_reset_form.html`: Form for entering a new password.
     - `password_reset_sent.html`: Notification page for sent password reset emails.
     - `payment.html`: Payment processing page for booked services.
     - `plumber-service.html`: Information and booking page for plumbing services.
     - `printing-service.html`: Information and booking page for printing services.
     - `profile.html`: User profile page displaying user details and bookings.
     - `register.html`: Registration page for new users.
     - `register_email.html`: Email template for user registration confirmation.
     - `services.html`: Lists all available services provided by the platform.
     - `technician-service.html`: Information and booking page for technician services.
     - `update_email.html`: Email template for updating user information.

## Installation and Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```

2. Navigate to the project directory:
   ```bash
   cd SERVICEVERSE
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.

## Usage

- Navigate to the homepage to explore available services.
- Register or log in for personalized features like booking and profile management.
- Access the admin panel at `/admin` for backend management.

## Contribution

1. Fork the repository and create a new branch.
2. Commit changes to the branch and push to your fork.
3. Submit a pull request for review and merging.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- Django Framework Documentation
- Contributors to open-source libraries used in the project

