### **Gold Price Prediction using Machine Learning**  

📌 **Overview**  
This project predicts **gold prices (GLD)** using a **Random Forest Regressor**. The model is trained on historical financial data and evaluates its accuracy using **R² Score**.  

📌 **Dataset**  
The dataset contains historical prices of **gold (GLD), silver (SLV), oil (USO), stock market index (SPX), and EUR/USD exchange rate**. The features used for prediction include:  
- **SPX** → S&P 500 Index  
- **USO** → Crude Oil Prices  
- **SLV** → Silver Prices  
- **EUR/USD** → Exchange Rate  

📌 **Libraries Used**  
- `pandas` → Data handling  
- `numpy` → Numerical calculations  
- `matplotlib & seaborn` → Data visualization  
- `sklearn` → Machine learning model & metrics  

📌 **Implementation Steps**  
1. **Load Data**: Read the dataset using `pandas`.  
2. **Data Exploration**: Check for missing values, summary statistics, and feature correlations.  
3. **Data Visualization**: Plot correlation heatmaps and distribution plots for insights.  
4. **Data Preprocessing**: Split the dataset into **features (X)** and **target (Y)**.  
5. **Model Training**: Train a **RandomForestRegressor** with 100 estimators.  
6. **Model Evaluation**: Calculate **R² Score** to measure prediction accuracy.  
7. **Prediction Visualization**: Compare **actual vs. predicted prices** using line plots.  



📌 **Results**  
- The **R² score** indicates how well the model fits the data (closer to 1 is better).  
- The model shows a **strong correlation** between **gold prices and silver prices (SLV)**.  


📌 **Future Improvements**  
✅ Use more advanced models like **XGBoost** or **LSTMs**.  
✅ Add external factors like **inflation rates** and **interest rates** for better predictions.  
✅ Deploy the model using **Flask or Streamlit**.  

📌 **Contributing**  
Feel free to fork this repository and contribute! 🚀  
