import streamlit as st
import requests

BACKEND_URL = "http://127.0.0.1:8000/analyze_image/"

st.set_page_config(page_title="AI Image Analyzer", layout="centered")
st.title("🖼️ AI Image Analyzer")
st.write("Upload an image to get a description and suggestions from the AI.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Analyze Image"):
        with st.spinner("Analyzing image..."):
            files = {"file": uploaded_file}
            response = requests.post(BACKEND_URL, files=files)
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    st.subheader("Description")
                    # Try to split description and suggestions if formatted
                    analysis = data.get("analysis", "")
                    if "Suggestions:" in analysis:
                        desc, sugg = analysis.split("Suggestions:", 1)
                        st.write(desc.strip())
                        st.subheader("Suggestions")
                        st.write(sugg.strip())
                    else:
                        st.write(analysis)
                else:
                    st.error("Error: " + data.get("message", "Unknown error"))
            else:
                st.error("Server error: " + str(response.status_code))