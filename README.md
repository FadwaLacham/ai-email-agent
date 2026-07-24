# 🤖 AI Email Agent

An intelligent multi-agent system that automatically analyzes Gmail emails, classifies them using Artificial Intelligence, assigns priorities, makes decisions, executes actions, and monitors the complete workflow through a secure interactive dashboard.

---

# 📌 Overview

AI Email Agent is an autonomous email management system based on a Multi-Agent AI Architecture.

The application connects to Gmail using Gmail API and OAuth2 authentication, retrieves emails, processes them through multiple AI agents, stores all information in a database, and provides analytics through a modern React dashboard.

The system includes:

- AI email classification
- Priority prediction
- Decision making
- Automated actions
- Notifications
- Agent monitoring
- Analytics dashboard
- User authentication with JWT
- Protected application routes
- Export functionalities

---

# ✨ Features

## 🤖 Artificial Intelligence

- Gmail API Integration
- Automatic Email Classification
- AI Priority Scoring
- Decision Agent
- Action Agent
- Memory Agent
- Notification System
- Multi-Agent Workflow


## 🔐 Authentication & Security

- User Registration
- User Login
- JWT Authentication
- Password Hashing
- Protected Backend APIs
- Protected React Routes
- Token Management
- Logout System


## 📊 Dashboard

- Total processed emails
- Priority statistics
- Category distribution
- Agent decisions analysis
- Recent emails
- Monitoring dashboard
- Performance metrics
- Notification center


## 📄 Export System

- Export emails to Excel
- Export emails to PDF


## ⚙ Agent Configuration

- AI model configuration
- Temperature setting
- Maximum emails processing
- Automatic action control


## 🔄 Automation

- Gmail Scheduler
- Automatic email scanning
- Workflow execution
- Agent logs tracking

---

# 🏗 System Architecture

```
                         Gmail API
                             |
                             ▼

                    Email Scheduler

                             |
                             ▼

                    Email Workflow

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

# 🧠 Multi-Agent Workflow

```
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

# 🛠 Technologies

## Backend

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
- Schedule


## Frontend

- ReactJS
- Material Dashboard 2 React
- Material UI
- Axios
- React Router
- Chart.js


## Artificial Intelligence

- Large Language Models
- Ollama
- Llama 3
- Prompt Engineering
- Multi-Agent Architecture

---

# 📂 Project Structure

```
ai-email-agent

│
├── backend
│
├── app
│
│   ├── agents
│   │
│   │   ├── email_classifier_agent.py
│   │   ├── decision_agent.py
│   │   ├── action_agent.py
│   │   └── memory_agent.py
│
│   ├── api
│   │   └── routes.py
│
│   ├── auth
│   │   ├── routes.py
│   │   ├── security.py
│   │   └── dependencies.py
│
│   ├── database
│   │   ├── database.py
│   │   └── models.py
│
│   ├── scheduler
│   │   └── email_scheduler.py
│
│   ├── services
│   │   └── llm_service.py
│
│   ├── tools
│   │   ├── gmail.py
│   │   └── priority_scorer.py
│
│   └── workflows
│       └── email_workflow.py
│
├── main.py
│
└── requirements.txt


frontend

│
├── src
│
├── layouts
│
├── components
│   ├── ProtectedRoute
│   └── LogoutButton
│
├── api
│   └── axios.js
│
├── routes.js
│
└── App.js
```

---

# 🗄 Database

The system uses SQLite with SQLAlchemy ORM.

## Users

Stores authentication information:

- username
- email
- hashed_password


## Emails

Stores processed emails:

- message_id
- sender
- subject
- body
- category
- priority
- score
- decision


## Notifications

Stores generated notifications:

- subject
- message
- status
- created_at


## Agent Logs

Stores agent execution:

- status
- processed_emails
- last_action
- processing_time
- created_at


## Agent Settings

Stores AI configuration:

- model
- temperature
- max_emails
- auto_action

---

# 📡 REST API

## Authentication

| Endpoint | Description |
|---|---|
| POST /auth/register | Create user account |
| POST /auth/login | Authenticate user |


## Emails

| Endpoint | Description |
|---|---|
| GET /emails | Retrieve emails |


## Statistics

| Endpoint | Description |
|---|---|
| GET /statistics | Dashboard statistics |
| GET /analytics | Advanced analytics |
| GET /performance | Agent performance |


## Monitoring

| Endpoint | Description |
|---|---|
| GET /monitoring | Agent monitoring |
| GET /notifications | Notifications |


## Export

| Endpoint | Description |
|---|---|
| GET /export/emails/excel | Export Excel |
| GET /export/emails/pdf | Export PDF |

---

# 🔐 Authentication Flow

```
User

 ↓

Register

 ↓

Password Hashing

 ↓

Database Storage

 ↓

Login

 ↓

JWT Token Generation

 ↓

Token Stored in Browser

 ↓

Protected Dashboard Access

 ↓

Logout

 ↓

Token Removed
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/ai-email-agent.git
```

---

# Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

Run FastAPI:

```bash
uvicorn main:app --reload
```

Run Scheduler:

```bash
python -m app.scheduler.email_scheduler
```

---

# Frontend Setup

```bash
cd frontend

npm install

npm start
```

---

# ⚙ Workflow Example

```
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

# 🎯 Future Improvements

- RAG Integration
- Vector Database
- Semantic Search
- Outlook Integration
- Docker Deployment
- Cloud Deployment
- Kubernetes Deployment
- Multi-user Gmail accounts
- PostgreSQL Migration


---

# 👩‍💻 Author

**Fadwa Lacham**

Data Science Engineer

ENSIAS

Morocco


---

# 📄 License

This project is licensed under the MIT License.