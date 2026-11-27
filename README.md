# Engineering Mathematics Tutor 📚

An AI-powered Engineering Mathematics Tutor designed for B.Tech first-year students.

## Features
- Step-by-step mathematics solutions
- Simple Hinglish explanations
- Custom mathematics dataset
- Gemini AI integration
- Dataset-based answer retrieval

## Topics Covered
- Matrices and Gauss Elimination
- Vectors
- Differential Calculus
- Basic Integration

## Technology Stack
- Python
- Streamlit
- Google Gemini AI
- Adaption Dataset
- Pandas

## How to Run

1. Install dependencies:
   `pip install streamlit google-genai pandas`

2. Set your `GEMINI_API_KEY` environment variable.

3. Run:
   `streamlit run app.py`

## Project Goal
To make Engineering Mathematics easier to understand through accessible, step-by-step AI tutoring.

## Dataset Files

### 1. Original Dataset
File: `math_dataset.jsonl`

Contains the initial 5 Engineering Mathematics question-answer examples created for this project.

### 2. Improved Dataset
File: `clean_math_dataset.csv`

Contains 11 rows produced after processing the original dataset using Adaption Labs. It includes enhanced explanations and localized English and Hindi content.

### Dataset Improvement Process
The original dataset was processed using Adaption's Translate and Localize workflow for India (English) and Hindi. This improved the explanations and made the content more accessible to students.

### Evaluation Results
- Original dataset grade: C
- Improved dataset grade: B
- Original score: 6.0
- Improved score: 7.5
- Reported improvement: 25%

## Limitations

- The current dataset covers a limited number of Engineering Mathematics examples.
- The chatbot uses basic keyword matching to retrieve stored solutions.
- AI-generated answers may occasionally contain errors and should be verified.
- More topics and examples can be added in future improvements.

## Team
Solo participant.


## Live Demo

[Open Engineering Mathematics Tutor](https://engineering-math-tutor-64qw9sczweuh4yjgzpelcp.streamlit.app/)






 
