# Grad School Acceptance Prediction

This project aims to predict and study the acceptance/rejection of applicants to a grad school program using machine learning techniques. Two techniques are attempted: a random forest classifier and a neural network to predict whether an applicant will recieve either an acceptanced or a rejected status based on various metrics provided by the applicants.

## Dataset

I retrieved the data from the unofficial subreddit of UT Austin's Master of Science in Data Science program. Luckily, there are several threads for each admission period, ranging from Fall/Spring 2021 up to Fall/Spring 2023, and all with identical formatting—making data preparation and preprocessing relatively straightforward. Below is a picture example of the data layout:
![image](https://github.com/sergiicodes/UT-Austin-MSDS-admissions-predictor/assets/79073281/724b5ec7-265b-4b56-a155-4122fc0c5165)

The dataset used in this project is formatted as JSON and contains the following fields for each applicant:

- `status`: The acceptance/rejection status of the applicant.
- `applicationDate`: The date of application.
- `decisionDate`: The date of the admission decision.
- `education`: Information about the applicant's educational background, including institution, degree, and GPA.
- `gre`: In comma separated format, listing highest Quant, Verbal and Writing Scores among submitted, NaN if not submitted. 
- `recommendations`: The number of recommendations received.
- `experience`: Details about the applicant's relevant work experience.
- `statementOfPurpose`: A binary indicator (Y/N) for the presence of a statement of purpose and perhaps alongside an assisting comment.
- `comments`: Additional, miscellaneous comments provided by the applicant.

## Project Structure

The project directory has the following structure:

- `data/`: Contains the JSON dataset files.
- `notebooks/`: Jupyter notebooks used for data exploration, preprocessing, model development, and evaluation.
- `models/`: Saved trained models.
- `README.md`: This file providing an overview of the project.
- Other necessary project files.

## Getting Started

To get started with the project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/grad-school-prediction.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Explore the Jupyter notebooks in the `notebooks/` directory to understand the project workflow.
4. Preprocess the data, train the model, and evaluate the performance using the provided notebooks.
5. Make necessary modifications and customize the code as per your requirements.

## Dependencies

The project has the following dependencies:

- Python 3.8
- numpy
- pandas
- scikit-learn
- matplotlib
- jupyter

You can install the dependencies using the command `pip install -r requirements.txt`.

## Results and Discussion

Document your findings, insights, and observations here. Discuss the performance of the logistic regression model and the relevance of the features used for prediction. Include any visualizations or metrics that showcase the model's performance.

## Future Improvements

List any potential areas of improvement or future work that can be done to enhance the project. This can include exploring different models, incorporating additional features, or collecting more data for better predictions.

## License

[Specify the license for your project, if applicable.]

## Acknowledgments

[Optional: Mention any acknowledgments or credits for resources, code snippets, or references used in the project.]

