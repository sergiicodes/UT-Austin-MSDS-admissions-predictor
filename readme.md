# UT-Austin MSDS Admissions Predictor

## Project Overview

This project aims to predict the acceptance or rejection of applicants to the University of Texas at Austin's Master of Science in Data Science (MSDS) program. Utilizing machine learning techniques, specifically a Random Forest Classifier and a Neural Network, the project analyzes various applicant metrics to forecast admission outcomes.

---

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
---
## Methods

1. **Data Preprocessing**: Standardizing formatting, handling missing values, and encoding categorical data.
2. **Model Development**: Implementing a Random Forest Classifier and a Bagging Classifier, as an ensemble learning technique.
3. **Evaluation**: Assessing model performance using accuracy, precision, recall, and F1 score.

---

## Results

The Random Forest and Bagging Classifiers were trained to predict admission results into the University of Texas at Austin's Master of Science in Data Science program, with the models achieving an overall accuracy of 87%. The precision, recall, and F1-score for the 'Accepted' class were particularly high at 92%, indicating a strong ability to identify candidates likely to be admitted. However, the metrics for the 'Rejected' class were lower, at 67%, which highlights an area for potential improvement, possibly by addressing the class imbalance or collecting more representative data.

### Key Insights:

- **Application Timing**: The feature importances revealed that the number of days between application and decision was the most influential factor, with earlier applications having a higher likelihood of acceptance. This suggests that promptness in application submission is critical.

- **Academic Performance**: Not surprisingly, undergraduate GPA was the second most significant factor. A GPA around 3.50 was found to notably increase the chances of acceptance, underscoring the importance of strong academic credentials.

- **Work Experience**: Total experience in years also played a significant role in the prediction model. Even a modest amount of relevant work experience appeared to positively influence the admission outcome.

- **GRE Scores**: While GRE scores (quantitative, verbal, and writing) were considered in the model, they had a lower impact compared to the factors above. Nonetheless, these scores are part of the comprehensive evaluation of an applicant's profile.

The decision tree visualization from the Random Forest offers a granular view of how different features interact to predict outcomes. For example, it shows that candidates with a GPA higher than 3.29 and who applied earlier were more likely to be accepted.

These results provide actionable insights for prospective applicants. They emphasize the benefits of early application, maintaining a strong GPA, and acquiring relevant work experience. For the admissions committee, these findings could inform the development of more transparent guidelines and expectations for applicants.

*Note: It is important to acknowledge that these results are model-based predictions and should be validated with actual admissions data for a more accurate understanding of the admission process.*

---

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


