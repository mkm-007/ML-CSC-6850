# Weather Time Series Analysis and Forecasting

This repository contains the code and report for the Weather Time Series Analysis and Forecasting project using the Max Planck Institute dataset.

## Repository

https://github.com/hemanth1233333/weather-forecasting

## Usage

You can run the code in three different environments:
1. **Locally on your machine** (Jupyter Notebook)  
2. **Google Colab**  
3. **As a standalone Python script** (optional)

---

### 1. Running Locally (Jupyter Notebook)

1. **Clone the repository**  
   ```bash
   git clone https://github.com/hemanth1233333/weather-forecasting.git
   cd weather-forecasting
   ```

2. **Set up Python environment**  
   - *(Optional)* Create and activate a virtual environment:  
     ```bash
     python3 -m venv venv
     source venv/bin/activate      # On Windows: venv\Scripts\activate
     ```  
   - Install dependencies:  
     ```bash
     pip install -r requirements.txt
     ```  
     If `requirements.txt` is not provided, install manually:  
     ```bash
     pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow jupyter
     ```

3. **Launch Jupyter Notebook**  
   ```bash
   jupyter notebook
   ```  
4. Open `M.L_PROJECT_GROUP8_CODE.ipynb` and run all cells.

---

### 2. Running in Google Colab

1. Go to [Google Colab](https://colab.research.google.com).  
2. Click **File → Open notebook → GitHub**.  
3. Enter the repository URL:  
   ```
   https://github.com/hemanth1233333/weather-forecasting
   ```  
4. Select `M.L_PROJECT_GROUP8_CODE.ipynb`.  
5. Add a cell at the top to install dependencies:  
   ```python
   !pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow
   ```  
6. Run all cells.

---

### 3. Running as a Python Script (Optional)

1. Convert the notebook to a `.py` script:  
   ```bash
   jupyter nbconvert --to script M.L_PROJECT_GROUP8_CODE.ipynb
   ```  
2. Run the generated script:  
   ```bash
   python M.L_PROJECT_GROUP8_CODE.py
   ```

---

## Generating `requirements.txt`

If you install new packages or update versions, capture all dependencies with:
```bash
pip freeze > requirements.txt
```

---

## Contact

For questions or issues, reach out to **Hemanth Kumar Mulluri** at <hmulluri1@student.gsu.edu>.
