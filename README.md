# Engineering Mathematics Tutor 📚

An AI-powered Engineering Mathematics Tutor designed for B.Tech first-year students. It helps students understand mathematical problems through step-by-step solutions and simple Hinglish explanations.

## 🚀 Features

- Step-by-step mathematics solutions
- Simple Hinglish explanations
- Custom Engineering Mathematics dataset
- Google Gemini AI integration
- Dataset-based answer retrieval
- Improved and localized learning content

## 📚 Topics Covered

- Matrices and Gauss Elimination
- Vectors
- Differential Calculus
- Basic Integration

## 🛠️ Technology Stack

- Python
- Streamlit
- Google Gemini AI
- Adaption Labs
- Pandas

## 📂 Dataset Files

### 1. Original Dataset

**File:** `math_dataset.jsonl`

Contains the initial 5 Engineering Mathematics question-answer examples created by the project author.

### 2. Improved Dataset

**File:** `clean_math_dataset.csv`

Contains 11 rows, including enhanced and localized versions of the original examples, generated through Adaption Labs. It includes improved explanations and English and Hindi content.

## 🔄 Dataset Improvement Process

The original dataset was processed using Adaption Labs' **Translate and Localize** workflow for India (English) and Hindi.

The improvement process focused on:

- Enhancing mathematical explanations
- Improving answer clarity
- Localizing content for English and Hindi learners
- Making the dataset more accessible to students

## 📊 Evaluation Results

The dataset quality assessment showed improvement after processing through Adaption Labs.

| Metric | Original | Improved |
|---|---:|---:|
| Dataset Grade | C | B |
| Evaluation Score | 6.0 | 7.5 |

**Reported improvement: 25%**

Evaluation was performed using Adaption Labs' dataset quality assessment.

## 💻 How to Run Locally

1. Clone this repository:

git clone https://github.com/Priyans12tech/Engineering-Math-Tutor.git

2. Install dependencies:

   `pip install streamlit google-genai pandas`

3. Configure your Google Gemini API key using Streamlit secrets or an environment variable.

4. Run the application:

   `streamlit run app.py`

## 🌐 Live Demo

[Open Engineering Mathematics Tutor](https://engineering-math-tutor-64qw9sczweuh4yjgzpelcp.streamlit.app/)

## 🎯 Project Goal

To make Engineering Mathematics easier to understand for B.Tech first-year students through accessible, interactive, and step-by-step AI-powered tutoring.

## ⚠️ Limitations

- The current dataset covers a limited number of Engineering Mathematics examples.
- The chatbot uses basic keyword matching to retrieve stored solutions.
- AI-generated answers may occasionally contain errors and should be verified.
- Gemini API availability may affect AI-generated responses.
- More mathematical topics and examples can be added in future improvements.

## 📖 Data Source

- Original dataset: Created by the project author.
- No third-party dataset was used.
- Dataset improvement and localization: Adaption Labs.
- Topics include matrices, vectors, differential calculus, and basic integration.

##
