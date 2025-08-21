from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import shutil, os, uuid
import ollama

# Initialize FastAPI
app = FastAPI()

# Allow CORS (so frontend can talk to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/analyze_image/")
async def analyze_image(file: UploadFile = File(...)):
    try:
        # Save uploaded file
        file_ext = os.path.splitext(file.filename)[-1]
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}{file_ext}")
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Prompt for description + suggestions
        prompt = """
        1. First, describe this image in detail. 
        2. Then, suggest the top 3 creative improvements, ideas, or recommendations 
           that could make this image more engaging, useful, or visually appealing.
        Format your answer as:
        Description: ...
        Suggestions:
        1. ...
        2. ...
        3. ...
        """

        # Send image to Ollama vision model
        response = ollama.chat(
            model="llama3.2-vision",   # ✅ make sure you pulled this with: ollama pull llama3.2-vision
            messages=[{
                "role": "user",
                "content": prompt,
                "images": [file_path]
            }]
        )

        # Extract response text
        description = response["message"]["content"]

        return JSONResponse({
            "status": "success",
            "analysis": description
        })

    except Exception as e:
        return JSONResponse({
            "status": "error",
            "message": str(e)
        }, status_code=500)
