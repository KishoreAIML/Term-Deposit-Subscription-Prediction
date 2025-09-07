# Term-Deposit-Subscription-Prediction
Machine Learning project to predict whether a client will subscribe to a term deposit using bank marketing data.

# Project Title  

## Contents  
- [Introduction](#introduction)  
- [Topics Covered](#topics-covered)  
- [Getting Started](#getting-started)  
- [Live Demo](#live-demo)  
- [Best Practices](#best-practices)  
- [FAQ](#faq)  
- [Troubleshooting](#troubleshooting)  
- [Contributing](#contributing)  
- [Additional Resources](#additional-resources)  
- [Challenges Faced](#challenges-faced)  
- [Lessons Learned](#lessons-learned)  
- [Why I Created This Repository](#why-i-created-this-repository)  
- [License](#license)  
- [Contact](#contact)  

---

## Introduction  
Briefly explain what your project is about, its purpose, and why it exists.  

## Topics Covered  
- Topic 1  
- Topic 2  
- Topic 3  

## Getting Started  
### Prerequisites  
List the tools/software needed.  

### Installation  
```bash
# Example
git clone https://github.com/username/repo-name.git
cd repo-name
pip install -r requirements.txt



# Bank Marketing Prediction

This project is based on the **direct marketing campaigns of a Portuguese banking institution**. The marketing campaigns were conducted through phone calls. Often, more than one contact with the same client was required in order to determine whether they would subscribe to the bank's term deposit product.

The objective of this project is to build a **machine learning model** that can predict whether a client will subscribe to a term deposit (`yes` or `no`) based on the given features.

---

## 📊 Dataset

- **Source**: [UCI Machine Learning Repository – Bank Marketing Data Set](https://archive.ics.uci.edu/ml/datasets/bank+marketing)  
- **Number of records**: ~41,000  
- **Features**:  
  - Client attributes: age, job, marital status, education, default, balance, housing loan, personal loan  
  - Contact attributes: contact type, last contact month/day, duration, campaign calls, previous contacts  
  - Outcome of previous marketing campaign  
- **Target variable**: `y` → Whether the client subscribed to a term deposit (`yes` or `no`)

---

## 🚀 Project Features
- Data cleaning and preprocessing  
- Exploratory Data Analysis (EDA)  
- Handling categorical and numerical variables  
- Imbalanced dataset handling  
- Model training and evaluation (Logistic Regression, Random Forest, LightGBM)  
- Deployment with **Flask web app** for real-time predictions  

---

## 📂 Repository Structure
bank-marketing-prediction/
│
├── data/ # Dataset files (excluded in .gitignore)
├── notebooks/ # Jupyter notebooks for EDA and model experiments
├── src/ # Source code (preprocessing, model training, utils)
├── models/ # Saved ML models
├── app/ # Flask application
│ ├── templates/ # HTML templates
│ └── static/ # CSS, JS, assets
├── requirements.txt # Dependencies
├── app.py # Flask entry point
├── README.md # Documentation
└── .gitignore # Ignored files
