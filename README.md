# Credit Card Fraud Detection

## Overview
This project aims to build a machine learning model to detect fraudulent credit card transactions. The dataset used contains transactions made by credit cards in September 2013 by European cardholders.

## Dataset
- **Source:** The dataset is highly imbalanced, with fraudulent transactions being only a small percentage of the total.
- **Features:** The dataset consists of numerical input variables resulting from a PCA transformation and two additional columns: `Time` and `Amount`.
- **Target Variable:** The `Class` column (0 = Non-Fraudulent, 1 = Fraudulent)

**Note:** The dataset is too large to be uploaded to GitHub. You can download it from [Google Drive](your_download_link_here) or Kaggle.

## Project Structure
```
credit_card_fraud_detection/
│-- data/                     # Dataset (not included in repo)
│-- notebooks/                # Jupyter notebooks for analysis
│-- models/                   # Saved machine learning models
│-- src/                      # Source code for data processing & modeling
│-- README.md                 # Project documentation
│-- requirements.txt          # Dependencies
│-- app.py                    # Streamlit web app (if applicable)
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/2004harshit/credit_card_fraud_detection.git
   cd credit_card_fraud_detection
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the Jupyter notebook to explore and train models:
   ```bash
   jupyter notebook
   ```
2. (If applicable) Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Models Used
- Logistic Regression

## Evaluation Metrics
- Accuracy
- Precision & Recall
- F1-Score
- ROC-AUC Score

## Contribution
Feel free to fork this repository, make improvements, and create pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The dataset is from the [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud) challenge.
- Inspired by various open-source ML projects.

---
✉️ **For queries, contact:** harshitchauhan10012004@gmail.com
