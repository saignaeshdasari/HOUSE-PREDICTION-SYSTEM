# 🏠 Bengaluru House Price Prediction System

A Machine Learning-based web application that predicts house prices in **Bengaluru** based on property-related inputs.

The project demonstrates an end-to-end Machine Learning workflow, including data analysis, model training, model serialization, and web-based prediction.

---

## 📌 Project Overview

The **Bengaluru House Price Prediction System** is designed to estimate the price of a property based on available housing information.

The project uses a **Linear Regression** machine learning model trained on Bengaluru housing data. The trained model is saved as `LinearRegression.pkl` and used by the Python application to generate price predictions.

The repository contains the model-training notebook, trained model, Python application, and HTML templates required for the prediction system.

---

## 🎯 Objectives

* Predict house prices based on property information.
* Apply Machine Learning to a real-world real-estate problem.
* Perform data preprocessing and analysis.
* Train a Linear Regression model.
* Save and reuse the trained ML model.
* Provide a web interface for obtaining predictions.

---

## ✨ Features

* 🏠 Bengaluru house-price prediction
* 🤖 Machine Learning-based prediction
* 📊 Data analysis using Jupyter Notebook
* 📈 Linear Regression model
* 💾 Pre-trained model using `LinearRegression.pkl`
* 🌐 Web-based prediction interface
* 🐍 Python-based implementation

---

## 🧠 Machine Learning Workflow

The project follows this workflow:

```text
Housing Dataset
      ↓
Data Preprocessing
      ↓
Exploratory Data Analysis
      ↓
Feature Selection
      ↓
Train-Test Split
      ↓
Linear Regression
      ↓
Model Evaluation
      ↓
Save Trained Model
      ↓
Web Application
      ↓
House Price Prediction
```

---

## 🛠️ Technologies Used

| Technology          | Purpose                             |
| ------------------- | ----------------------------------- |
| 🐍 Python           | Application and ML development      |
| 📊 Pandas           | Data manipulation                   |
| 🔢 NumPy            | Numerical operations                |
| 🤖 Scikit-learn     | Machine Learning                    |
| 📓 Jupyter Notebook | Data analysis and model development |
| 🌐 HTML             | Web interface                       |
| 🧩 Flask            | Python web application              |
| 💾 Pickle           | Saving/loading the trained model    |

> The repository currently contains `Houseprice.ipynb`, `main.py`, `LinearRegression.pkl`, and a `templates` directory.

---

## 📂 Project Structure

```text
HOUSE-PREDICTION-SYSTEM/
│
├── templates/
│   └── HTML template files
│
├── Houseprice.ipynb
│   └── Data analysis and ML model development
│
├── LinearRegression.pkl
│   └── Trained Linear Regression model
│
├── main.py
│   └── Web application
│
├── .gitignore
├── .hintrc
└── README.md
```

---

## ⚙️ How It Works

### 1. Data Analysis

The housing dataset is analyzed using Python and Jupyter Notebook.

The notebook is used for:

* Understanding the dataset
* Data cleaning
* Feature preparation
* Exploratory analysis
* Model development

---

### 2. Model Training

A **Linear Regression** model is trained using the available housing data.

The basic idea is:

```text
Property Features
       ↓
Linear Regression Model
       ↓
Predicted House Price
```

---

### 3. Model Serialization

After training, the model is saved as:

```text
LinearRegression.pkl
```

This allows the trained model to be loaded later without training it again.

---

### 4. Web Application

`main.py` handles the Python web application.

The user provides property information through the web interface, and the trained model generates the predicted house price.

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/saignaeshdasari/HOUSE-PREDICTION-SYSTEM.git
```

### Step 2: Open the Project

```bash
cd HOUSE-PREDICTION-SYSTEM
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

---

### Step 4: Install Required Libraries

```bash
pip install pandas numpy scikit-learn flask jupyter
```

---

### Step 5: Run the Application

```bash
python main.py
```

Then open the local URL displayed by Flask in your browser.

---

## 🧪 Model

### Algorithm

```text
Linear Regression
```

### Problem Type

```text
Supervised Learning
Regression
```

### Target

```text
House Price
```

The model learns the relationship between property features and house prices and then uses that relationship to estimate prices for new inputs.

---

## 📊 Example Workflow

A user enters property information such as:

```text
Location
Area
Number of Bedrooms
Other Property Features
```

The application processes the input:

```text
User Input
    ↓
Data Processing
    ↓
Linear Regression Model
    ↓
Predicted Price
```

Example output:

```text
Estimated House Price: ₹XX Lakhs
```

---

## 🌟 Key Learning Outcomes

This project helped demonstrate practical experience with:

* Machine Learning fundamentals
* Regression algorithms
* Data preprocessing
* Exploratory Data Analysis
* Python programming
* Model serialization
* Flask web applications
* Integrating ML models with web interfaces

---

## 🔮 Future Enhancements

The project can be improved by adding:

* 📈 Model accuracy and evaluation metrics
* 🔄 Comparison of Linear Regression, Ridge, Lasso and Random Forest
* 🗺️ Location-based visualization
* 📊 Interactive price analytics
* 🎨 Improved responsive UI
* 🧹 Advanced feature engineering
* ☁️ Cloud deployment
* 🔐 User authentication
* 📱 Mobile-friendly interface
* 💡 Price range and confidence estimation

---

## 💼 Project Highlights

**Project:** Bengaluru House Price Prediction System

**Domain:** Machine Learning / Real Estate

**Type:** Regression

**Model:** Linear Regression

**Application:** Web-based House Price Prediction

**Location:** Bengaluru, India

---

## 👨‍💻 Author

**Saignaesh Dasari**

GitHub:
[github.com/saignaeshdasari](https://github.com/saignaeshdasari?utm_source=chatgpt.com)

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
