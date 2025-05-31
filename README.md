# Farm Management System

A Django-based farm management system with JWT authentication, user management, and plot tracking capabilities.

## Features

- **User Management**
  - JWT-based authentication
  - User registration and login
  - Role-based access control
  - User profile management

- **Plot Management**
  - Create and manage farm plots
  - Unique plot identification system
  - Plot details tracking (name, location, size)
  - Timestamp tracking for plot creation and updates

- **Security**
  - JWT token-based authentication
  - Secure password handling
  - Protected API endpoints
  - Role-based permissions

## Tech Stack

- **Backend Framework**: Django 5.2.1
- **REST API**: Django REST Framework 3.14.0
- **Authentication**: 
  - djangorestframework-simplejwt 5.3.1
  - django-allauth 0.61.1
- **Database**: SQLite (default)
- **Containerization**: Docker

## Prerequisites

- Python 3.13 or higher
- Docker and Docker Compose (for containerized setup)
- Git

## Local Development Setup

### Option 1: Traditional Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/gks281263/farm.git
   cd farm
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run development server**
   ```bash
   python manage.py runserver
   ```

### Option 2: Docker Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/gks281263/farm.git
   cd farm
   ```

2. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

### Detailed Docker Setup Guide

#### Prerequisites
- Docker Engine (version 20.10.0 or later)
- Docker Compose (version 2.0.0 or later)

#### Step-by-Step Docker Setup

1. **Environment Setup**
   ```bash
   # Create .env file
   cp .env.example .env
   # Edit .env with your configuration
   nano .env
   ```

2. **Build the Docker Image**
   ```bash
   # Build the image
   docker-compose build
   ```

3. **Database Setup**
   ```bash
   # Run migrations
   docker-compose run web python manage.py migrate
   
   # Create superuser
   docker-compose run web python manage.py createsuperuser
   ```

4. **Start the Application**
   ```bash
   # Start all services
   docker-compose up -d
   
   # View logs
   docker-compose logs -f
   ```

5. **Access the Application**
   - Web Interface: http://localhost:8000
   - Admin Interface: http://localhost:8000/admin
   - API Endpoints: http://localhost:8000/api/

#### Docker Commands Reference

```bash
# Start services
docker-compose up -d

# Stop services
docker-compose down

# View logs
docker-compose logs -f

# Access shell
docker-compose exec web bash

# Run Django commands
docker-compose exec web python manage.py <command>

# Rebuild containers
docker-compose up -d --build

# Remove all containers and volumes
docker-compose down -v
```

#### Docker Configuration Files

1. **Dockerfile**
   ```dockerfile
   FROM python:3.13-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install -r requirements.txt
   COPY . .
   ```

2. **docker-compose.yml**
   ```yaml
   version: '3.8'
   services:
     web:
       build: .
       command: python manage.py runserver 0.0.0.0:8000
       volumes:
         - .:/app
       ports:
         - "8000:8000"
       environment:
         - DEBUG=1
         - SECRET_KEY=${SECRET_KEY}
         - DJANGO_ALLOWED_HOSTS=${DJANGO_ALLOWED_HOSTS}
   ```

#### Troubleshooting Docker Setup

1. **Permission Issues**
   ```bash
   # Fix permissions for mounted volumes
   sudo chown -R $USER:$USER .
   ```

2. **Container Not Starting**
   ```bash
   # Check container logs
   docker-compose logs web
   
   # Check container status
   docker-compose ps
   ```

3. **Database Issues**
   ```bash
   # Reset database
   docker-compose down -v
   docker-compose up -d
   docker-compose exec web python manage.py migrate
   ```

4. **Cache Issues**
   ```bash
   # Clear Docker cache
   docker system prune -a
   ```

## API Endpoints

### Authentication
- `POST /api/token/` - Obtain JWT token
- `POST /api/token/refresh/` - Refresh JWT token

### Users
- `POST /api/users/register/` - Register new user
- `GET /api/users/profile/` - Get user profile
- `PUT /api/users/profile/` - Update user profile

### Plots
- `POST /api/plots` - Create new plot
  - Required fields: plot_name, plot_location, plot_size
  - Authentication required

## Project Structure

```
farm/
├── farm_tool/          # Main project settings
├── users/             # User management app
│   ├── models.py      # User models
│   ├── views.py       # User views
│   ├── serializers.py # User serializers
│   └── urls.py        # User URLs
├── plots/             # Plot management app
│   ├── models.py      # Plot models
│   ├── views.py       # Plot views
│   ├── serializers.py # Plot serializers
│   └── urls.py        # Plot URLs
├── requirements.txt   # Project dependencies
├── Dockerfile        # Docker configuration
└── docker-compose.yml # Docker Compose configuration
```

## Environment Variables

Create a `.env` file in the project root with the following variables:

```env
DEBUG=1
SECRET_KEY=your-secret-key-here
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0 [::1]
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

