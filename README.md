# 🤖 AI Email Agent

An intelligent multi-agent system that automatically analyzes Gmail emails, classifies them using Artificial Intelligence, assigns priorities, makes decisions, executes actions, and monitors the complete workflow through a secure interactive dashboard.

---

## 📌 Overview

AI Email Agent is an autonomous email management system based on a Multi-Agent AI Architecture.

The application connects to Gmail using the Gmail API and OAuth2 authentication, retrieves emails, processes them through multiple AI agents, stores information in a database, and provides analytics through a modern React dashboard.

The system includes:

- 🤖 AI email classification
- ⚡ Priority prediction
- 🧠 Decision making
- 🚀 Automated actions
- 🔔 Notifications
- 💾 Memory Agent
- 📊 Agent monitoring
- 📈 Analytics dashboard
- 🔐 User authentication with JWT
- 🛡️ Protected application routes
- 📄 Export functionalities
- ⏰ Automated Gmail scheduler
- ☁️ Cloud deployment
- 🔄 GitHub Actions automation

---

## ✨ Features

### 🤖 Artificial Intelligence

- Gmail API Integration
- Automatic Email Classification
- AI Priority Scoring
- Decision Agent
- Action Agent
- Memory Agent
- Notification System
- Multi-Agent Workflow

### 🔐 Authentication & Security

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Protected Backend APIs
- Protected React Routes
- Token Management
- Logout System
- Scheduler Secret Authentication
- Environment-based secrets

### 📊 Dashboard

- Total processed emails
- Priority statistics
- Category distribution
- Agent decisions analysis
- Recent emails
- Monitoring dashboard
- Performance metrics
- Notification center
- Scheduler status

### 📄 Export System

- Export emails to Excel
- Export emails to PDF

### ⚙️ Agent Configuration

- AI model configuration
- Temperature setting
- Maximum emails processing
- Automatic action control

### 🔄 Automation

The system includes an automated scheduler that:

1. Connects to Gmail
2. Retrieves unread emails
3. Checks whether emails have already been processed
4. Processes new emails
5. Executes the AI workflow
6. Performs Gmail actions
7. Stores processed emails
8. Saves monitoring logs

The scheduler is automatically triggered through GitHub Actions.

---

## 🏗️ System Architecture

```text
                         Gmail API
                             |
                             ▼
                    Email Scheduler
                             |
                             ▼
                    Email Workflow
                             |
        -----------------------------------------
        |                  |                    |
        ▼                  ▼                    ▼
Classification      Priority Agent       Decision Agent
Agent
        |                  |                    |
        -----------------------------------------
                             |
                             ▼
                       Action Agent
                             |
              -------------------------------
              |                             |
              ▼                             ▼
        Gmail Actions              Notifications
              |                             |
              -------------------------------
                             |
                             ▼
                       Memory Agent
                             |
                             ▼
                    SQLite Database
                             |
                             ▼
                    FastAPI Backend
                             |
                             ▼
                    React Dashboard
```

---

## 🧠 Multi-Agent Workflow

```text
📩 Email Received
        |
        ▼
🤖 Classification Agent
        |
        ▼
⚡ Priority Agent
        |
        ▼
🧠 Decision Agent
        |
        ▼
🚀 Action Agent
        |
        ▼
🔔 Notification System
        |
        ▼
💾 Memory Agent
        |
        ▼
📊 Dashboard
```

---

## 🛠️ Technologies

### Backend

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Gmail API
- OAuth2
- JWT
- Passlib
- Pandas
- ReportLab

### Frontend

- ReactJS
- Material Dashboard 2 React
- Material UI
- Axios
- React Router
- Chart.js

### Artificial Intelligence

- Large Language Models
- Gemini API
- Prompt Engineering
- Multi-Agent Architecture
- AI-powered classification
- AI-powered priority analysis
- AI-powered decision making

### DevOps & Deployment

- GitHub
- GitHub Actions
- FastAPI Cloud
- Environment Variables
- Automated Scheduler
- REST API

