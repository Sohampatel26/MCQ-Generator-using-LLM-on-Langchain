# MCQ Generator using LLM and Langchain

![MCQ Generator](https://img.shields.io/badge/MCQ-Generator-blue.svg)

An AI-powered Multiple Choice Question (MCQ) generator, utilizing **Large Language Models (LLMs)** and **Langchain** for generating custom questions based on input text files or PDF documents. This tool allows educators, students, and learners to easily create customized MCQs, improving learning experiences and automating question generation tasks.

## 🚀 Features

- **Automatic MCQ generation**: Generates MCQs from `.txt` or `.pdf` files using LLMs.
- **Customizable**: Control the number of questions, subject, and difficulty level.
- **User-friendly UI**: Built using Streamlit for a simple, web-based interface.
- **CSV Download**: Export generated MCQs to a CSV file for easy sharing and integration.
- **Error handling**: Handles various errors like missing files or unsupported formats.
  
## 🛠️ Technologies Used

- **Python**: The core programming language used to build the project.
- **Langchain**: Facilitates the integration of LLMs for generating MCQs.
- **Streamlit**: Provides the user interface for uploading files and customizing MCQs.
- **Pandas**: Handles data and tabular representation of questions and choices.
- **dotenv**: Manages environment variables securely.
  
## 🖥️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Sohampatel26/MCQ-Generator-using-LLM-on-Langchain.git
cd MCQ-Generator-using-LLM-and-Langchan
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Add environment variables

Create a `.env` file in the root directory and add your environment variables such as API keys, if needed:

```
# .env
API_KEY=your_api_key_here
```

### 5. Run the application

```bash
streamlit run app.py
```

### 6. Access the Web Interface

Open your browser and go to `http://localhost:8501/`. Upload a `.txt` or `.pdf` file to generate MCQs, customize settings like the number of questions and difficulty level, and export the MCQs in CSV format.

## 📂 Project Structure

```bash
├── app.py                     # Main application entry point
├── requirements.txt            # Python dependencies
├── .gitignore                  # Ignored files and folders for Git
├── .env                        # Environment variables (not included in the repo)
├── README.md                   # Project documentation
├── src/                        # Source code folder
│   ├── mcqgenerator/           # MCQ generation logic
│   └── utils/                  # Helper functions (e.g., reading files, handling JSON)
└── response.json               # JSON template for LLM response
```

## 🧪 How It Works

1. **Upload Input File**: The user uploads a text or PDF file.
2. **LLM Processing**: The app uses Langchain and a pre-trained Large Language Model (LLM) to generate MCQs based on the input content.
3. **Customization**: Users can set the number of MCQs, topic, and difficulty level.
4. **MCQ Display**: The generated MCQs are displayed in a table, including questions, choices, and correct answers.
5. **CSV Export**: Users can export the generated MCQs as a CSV file for future use.

## 🤖 Future Enhancements

- **Improved LLM Integration**: Explore other LLMs for enhanced question generation.
- **NLP Features**: Add options to generate questions in different formats (e.g., True/False, short answer).
- **Advanced Customization**: Enable users to set more detailed customization options like question types, subtopics, and time limits.
- **Multi-language Support**: Expand support for generating questions in multiple languages.

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🧑‍💻 Contributing

Contributions are welcome! Please open an issue or submit a pull request to improve this project.

1. Fork the repository.
2. Create a new feature branch (`git checkout -b feature/my-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/my-feature`).
5. Open a pull request.

## 👨‍💻 Author

- **Soham Patel** - [GitHub Profile](https://github.com/Sohampatel26)

---

### Feel free to modify the template as needed! Let me know if you need further adjustments or assistance with other parts of your project.

<img width="1336" alt="image" src="https://github.com/user-attachments/assets/fc334d00-d0aa-4c9c-9136-26ebb893f9df">
