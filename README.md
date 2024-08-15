

```markdown
# User and Task Management API

## Overview

A Flask-based RESTful API for managing users and tasks. Includes a simple HTML frontend and CI/CD setup with GitHub Actions and Docker.

## Setup

### Backend

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/km-er013/user-task-management-api.git
   cd user-task-management-api
   ```

2. **Setup Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   flask run
   ```

### Frontend

Open `index.html` in a web browser.

## API Endpoints

### User Management

- `GET /users` - Retrieve all users.
- `POST /users` - Add a new user.
- `GET /users/<id>` - Retrieve a user by ID.
- `PUT /users/<id>` - Update a user's information.
- `DELETE /users/<id>` - Delete a user by ID.

### Task Management

- `GET /tasks` - Retrieve all tasks.
- `POST /tasks` - Add a new task.
- `GET /tasks/<id>` - Retrieve a task by ID.
- `PUT /tasks/<id>` - Update a task's information.
- `DELETE /tasks/<id>` - Delete a task by ID.

## CI/CD

### GitHub Actions

- **File**: `.github/workflows/ci-cd.yml`


### Docker

- **Dockerfile**: Ensure this file is in the root directory.