---

## 📂 Project Structure

```text
ai-email-agent
│
├── backend
│   │
│   ├── app
│   │   │
│   │   ├── agents
│   │   │   ├── email_classifier_agent.py
│   │   │   ├── decision_agent.py
│   │   │   ├── action_agent.py
│   │   │   └── memory_agent.py
│   │   │
│   │   ├── api
│   │   │   └── routes.py
│   │   │
│   │   ├── auth
│   │   │   ├── routes.py
│   │   │   ├── security.py
│   │   │   └── dependencies.py
│   │   │
│   │   ├── database
│   │   │   ├── database.py
│   │   │   └── models.py
│   │   │
│   │   ├── scheduler
│   │   │   └── email_scheduler.py
│   │   │
│   │   ├── services
│   │   │   └── llm_service.py
│   │   │
│   │   ├── tools
│   │   │   ├── gmail.py
│   │   │   └── priority_scorer.py
│   │   │
│   │   └── workflows
│   │       └── email_workflow.py
│   │
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   │
│   ├── src
│   ├── layouts
│   ├── components
│   │   ├── ProtectedRoute
│   │   └── LogoutButton
│   │
│   ├── api
│   │   └── axios.js
│   │
│   ├── routes.js
│   └── App.js
│
└── .github
    │
    └── workflows
        └── scheduler.yml
```

> ⚠️ The `.github` directory is located at the root of the repository, not inside `backend`.

---

## 🗄️ Database

The system uses SQLite with SQLAlchemy ORM.

### Users

Stores authentication information:

- `username`
- `email`
- `hashed_password`

### Emails

Stores processed emails:

- `message_id`
- `sender`
- `subject`
- `body`
- `category`
- `priority`
- `score`
- `decision`

### Notifications

Stores generated notifications:

- `subject`
- `message`
- `status`
- `created_at`

### Agent Logs

Stores agent execution information:

- `status`
- `processed_emails`
- `last_action`
- `processing_time`
- `created_at`

### Agent Settings

Stores AI configuration:

- `model`
- `temperature`
- `max_emails`
- `auto_action`

---

## 📡 REST API

### Authentication

| Method | Endpoint         | Description          |
|--------|------------------|-----------------------|
| POST   | `/auth/register` | Create user account   |
| POST   | `/auth/login`    | Authenticate user     |

### Emails

| Method | Endpoint  | Description             |
|--------|-----------|--------------------------|
| GET    | `/emails` | Retrieve processed emails |

### Statistics

| Method | Endpoint       | Description           |
|--------|----------------|-------------------------|
| GET    | `/statistics`  | Dashboard statistics    |
| GET    | `/analytics`   | Advanced analytics      |
| GET    | `/performance` | Agent performance       |

### Monitoring

| Method | Endpoint        | Description       |
|--------|-----------------|--------------------|
| GET    | `/monitoring`   | Agent monitoring   |
| GET    | `/notifications`| Notifications      |

### Scheduler

| Method | Endpoint            | Description                 |
|--------|---------------------|-------------------------------|
| POST   | `/scheduler/run`    | Execute email scheduler       |
| GET    | `/scheduler/status` | Retrieve scheduler status     |

> The scheduler endpoint is protected using the `SCHEDULER_SECRET` environment variable.

### Export

| Method | Endpoint                  | Description             |
|--------|----------------------------|--------------------------|
| GET    | `/export/emails/excel`     | Export emails to Excel  |
| GET    | `/export/emails/pdf`       | Export emails to PDF    |

---

## 🔐 Authentication Flow

```text
User
  |
  ▼
Register
  |
  ▼
Password Hashing
  |
  ▼
Database Storage
  |
  ▼
Login
  |
  ▼
JWT Token Generation
  |
  ▼
Token Stored in Browser
  |
  ▼
Protected Dashboard Access
  |
  ▼
Logout
  |
  ▼
Token Removed
```

