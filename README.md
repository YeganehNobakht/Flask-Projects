# Flask Webhook App for Alertmanager Alerts

This Flask app acts as a webhook receiver for Alertmanager alerts. It processes incoming alerts, stores them based on team and severity, and sends an email notification for each alert. You can customize the alert storage and notification settings as needed.

## Requirements

- Python 3.7 or higher
- Flask
- Python-dotenv (for loading environment variables)
- smtplib (for email sending)

## Installation

1. **Clone the repository:**

    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2. **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### 1. Create a `.env` file

The `.env` file is used to store sensitive information such as email credentials. The app will automatically load this file using `python-dotenv`.

Create a `.env` file in the root directory of the project with the following content:

```env
EMAIL_USERNAME=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
TO_EMAIL=recipient_email@example.com
```


# Notes API Documentation

This API allows you to manage your notes, including the ability to create, retrieve, update, delete, and export notes in various formats such as JSON and YAML.
