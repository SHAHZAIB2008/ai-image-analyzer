# 🖼️ AI Image Analyzer

Upload an image and get description + creative suggestions using Ollama Vision model.

## 🚀 Features
- FastAPI backend with Ollama `llava` vision model
- Streamlit frontend for uploading images
- GPU acceleration (CUDA)
- Generates **description** and **creative suggestions**

## ⚡ Setup
```bash
# Clone repo
git clone https://github.com/your-username/ai-image-analyzer.git
cd ai-image-analyzer

# Create venv
python -m venv venv
source venv/bin/activate   # (Windows: venv\Scripts\activate)

# Install dependencies
pip install -r requirements.txt

# Run backend
uvicorn backend.main:app --reload

# Run frontend
streamlit run frontend/app.py
