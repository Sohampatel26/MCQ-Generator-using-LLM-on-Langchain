""" Script to generate MCQ """

import os 
import json
import traceback
import warnings
import pandas as pd 

from dotenv import load_dotenv
from src.mcqgenerator.prompts import GEN_TEMPLATE, EVAL_TEMPLATE
from src.mcqgenerator.logger import logging

# Import packages from langchain and gemini 
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Suppress warnings
warnings.filterwarnings('ignore')

# Load environment variables
load_dotenv()

# Get gemini_key from .env
KEY = os.getenv("KEY")

# Setup Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7,google_api_key=KEY)

# Generate quiz prompt
quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "tone", "response_json"],
    template=GEN_TEMPLATE
)

# Setting up the LLMChain
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

# Evaluate quiz prompt 
quiz_evaluation_prompt = PromptTemplate(input_variables=["subject", "quiz'"], template=EVAL_TEMPLATE)

# Review quiz eval prompt
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)


# Setting up Sequential Chain
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "subject", "tone", "response_json"],
    output_variables=["quiz", "review"],
    verbose=True
)