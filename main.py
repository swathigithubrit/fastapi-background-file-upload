from fastapi import FastAPI, Request, UploadFile, File, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import shutil
import time
import os

app = FastAPI()

templates = Jinja2Templates(directory="templates")

# Create upload folder
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# ---------------------- BLOCKING UPLOAD ----------------------
@app.post("/upload-blocking/", response_class=HTMLResponse)
def upload_blocking(request: Request, file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Simulating slow process
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        time.sleep(5)   # Blocking delay

    return templates.TemplateResponse(
        "upload_blocking.html",
        {"request": request, "status": "Blocking Upload Successful!"}
    )

# ---------------------- BACKGROUND UPLOAD ----------------------
def save_file_background(file: UploadFile):
    """Uploads file without blocking the main thread"""
    try:
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            time.sleep(5)   # Background delay
        print("File uploaded successfully in background!")
    except Exception as e:
        print(f"Error: {e}")

@app.post("/upload-background/", response_class=HTMLResponse)
async def upload_nonblocking(
    request: Request,
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    background_tasks.add_task(save_file_background, file)

    return templates.TemplateResponse(
        "upload_background.html",
        {"request": request, "status": "Uploaded successfully in background"}
    )

# ---------------------- ROUTES FOR FORMS ----------------------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("upload_blocking.html", {"request": request})

@app.get("/background", response_class=HTMLResponse)
def background_form(request: Request):
    return templates.TemplateResponse("upload_background.html", {"request": request})
