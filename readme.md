# UT-Austin MSDS Admissions Predictor

## Project Overview

This project aims to predict the acceptance or rejection of applicants to the University of Texas at Austin's Master of Science in Data Science (MSDS) program. Utilizing machine learning techniques, specifically a Random Forest Classifier and a Neural Network, the project analyzes various applicant metrics to forecast admission outcomes.

---

## Dataset

The dataset was sourced from the [unofficial subreddit](https://www.reddit.com/r/MSDSO/) of UT Austin's MSDS program, covering admissions from Fall/Spring 2021 to Fall/Spring 2023. The data includes:

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

---

![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/ad370925-ad99-4589-8233-145701e1e3a9)

- **Academic Performance**: Not surprisingly, undergraduate GPA was the second most significant factor. A GPA around 3.50 was found to notably increase the chances of acceptance, underscoring the importance of strong academic credentials.

---

- **Work Experience**: Total experience in years also played a significant role in the prediction model. Even a modest amount of relevant work experience appeared to positively influence the admission outcome.

---

![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/6191b209-ef24-4c34-a895-9e87477a7169)

- **GRE Scores**: Interestingly, a significant portion of applicants, 80.6%, did not submit GRE scores, indicating that while the GRE is a consideration factor, it may not be a central component of the application. This aligns with our model's findings that GRE scores, though considered, had less impact on the prediction outcomes than other factors such as GPA and work experience.

---

![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/5aade766-1b3f-43c7-9952-7827ea0f9f58)

- **Educational Background Influence**: The distribution of educational institutions shows a diverse range of applicants, with the majority coming from undisclosed public/state universities, followed by UT Austin alumni, public Ivies, and Ivy League graduates. This suggests that while the program attracts applicants from prestigious institutions, it also considers a broad spectrum of candidates, reinforcing the inclusive nature of the admissions process.

---

### Model Performance:
![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/f8f6b942-714f-4baf-9ad4-4a54968e1123)

The Receiver Operating Characteristic (ROC) curve, with an Area Under Curve (AUC) score of 0.81, demonstrates the model's good classification ability. This high AUC score suggests that the model has a strong capability to distinguish between the 'Accepted' and 'Rejected' classes.

---

These results provide actionable insights for prospective applicants. They emphasize the benefits of early application, maintaining a strong GPA, and acquiring relevant work experience. For the admissions committee, these findings could inform the development of more transparent guidelines and expectations for applicants.

![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/81cd1900-f0d9-470b-8eee-33a604f1ac5c)

To reinforce the relevance of these insights, the University's official website states the following eligibility requirements:

- A minimum GPA of 3.0 in upper-division undergraduate courses.
- A bachelor's degree in a field related to the chosen program of study from a regionally accredited institution.
  
*Note: It is important to acknowledge that these results are model-based predictions and should be validated with actual admissions data for a more accurate understanding of the admission process.*
