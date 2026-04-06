# 🚀 GitHub Cloud Connector

## 📌 Overview

This project is a **GitHub Cloud Connector** built using **FastAPI (Python)**.
It integrates with the GitHub API using a **Personal Access Token (PAT)** and exposes simple REST endpoints to interact with GitHub resources.

The connector allows users to:

* Fetch repositories
* List issues
* Create issues

---

## ⚙️ Tech Stack

* **Backend:** Python
* **Framework:** FastAPI
* **HTTP Client:** Requests
* **Environment Management:** python-dotenv

---

## 🔐 Authentication

This project uses a **GitHub Personal Access Token (PAT)** for authentication.

* The token is stored securely in a `.env` file
* It is **never hardcoded** in the source code

---

## 🛠️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yashtupe/github-cloud-connector.git
cd github-cloud-connector
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### 3️⃣ Activate Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GITHUB_TOKEN=your_personal_access_token
```

---

## ▶️ How to Run the Project

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open in browser:

* API Base URL: http://127.0.0.1:8000
* Swagger UI (API Docs): http://127.0.0.1:8000/docs

---

## 📡 API Endpoints

### 🔹 1. Get Repositories

Fetch repositories of a user.

```http
GET /repos/{username}
```

**Example:**

```
GET /repos/yashtupe
```

---

### 🔹 2. Get Issues

Fetch issues from a repository.

```http
GET /issues/{owner}/{repo}
```

**Example:**

```
GET /issues/yashtupe/Bootcamp
```

---

### 🔹 3. Create Issue

Create a new issue in a repository.

```http
POST /create-issue
```

**Request Body:**

```json
{
  "owner": "yashtupe",
  "repo": "Bootcamp",
  "title": "Test Issue",
  "body": "Created via API"
}
```

---

### 🔹 4. Health Check

```http
GET /
```

**Response:**

```json
{
  "message": "GitHub Connector is running 🚀"
}
```

---

## ⚠️ Error Handling

The API handles:

* Invalid inputs
* GitHub API failures
* Authentication errors

---

## 🧠 Key Features

* Secure authentication using PAT
* Clean and modular architecture
* RESTful API design
* Input validation using Pydantic
* Real-time integration with GitHub API

---

## 🎯 Use Cases

* Automating GitHub workflows
* Internal developer tools
* Issue tracking systems
* Repository analytics dashboards

---

## 🚀 Future Enhancements

* OAuth 2.0 authentication
* Fetch commits
* Create pull requests
* Docker support

---

## 👨‍💻 Author

**Yash Tupe**
