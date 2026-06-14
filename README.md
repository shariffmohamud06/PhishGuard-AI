# PhishGuard – Machine Learning Email Phishing Detection

## Overview 

PhishGuard is a machine learning-based phishing email detection system that classifies emails as either legitimate or phishing using Natural Language Processing (NLP) techniques. The model transforms email text into numerical features with TF-IDF vectorization and uses Logistic Regression for classification. In addition to achieving high accuracy, the project investigates real-world failure cases to better understand the challenges of phishing detection.

## Dataset

The model was trained on approximately **82,000 labeled email messages** containing both legitimate and phishing emails. Email content was cleaned, preprocessed, and converted into numerical features using **TF-IDF vectorization** before training and evaluation.

## Results

The classifier achieved **98% accuracy** on a test set of **16,498 emails**. Out of **8,579 phishing emails**, the model correctly identified **8,442** and missed **137**, resulting in a phishing recall of approximately **98.4%**. Overall, the model made **313 errors**, consisting of **137 false negatives** (phishing emails that slipped through) and **176 false positives** (legitimate emails incorrectly flagged as phishing).

## Failure Analysis

Analysis of the **137 phishing emails that slipped through the classifier** revealed three recurring patterns. First, **domain-overlap spam** frequently resembled legitimate financial newsletters or investment reports, using vocabulary commonly found in genuine finance-related emails. Second, **non-English phishing emails** were more likely to be misclassified because the TF-IDF vocabulary was learned primarily from English text, leaving many foreign-language terms underrepresented. Third, **social-engineering emails disguised as personal conversations** often appeared legitimate due to their natural, conversational tone and lack of obvious spam keywords. These observed failure cases highlight the limitations of text-only classification and demonstrate how attackers can exploit language patterns that closely resemble legitimate communication.

## How to Run

**Prerequisites:** Python 3 and the following libraries:
```
pip install pandas numpy scikit-learn
```
**1. Clone the repository**
```
git clone https://github.com/shariffmohamud06/PhishGuard-AI.git
cd PhishGuard-AI
```
**2. Download the dataset**
This project uses the [Phishing Email Dataset](https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset) by Naser Abdullah Alam (CC BY-SA 4.0). Download it from Kaggle and place `phishing_email.csv` in the project folder, alongside `classifier.py`.

**3. Run the classifier**
```
python classifier.py
```
The script trains the model and prints the classification report, confusion matrix, total misclassified count, and examples of phishing emails the model missed.

## Limitations & Future Improvements

This project relies solely on the email body text and does not perform structured analysis of the sender, URL/domain features, other important phishing indicators, or attachments. As a result, phishing emails with convincing content but suspicious metadata may not be identified effectively.
The model was trained and evaluated on a single public dataset, meaning its performance is measured on data from a similar distribution. Real-world phishing campaigns continuously evolve, so accuracy on live email traffic may differ from the results reported here.
Additionally, the TF-IDF approach is based on word frequency rather than language understanding. It has limited ability to capture semantic meaning, making it more vulnerable to non-English emails, novel phishing techniques, and carefully worded social-engineering attacks.
Future work could include incorporating multilingual training data, extracting sender and URL-based features, experimenting with transformer-based models such as BERT, which would likely improve semantic and multilingual coverage but are heavier to train and run, and optimising classification thresholds to better balance missed phishing emails and false alarms in real-world deployments.

