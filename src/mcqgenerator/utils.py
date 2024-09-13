""" Utility script to read the contents of PDF and convert the LLM response to a CSV file """

import os
import PyPDF2
import json
import traceback


# Read contents of file in .pdf or .txt file format
def read_file(file):
    try:
        if file.name.endswith(".pdf"):
            # Use PdfReader instead of PdfFileReader (Updated for PyPDF2 v3.0.0)
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()  # Use the updated extract_text() method
            return text

        elif file.name.endswith(".txt"):
            # For text files, directly read and decode the content
            return file.read().decode("utf-8")

        else:
            # Raise an exception if the file format is not supported
            raise Exception("Unsupported file format. Only PDF and text files are supported.")

    except Exception as e:
        # Print traceback and raise a custom error message for better debugging
        traceback.print_exception(type(e), e, e.__traceback__)
        raise Exception(f"Error reading the file: {str(e)}")


# Clean the generated response from LLM
def extract_json(markdown_string):
    try:
        # Extract JSON from markdown string using markers
        start_marker = '```json'
        end_marker = '```'
        start = markdown_string.find(start_marker) + len(start_marker)
        end = markdown_string.find(end_marker, start)
        
        if start == -1 or end == -1:
            raise ValueError("JSON markers not found in the response.")
        
        # Return the extracted JSON string, stripped of any extra spaces
        return markdown_string[start:end].strip()

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)
        raise Exception(f"Error extracting JSON: {str(e)}")


# Get table data from cleaned JSON
def get_table_data(cleaned_json):
    try:
        # Convert the JSON string to a dictionary
        data = json.loads(cleaned_json)
        quiz_data = []

        # Loop through each dictionary in the list
        for item in data:
            # Each item is a dictionary with numeric keys (representing questions)
            for key, question in item.items():
                mcq = question.get('mcq')
                options = question.get('options')
                correct_value = question.get('correct')

                # Append the question, options, and correct answer to the quiz data list
                quiz_data.append({
                    "MCQ": mcq,
                    "CHOICES": options,
                    "CORRECT ANSWER": correct_value
                })

        return quiz_data

    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        traceback.print_exception(type(e), e, e.__traceback__)
        raise Exception("Invalid JSON format")
    except Exception as e:
        # Handle general errors in the process
        traceback.print_exception(type(e), e, e.__traceback__)
        raise Exception("Error processing the table data")