# Speech-to-Text Analyzer

A comprehensive web application that converts audio input into written text using Python and React, powered by OpenAI's Whisper model. This project aims to evolve into a multilingual translation application, providing users with accurate and efficient speech recognition capabilities.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Pictures](#pictures)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Backend Setup](#2-backend-setup)
    - [2.1. Environment Variables](#21-environment-variables)
    - [2.2. Docker Setup](#22-docker-setup)
    - [2.3. Apply Database Migrations](#23-apply-database-migrations)
    - [2.4. Create a Superuser (Optional)](#24-create-a-superuser-optional)
  - [3. Frontend Setup](#3-frontend-setup)
    - [3.1. Navigate to Frontend Directory](#31-navigate-to-frontend-directory)
    - [3.2. Install Dependencies](#32-install-dependencies)
    - [3.3. Configure Environment Variables](#33-configure-environment-variables)
    - [3.4. Start the Frontend Server](#34-start-the-frontend-server)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [Project Structure](#project-structure)
- [Additional Notes](#additional-notes)
- [Contributing](#contributing)
- [Contact](#contact)

## Features

- **Audio Recording**: Record audio directly from the browser.
- **File Upload**: Upload audio files (MP3, WAV, etc.) for transcription.
- **Transcription**: Convert speech to text using OpenAI's Whisper model.
- **Dark Mode**: Toggle between light and dark themes.
- **Download Recording**: Download recorded audio for reference.
- **Multilingual Support**: Future integration with translation services for multilingual capabilities.

## Technologies Used

- **Frontend**: React.js, Tailwind CSS
- **Backend**: Django, Django REST Framework, OpenAI Whisper
- **Database**: PostgreSQL
- **Containerization**: Docker, Docker Compose
- **Other Tools**: FFmpeg, PyDub

## Pictures
![Audio File to Transcript](./photos/Screenshot%202024-12-24%20at%2010.49.25%20AM.jpg)

## Prerequisites
Ensure you have the following installed on your machine:

- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Node.js & npm](https://nodejs.org/en/download/) (for frontend setup)

## Installation

Follow these steps to set up and run the application locally.

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/speech-to-text-analyzer.git
cd speech-to-text-analyzer
```

### 2. Backend Setup
The backend is built with Django and containerized using Docker. It connects to a PostgreSQL database also managed by Docker.

#### 2.1. Environment Variables
Create a .env file in the root directory to configure environment variables for the backend. Here's an example of what it might look like:

```bash
# .env

# Django settings
DJANGO_SECRET_KEY=your_secret_key_here
DJANGO_DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database settings
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
Note: Replace your_secret_key_here, your_db_name, your_db_user, and your_db_password with your actual settings.

#### 2.2. Docker Setup
Ensure Docker is installed and running on your machine. The application uses Docker Compose to manage both the backend and the PostgreSQL database.

1. Build and Start Containers

In the root directory of the project, run:
```bash
docker-compose up --build
```

This command will:
- Build the Docker images for the backend.
- Start the PostgreSQL database.
- Install all necessary dependencies.

2. Install System Dependencies

The backend requires FFmpeg for audio processing. The provided Dockerfile includes FFmpeg installation. If you're running the backend outside Docker, ensure FFmpeg is installed:
- macOS: brew install ffmpeg
- Ubuntu/Debian: sudo apt-get install ffmpeg
- Windows: Download from the FFmpeg website and add it to your PATH.

#### 2.3. Apply Database Migrations
Once the containers are up and running, apply Django migrations to set up the database schema.

```bash
docker-compose exec backend python manage.py migrate
```

#### 2.4. Create a Superuser (Optional)
To access the Django admin interface, create a superuser:

```bash
docker-compose exec backend python manage.py createsuperuser
```

Follow the prompts to set up your admin account.

### 3. Frontend Setup
The frontend is built with React and managed separately from the backend.

#### 3.1. Navigate to Frontend Directory
```bash
cd frontend
```

#### 3.2. Install Dependencies
Ensure you have Node.js and npm installed. Then, install the frontend dependencies:

```bash
npm install
```

#### 3.3. Configure Environment Variables
Create a .env file in the frontend directory with the following content:

```bash
REACT_APP_BACKEND_URL=http://localhost:8000
```

Note: Adjust REACT_APP_BACKEND_URL if your backend runs on a different URL or port.

#### 3.4. Start the Frontend Server
```bash
npm start
```
The frontend should now be accessible at http://localhost:3000.

## Usage
1. Access the Application

- Open your browser and navigate to http://localhost:3000.

2. Record Audio

- Click on "Start Recording" to begin recording audio directly from your browser.
- Click "Stop Recording" to end the recording.
- Optionally, download the recording by clicking "Download Recording".

3. Upload Audio

- Click on the file input to upload an existing audio file (e.g., MP3, WAV).
- Click "Upload Audio" to send the file to the backend for transcription.

4. View Transcription

- Once processing is complete, the transcribed text will appear on the screen under "Transcription Result".

5. Toggle Dark Mode
- Click the "Dark Mode" button to switch between light and dark themes for better user experience.

## Troubleshooting
### Common Issues
1. 500 Internal Server Error When Uploading Files
- Cause: Misconfiguration in ALLOWED_HOSTS or incorrect installation of the whisper package.
- Solution:
    - Ensure ALLOWED_HOSTS in the backend .env file is a comma-separated list of allowed hostnames (e.g., localhost,127.0.0.1).
    - Verify that the backend has openai-whisper installed instead of any other whisper package.
    - Rebuild the Docker containers after making changes:
```bash
docker-compose down
docker-compose up --build
```

2. CORS Errors
Cause: Backend not configured to accept requests from the frontend origin.
Solution:
Ensure django-cors-headers is installed and configured in settings.py with CORS_ALLOWED_ORIGINS including http://localhost:3000.

## Project Structure
```bash
speech-to-text-analyzer/
├── backend/
│   ├── api/
│   │   ├── views.py
│   │   └── ...
│   ├── your_project/
│   │   ├── settings.py
│   │   └── ...
│   ├── Dockerfile
│   ├── requirements.txt
│   └── ...
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   └── AudioRecorder.js
│   │   └── ...
│   ├── public/
│   ├── package.json
│   ├── .env
│   └── ...
├── docker-compose.yml
├── .env
└── README.md
```

## Additional Notes
Model Selection: OpenAI's Whisper offers various model sizes (tiny, base, small, medium, large). Choose based on your performance and accuracy requirements.
Performance Optimization: Loading the Whisper model can be resource-intensive. Consider loading the model once at server startup and reusing it for subsequent requests.
Security: For production, set DJANGO_DEBUG=False and properly configure ALLOWED_HOSTS. Also, secure your secret keys and consider using environment variables or secret management tools.
Future Enhancements:
Multilingual Support: Integrate translation APIs (e.g., Google Translate API) to add multilingual translation capabilities.
Asynchronous Processing: Implement background tasks (e.g., using Celery) for handling transcription to improve scalability and user experience.

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the Repository

2. Create a New Branch

```bash
git checkout -b feature/YourFeatureName
```

3. Commit Your Changes

```bash
git commit -m "Add some feature"
```

4. Push to the Branch

```bash
git push origin feature/YourFeatureName
```

5. Open a Pull Request

## Contact
For further assistance or questions, please contact simess@vcu.edu