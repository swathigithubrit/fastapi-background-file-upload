FastAPI Background File Upload System  
A complete demonstration project built using FastAPI, showcasing how to handle blocking and non-blocking (background) file uploads.  
This project is ideal for learning server-side file handling, BackgroundTasks, asynchronous processing, and template rendering.


Project Overview

Uploading large files can block the entire API execution until the file is processed.  
This can slow down the server and affect user experience.

This project solves that by implementing:

✔ Blocking Upload
- File upload is handled immediately.
- The API waits until the upload is fully completed.
- Best for small files.

✔ Non-Blocking (Background) Upload
- File upload happens in the background using FastAPI's `BackgroundTasks`.
- The API responds immediately while the file continues uploading behind the scenes.
- Ideal for large files & production-grade systems.

This project includes an easy-to-use **frontend** built with HTML + Jinja2 templates.


Features

- 🔹 Blocking file upload with server-side processing delay
- 🔹 BackgroundTasks-based non-blocking file upload
- 🔹 Clean UI with HTML templates (Jinja2)
- 🔹 Separate pages for blocking and background uploads
- 🔹 Safe upload directory creation
- 🔹 Fully documented and beginner-friendly project
- 🔹 Ideal for learning FastAPI async concepts



Tech Stack

| Component | Technology |
|----------|-------------|
| Backend  | FastAPI (Python) |
| Server   | Uvicorn |
| Templates | Jinja2 |
| Frontend | HTML, CSS |
| File System | Python shutil, os |


How It Works

1. Blocking Upload
When the user uploads a file:

- API receives the file
- Saves it to the directory
- Sleeps for 5 seconds (simulating heavy processing)
- Returns the response after finishing the upload

2. Background Upload
When the user uploads a file:

- API receives the file
- Immediately returns a success message
- File saving happens quietly in the background
- The user does not wait for processing

FastAPI’s `BackgroundTasks` makes this possible.



Installation & Setup

1️⃣ Clone the Repository

git clone https://github.com/YOUR-USERNAME/fastapi-background-file-upload.git
cd fastapi-background-file-upload

2️⃣ Create Virtual Environment (Windows PowerShell)

python -m venv venv
.\venv\Scripts\Activate.ps1

3️⃣ Install Dependencies

pip install fastapi uvicorn jinja2 python-multipart

4️⃣ Run the Server

uvicorn main:app --reload

5️⃣ Open in Browser

Blocking Upload Page:

http://127.0.0.1:8000/

Background Upload Page:

http://127.0.0.1:8000/background

🔗 API Routes
1. GET /

Loads the Blocking Upload UI.
2. GET /background

Loads the Background Upload UI.
3. POST /upload-blocking/

Processes the file upload synchronously.
4. POST /upload-nonblocking/

Processes file upload asynchronously in background.

