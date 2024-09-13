import json
import pandas as pd
import streamlit as st
import os
from dotenv import load_dotenv
import traceback
from src.mcqgenerator.utils import read_file, extract_json, get_table_data
from src.mcqgenerator.generate import generate_evaluate_chain

# Load environment variables
load_dotenv()

# Load JSON Response format file with error handling
try:
    with open("./response.json", "r") as file:
        RESPONSE_JSON = json.load(file)
except FileNotFoundError:
    st.error("Response JSON file not found.")
    st.stop()

# Set page configuration
st.set_page_config(
    page_title="MCQ Generator - Built by Soham Patel",
    page_icon="🧠",
    layout="centered",  # Center layout to avoid issues with large content
    initial_sidebar_state="expanded",
)

# Add custom CSS to improve overall design and readability
st.markdown("""
    <style>
        body {
            background-color: #F0F0F0;  /* Light grey background for overall page */
            color: #333333;  /* Darker text for better readability */
            font-family: 'Arial', sans-serif;
        }
        .main {
            background-color: #FFFFFF;  /* White background for main content area */
            color: #333333;  /* Dark text for better contrast */
            border-radius: 10px;  /* Rounded corners for the main container */
            padding: 2rem;  /* More padding for spacing */
            box-shadow: 0 0 10px rgba(0,0,0,0.1);  /* Subtle shadow for depth */
        }
        .stSidebar {
            background-color: #FAFAFA;  /* Slightly lighter grey background for sidebar */
            color: #333333;  /* Darker text for better readability */
            border-right: 2px solid #E0E0E0;  /* Solid separation line from main content */
        }
        .stButton>button {
            border-radius: 5px;
            border: none;
            background-color: #A8DADC;  /* Light teal button color */
            color: #1D3557;  /* Darker blue text for contrast on buttons */
            padding: 10px 24px;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #81B9C3;  /* Slightly darker teal hover effect */
        }
        h1, h2, h3, h4, h5, h6 {
            color: #2C3E50;  /* Darker headings for emphasis */
        }
        .stDataFrame {
            background-color: white;  /* Ensure table background is white */
            color: #000000 !important;  /* Dark black text for the table */
        }
        .css-2trqyj {
            padding-top: 5rem;
        }
        footer {
            text-align: center;
            font-size: 12px;
            color: #999999;  /* Subtle grey for the footer text */
            margin-top: 2rem;
        }
        table {
            color: #000000 !important; /* Force table text to be black */
        }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("🧠 MCQ Generator - Built by Soham Patel")
st.write("""
Welcome to the **MCQ Generator**, an AI-powered tool that helps you generate multiple-choice questions (MCQs) from text or PDF files. 
You can customize the number of questions, topic, and difficulty level, making it an ideal tool for educators and learners alike.
""")

# Sidebar
with st.sidebar:
    st.subheader("📄 Upload Your File")
    st.write("Please upload a `.txt` or `.pdf` file from which the MCQs will be generated.")
    
    file_upload = st.file_uploader(
        "Upload file", type=["txt", "pdf"])

    st.subheader("📝 Customize MCQs")
    mcq_count = st.number_input(
        "Number of MCQs", min_value=3, max_value=10, value=5, step=1)
    
    topic = st.text_input("Subject", max_chars=25, placeholder="e.g., Mathematics")
    difficulty = st.text_input("Difficulty Level", max_chars=20, placeholder="e.g., simple, mid, hard")

    generate_button = st.button("Generate MCQs")

# Main content
if file_upload and generate_button:
    with st.spinner("🔄 Generating your MCQs... Please wait!"):
        try:
            # Check file size before processing
            file_size = file_upload.size / (1024 * 1024)  # File size in MB
            if file_size > 50:  # Set file size limit to 50MB
                st.error("File is too large! Please upload a file smaller than 50MB.")
            else:
                # Read the file in chunks
                text = read_file(file_upload)

                # Generate MCQs
                response = generate_evaluate_chain(
                    {
                        "text": text,
                        "number": mcq_count,
                        "subject": topic,
                        "tone": difficulty,
                        "response_json": json.dumps(RESPONSE_JSON)
                    }
                )

                if 'quiz' in response:
                    quiz = response.get("quiz")
                    if quiz:
                        cleaned_json = extract_json(quiz)
                        table_data = get_table_data(cleaned_json)
                        if table_data:
                            df = pd.DataFrame(table_data)
                            df.index = df.index + 1
                            st.subheader("📚 Generated MCQs")
                            st.table(df.style.set_properties(**{'color': 'black'}))  # Ensure text is black

                            # Download the table as CSV
                            st.download_button(
                                label="⬇️ Download as CSV",
                                data=df.to_csv(index=False),
                                file_name="mcq.csv",
                                mime="text/csv",
                            )
                        else:
                            st.error("🚫 Error processing table data.")
                    else:
                        st.error("🚫 No MCQs generated.")
        except Exception as e:
            st.error("⚠️ An error occurred while generating MCQs.")
            st.text(traceback.format_exc())

# Footer
st.markdown("""
    <footer>
        MCQ Generator | Developed by <b>Soham Patel</b> | © 2024
    </footer>
""", unsafe_allow_html=True)

