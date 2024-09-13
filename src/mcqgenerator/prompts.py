""" Prompt Templates """

# Creating a zero-shot prompt template for generating and evaluate MCQs
GEN_TEMPLATE=""""
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to \
    create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Make sure to format your response like RESPONSE_JSON below with appropriate json structure and use it as a guide. \
    Ensure to make {number} MCQs

    {response_json}
"""


EVAL_TEMPLATE="""
You are an expert english grammarian and writer. Given a Multiple Choice Quiz for {subject} students.\
You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis. 
if the quiz is not at per with the cognitive and analytical abilities of the students,\
update the quiz questions which needs to be changed and change the tone such that it perfectly fits the student abilities
Quiz_MCQs:
{quiz}

Check from an expert English Writer of the above quiz:
"""