---

## ⏰ Automated Scheduler

The email scheduler is exposed through:

```
POST /scheduler/run
```

The endpoint is protected by a scheduler secret.

The automated execution flow is:

```text
GitHub Actions
       |
       ▼
POST /scheduler/run
       |
       ▼
FastAPI Cloud
       |
       ▼
Gmail Authentication
       |
       ▼
Retrieve Unread Emails
       |
       ▼
Check Already Processed Emails
       |
       ▼
Multi-Agent AI Workflow
       |
       ▼
Gmail Actions
       |
       ▼
Save Email to Database
       |
       ▼
Save Agent Log
       |
       ▼
Dashboard
```

---

## 🔄 GitHub Actions Automation

The scheduler is automatically triggered using GitHub Actions.

The workflow file is located at:

```
.github/workflows/scheduler.yml
```

> The `.github` directory must be located at the root of the repository.

Example workflow:

```yaml
name: Email Scheduler

on:
  schedule:
    - cron: "*/15 * * * *"
  workflow_dispatch:

jobs:
  run-scheduler:
    runs-on: ubuntu-latest

    steps:
      - name: Run Email Scheduler
        run: |
          curl --fail-with-body -X POST \
            "${{ secrets.BACKEND_URL }}/scheduler/run" \
            -H "X-Scheduler-Secret: ${{ secrets.SCHEDULER_SECRET }}"
```

**Automatic Execution**

The scheduler runs automatically according to the configured cron schedule. The example above runs the scheduler every 15 minutes.

**Manual Execution**

The workflow can also be triggered manually:

```
GitHub → Actions → Email Scheduler → Run workflow
```

---

## 🔑 Environment Variables

The application uses environment variables for sensitive configuration.

Example:

```env
GEMINI_API_KEY=your_gemini_api_key
GMAIL_TOKEN_JSON=your_gmail_token
JWT_SECRET_KEY=your_jwt_secret
SCHEDULER_SECRET=your_scheduler_secret
```

GitHub Actions requires:

- `BACKEND_URL`
- `SCHEDULER_SECRET`

These values must be configured in:

```
GitHub → Repository → Settings → Secrets and variables → Actions
```

> ⚠️ Sensitive information such as API keys, OAuth tokens, JWT secrets, and scheduler secrets must never be committed to GitHub.

---

## ☁️ Cloud Deployment

The backend is deployed using FastAPI Cloud.

**Production backend:**
`https://ai-email-agent-backend.fastapicloud.dev`

**API documentation:**
`https://ai-email-agent-backend.fastapicloud.dev/docs`

### Deploy Backend

From the backend directory:

```bash
cd backend
```

Login to FastAPI Cloud:

```bash
fastapi cloud login
```

Check the authenticated account:

```bash
fastapi cloud whoami
```

Deploy the application:

```bash
fastapi deploy
```

The deployed FastAPI application is then available through the production URL.

### ⚙️ FastAPI Cloud Environment Variables

The following environment variables must be configured in the FastAPI Cloud environment:

- `GEMINI_API_KEY`
- `GMAIL_TOKEN_JSON`
- `JWT_SECRET_KEY`
- `SCHEDULER_SECRET`

These variables are used for:

- AI API authentication
- Gmail authentication
- JWT security
- Scheduler authorization

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/ai-email-agent.git
```

### 🐍 Backend Setup

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### ▶️ Run FastAPI Locally

```bash
uvicorn main:app --reload
```

The backend will be available at:

```
http://127.0.0.1:8000
```

Swagger documentation:

```
http://127.0.0.1:8000/docs
```

### ⏰ Run Scheduler Locally

The scheduler can be executed manually during development:

```bash
python -m app.scheduler.email_scheduler
```

The production scheduler is triggered through `POST /scheduler/run` and automatically called by GitHub Actions.

### ⚛️ Frontend Setup

Go to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm start
```

---

## 🔄 Complete Workflow Example

