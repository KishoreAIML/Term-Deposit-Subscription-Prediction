# Term Deposit Subscription Prediction

A Machine Learning project to predict whether a bank client will subscribe to a **term deposit** based on marketing campaign data.

---

## Project Overview

Banks run direct marketing campaigns (phone calls) to promote term deposits.  
This project builds a **predictive model** that helps identify customers who are most likely to subscribe.

**Goal:**  
Predict target variable `y`  
- `yes` → Customer will subscribe  
- `no` → Customer will not subscribe

This helps banks:
- Improve marketing efficiency
- Reduce operational cost
- Target the right customers

---

## Dataset

- **Source:** UCI Machine Learning Repository – Bank Marketing Dataset
- **Records:** ~41,000
- **Target Variable:** `y` (subscription: yes/no)

### Features

**Client Information**
- age
- job
- marital
- education
- default
- balance
- housing loan
- personal loan

**Campaign Information**
- contact type
- month, day
- duration
- number of contacts
- previous contacts
- previous campaign outcome

---

## Project Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Handling Missing Values
5. Encoding Categorical Variables
6. Handling Imbalanced Data
7. Model Training
8. Model Evaluation
9. Model Saving
10. Flask Deployment

---

## Models Used

- Logistic Regression
- Random Forest
- LightGBM

Evaluation Metrics:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

---

## Project Structure

```

Term-Deposit-Subscription-Prediction/
│
├── data/                # Dataset (ignored in Git)
├── notebooks/           # EDA and experimentation
├── models/              # Saved trained models
├── templates/           # HTML templates for Flask
├── app.py               # Flask application
├── config.py            # Configuration settings
├── requirements.txt     # Dependencies
├── Dockerfile           # Docker setup
├── README.md            # Project documentation
└── .gitignore

````

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone https://github.com/KishoreAIML/Term-Deposit-Subscription-Prediction.git
cd Term-Deposit-Subscription-Prediction
````

### 2. Create Virtual Environment (Optional)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
python app.py
```

Open browser:

```
http://127.0.0.1:5000/
```

Enter customer details to get prediction.

---

## Docker (Optional)

Build image:

```bash
docker build -t term-deposit-app .
```

Run container:

```bash
docker run -p 5000:5000 term-deposit-app
```

---

## Exploratory Data Analysis (EDA)

* Class imbalance analysis
* Feature distribution
* Correlation analysis
* Customer behavior insights

---

## Model Deployment

* Flask-based web interface
* Real-time prediction
* User input form
* Model loaded from `models/` folder

---

## Key Insights

* Call duration strongly impacts subscription
* Previous campaign success increases probability
* Certain job and education groups show higher conversion
* Class imbalance handled for better recall

---

## Challenges Faced

* Handling imbalanced data
* Encoding multiple categorical features
* Avoiding data leakage
* Model selection and tuning
* Flask integration

---

## Future Improvements

* Add more models (XGBoost, CatBoost)
* Hyperparameter tuning
* Cloud deployment (AWS/Render)
* Add API endpoint
* Improve UI design

---

## Technologies Used

* Python
* Pandas, NumPy
* Scikit-learn
* LightGBM
* Matplotlib, Seaborn
* Flask
* Docker

---

## License

This project is licensed under the **MIT License**.

---

## Author

**Kishore Tirumani**

* GitHub: [https://github.com/KishoreAIML](https://github.com/KishoreAIML)
* LinkedIn: *(Add your LinkedIn here)*

---

## If you like this project

⭐ Star the repository
🍴 Fork it
📢 Share it

```

---

If you want, I can also give you:
- A **resume-ready project description**
- A **LinkedIn post for this project**
- A **professional GitHub portfolio README**
- A **live deployment guide (Render/Streamlit)**

This project is good for ML Engineer/Data Scientist profile — we can make it even stronger.
::contentReference[oaicite:1]{index=1}
```

[1]: https://github.com/KishoreAIML/Term-Deposit-Subscription-Prediction "GitHub - KishoreAIML/Term-Deposit-Subscription-Prediction: Machine Learning project to predict whether a client will subscribe to a term deposit using bank marketing data."

