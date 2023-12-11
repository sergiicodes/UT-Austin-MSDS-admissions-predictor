# UT-Austin MSDS Admissions Predictor

## Project Overview

This project aims to predict the acceptance or rejection of applicants to the University of Texas at Austin's Master of Science in Data Science (MSDS) program. Utilizing machine learning techniques, specifically a Random Forest Classifier and a Neural Network, the project analyzes various applicant metrics to forecast admission outcomes.

## Dataset

The dataset was sourced from the unofficial subreddit of UT Austin's MSDS program, covering admissions from Fall/Spring 2021 to Fall/Spring 2023. The data includes:

![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/724b5ec7-265b-4b56-a155-4122fc0c5165)

- `status`: Acceptance or rejection status.
- `applicationDate`: Date of application.
- `decisionDate`: Date of the admission decision.
- `education`: Applicant's educational background.
- `gre`: GRE scores (Quant, Verbal, Writing).
- `recommendations`: Number of recommendations.
- `experience`: Relevant work experience.
- `statementOfPurpose`: Presence of a statement of purpose (Y/N).
- `comments`: Additional applicant comments.

## Methods

1. **Data Preprocessing**: Standardizing formatting, handling missing values, and encoding categorical data.
2. **Model Development**: Implementing a Random Forest Classifier and a Bagging Classifier, as an ensemble learning technique.
3. **Evaluation**: Assessing model performance using accuracy, precision, recall, and F1 score.

## Results

*Discuss any key findings, insights, or patterns observed from the project. Highlight model performance metrics.*

## How to Use

### Prerequisites

- Python 3.x
- Libraries: pandas, numpy, scikit-learn, tensorflow (or other relevant libraries)

### Installation

*Provide steps to install and run your project. Example:*

```bash
git clone https://github.com/yourusername/UT-Austin-MSDS-admissions-predictor.git
cd UT-Austin-MSDS-admissions-predictor
pip install -r requirements.txt


