# Learniee

**Learniee** is a full-stack e-learning platform designed to provide students with a simple way to discover and explore educational courses.

The project is built using **React.js** on the frontend and **Flask/Python** on the backend. It includes user authentication, protected routes, course browsing, filtering, searching, sorting, and pagination.

---

## Features

### Authentication

* User registration and login
* Password hashing using Werkzeug
* JWT-based authentication
* Protected user routes
* Retrieve authenticated user's information
* Persistent authentication on the frontend

### Course Management

* Browse available courses
* Search courses by name or subject
* Filter courses by:

  * Subject
  * Grade
  * Price range
  * Minimum rating
* Sort courses by:

  * Price — Low to High
  * Price — High to Low
  * Rating
* Paginated course results

### Frontend

* Responsive React interface
* React Router navigation
* Login and signup pages
* Protected dashboard
* Course browsing interface
* Dynamic API-driven course data

### Backend

* RESTful API built with Flask
* SQLAlchemy ORM
* JWT authentication
* CORS configuration
* Password hashing
* Query filtering and pagination
* SQLite/database integration

---

## Tech Stack

### Frontend

* React.js
* Vite
* JavaScript
* React Router
* CSS

### Backend

* Python
* Flask
* Flask-SQLAlchemy
* Flask-JWT-Extended
* Flask-CORS
* Werkzeug

### Database

* SQLite / SQLAlchemy

### Development Tools

* Git
* GitHub
* VS Code
* Postman

---

## Project Architecture

```text
Learniee/
│
├── backend/
│   ├── app.py
│   ├── config.py
│   ├── extensions.py
│   ├── models.py
│   ├── cousre_data.py
│   └── requirements.txt
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── vite.config.js
│   └── eslint.config.js
│
└── .gitignore
```

---

## Application Flow

```text
                    ┌──────────────────┐
                    │   React Frontend │
                    │     (Vite)       │
                    └────────┬─────────┘
                             │
                             │ HTTP Requests
                             ▼
                    ┌──────────────────┐
                    │   Flask REST API │
                    └────────┬─────────┘
                             │
                ┌────────────┴────────────┐
                │                         │
                ▼                         ▼
        ┌──────────────┐          ┌──────────────┐
        │ JWT Auth     │          │ SQLAlchemy   │
        │              │          │ ORM          │
        └──────────────┘          └──────┬───────┘
                                         │
                                         ▼
                                  ┌─────────────┐
                                  │  Database   │
                                  └─────────────┘
```

---

## API Endpoints

### Authentication

#### Register

```http
POST /api/signup
```

Example request:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "password123"
}
```

#### Login

```http
POST /api/login
```

Example request:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

The login endpoint returns a JWT access token that can be used to access protected endpoints.

#### Current User

```http
GET /api/me
```

Requires a valid JWT token.

---

### Courses

#### Get Courses

```http
GET /api/courses
```

The endpoint supports multiple query parameters.

Example:

```http
GET /api/courses?search=python&subject=Programming&grade=10
```

### Available Filters

| Parameter    | Description                      |
| ------------ | -------------------------------- |
| `search`     | Search by course name or subject |
| `subject`    | Filter by subject                |
| `grade`      | Filter by grade                  |
| `min_price`  | Minimum course price             |
| `max_price`  | Maximum course price             |
| `min_rating` | Minimum rating                   |
| `sort`       | Sort course results              |
| `page`       | Page number                      |
| `per_page`   | Number of results per page       |

### Sorting

```text
price_asc
price_desc
rating_desc
```

Example:

```http
GET /api/courses?sort=price_asc
```

---

## Authentication Flow

Learniee uses **JWT (JSON Web Tokens)** for authentication.

```text
User
 │
 │ Login
 ▼
React Frontend
 │
 │ POST /api/login
 ▼
Flask Backend
 │
 │ Validate credentials
 ▼
Database
 │
 │ User found
 ▼
JWT Access Token
 │
 ▼
React
 │
 │ Store token
 ▼
Protected API Requests
```

The backend hashes passwords before storing them and verifies the password during login. Successful authentication generates an access token containing the user's ID.

---

## Database Models

### User

```text
User
├── id
├── name
├── email
└── password
```

### Course

```text
Course
├── id
├── name
├── subject
├── grade
├── price
├── teacher
└── rating
```

The backend defines these models using SQLAlchemy.

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AmeyDhuri/Learniee.git

cd Learniee
```

---

### 2. Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

#### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the Flask server:

```bash
python app.py
```

The backend will run on:

```text
http://localhost:5000
```

---

### 3. Frontend Setup

Open another terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will be available at the URL displayed by Vite, usually:

```text
http://localhost:5173
```

---

## Testing the API

You can test the backend using **Postman** or any API testing tool.

### Health Check

```http
GET /
```

Expected response:

```json
{
  "message": "Learniee API is running!!"
}
```

### Example API Flow

```text
1. Register user
       ↓
2. Login
       ↓
3. Receive JWT token
       ↓
4. Send JWT with protected requests
       ↓
5. Access current user
       ↓
6. Browse courses
       ↓
7. Search / filter / sort courses
```

---

## What I Learned

Building Learniee helped me gain practical experience in full-stack web development, particularly:

* Building REST APIs with Flask
* Connecting React with a Python backend
* Implementing JWT authentication
* Password hashing and credential validation
* Working with SQLAlchemy models
* Designing API endpoints
* Handling HTTP requests and responses
* Using query parameters for filtering
* Implementing pagination
* Implementing sorting and searching
* Protecting frontend routes
* Managing authentication state in React
* Handling CORS between frontend and backend
* Testing APIs with Postman
* Structuring a full-stack project into frontend and backend applications

---

## Key Technical Concepts

### Frontend

```text
React
  ↓
Components
  ↓
React Router
  ↓
API Requests
  ↓
Backend
```

### Backend

```text
Flask
  ↓
Routes
  ↓
Authentication
  ↓
SQLAlchemy
  ↓
Database
```

### Authentication

```text
Credentials
    ↓
Password Verification
    ↓
JWT Generation
    ↓
Access Token
    ↓
Protected Requests
```

---

## Future Improvements

Some features that can be added in future versions:

* [ ] Course details page
* [ ] Course enrollment
* [ ] Student progress tracking
* [ ] Teacher/admin dashboard
* [ ] Course creation through the UI
* [ ] Reviews and ratings
* [ ] Wishlist functionality
* [ ] Payment integration
* [ ] Profile management
* [ ] Refresh tokens
* [ ] Role-based authorization
* [ ] Deployment
* [ ] Automated testing
* [ ] Docker support
* [ ] CI/CD pipeline

---

## Screenshots

Add screenshots of the following pages here:

```text
Login
Signup
Dashboard
Course Listing
Course Filters
```

Example:

```markdown
![Login Page](screenshots/login.png)

![Dashboard](screenshots/dashboard.png)
```

---

## Project Status

**In Development**

Learniee is an ongoing full-stack learning project. The current implementation focuses on authentication, protected routes, course APIs, course filtering, searching, sorting, and pagination.

---

## Author

**Amey Dhuri**

GitHub:
https://github.com/AmeyDhuri

---

## If you find this project useful

Feel free to fork the repository, explore the code, or suggest improvements.

**Built with Python, Flask, React and JavaScript.**