```text
📩 Email Received
        ↓
🤖 Classification Agent
        ↓
⚡ Priority Calculation
        ↓
🧠 Decision Generation
        ↓
🚀 Action Execution
        ↓
🔔 Notification Creation
        ↓
💾 Database Storage
        ↓
📊 Dashboard Update
```

---

## 📊 Monitoring

The system records scheduler execution information such as:

- Scheduler status
- Last scan
- Processed emails
- Last executed action
- Processing time
- Number of errors

Example successful execution:

```text
🔎 Checking Gmail...
📩 1 emails found

Processing: Example email

📩 Step 1: Email received
🤖 Step 2: Classification Agent running
⚡ Step 3: Priority Agent running
🧠 Step 4: Decision Agent running
🚀 Step 5: Action Agent running
💾 Step 6: Memory Agent running

💾 Email saved in database
📡 Monitoring log saved
✅ Email scan completed
📊 Scheduler status: COMPLETED
```

---

## 🛡️ Scheduler Security

The `/scheduler/run` endpoint is protected using the `SCHEDULER_SECRET` environment variable.

The request must contain:

```
X-Scheduler-Secret: YOUR_SCHEDULER_SECRET
```

If the secret is missing, the API returns:

```
500 SCHEDULER_SECRET is not configured
```

If the secret is incorrect, the API returns:

```
401 Invalid scheduler secret
```

This prevents unauthorized users from triggering the email processing workflow.

---

## 🧠 Duplicate Email Protection

Before processing an email, the Memory Agent checks whether the email has already been processed.

```text
New Email
    |
    ▼
Check message_id
    |
    ├── Already exists
    │       |
    │       ▼
    │   Skip Email
    │
    └── Does not exist
            |
            ▼
       Process Email
            |
            ▼
       Save to Database
```

This prevents the same email from being processed multiple times.

---

## ⚠️ AI Quota Management

The AI workflow depends on the configured AI provider and its API quota.

If the API quota is exceeded, the scheduler records the error and monitoring information.

Example:

```
429 RESOURCE_EXHAUSTED
```

The scheduler can return:

```json
{
  "success": true,
  "processed_emails": 0,
  "last_action": "GEMINI_QUOTA"
}
```

This allows the dashboard and monitoring system to identify AI quota-related failures.

---

## 🔍 Scheduler Monitoring Endpoint

The current scheduler status can be retrieved using:

```
GET /scheduler/status
```

Example response:

```json
{
  "status": "COMPLETED",
  "last_scan": "2026-08-16 23:41:04",
  "processed_emails": 1,
  "last_action": "Email archived",
  "processing_time": "5.32s",
  "errors": 0
}
```

---

## 📈 Production Automation Architecture

```text
                    GitHub Repository
                           |
             ┌─────────────┴─────────────┐
             |                           |
             ▼                           ▼
       Backend Code                GitHub Actions
             |                           |
             ▼                           |
       FastAPI Cloud                    |
             |                           |
             ▼                           |
     Production API <--------------------
             |
             ▼
      /scheduler/run
             |
             ▼
         Gmail API
             |
             ▼
      Multi-Agent AI
             |
             ▼
         Database
             |
             ▼
       React Dashboard
```

---

## 🎯 Future Improvements

- RAG Integration
- Vector Database
- Semantic Search
- Outlook Integration
- Docker Deployment
- Kubernetes Deployment
- PostgreSQL Migration
- Multi-user Gmail accounts
- Advanced AI memory
- Retry mechanism for AI quota errors
- Background task processing
- Advanced scheduler configuration
- Email attachments analysis

---

## 👩‍💻 Author

**Fadwa Lacham**
Data Science Engineer
ENSIAS — Morocco

---

## 📄 License

This project is licensed under the MIT License.

---

## 🎨 Credits

The frontend dashboard is based on [Material Dashboard 2 React](https://www.creative-tim.com) by Creative Tim.

Original license: MIT License
Copyright (c) 2013-2021 Creative Tim