# Finance_Analysis
## Stock Return and Risk Analysis using CAPM

### 1. Objective
The objective of this project is to analyze stock returns and quantify risk using financial econometric methods.

Specifically, the project aims to:
- Calculate daily stock returns
- Analyze the distribution of returns
- Estimate CAPM beta using regression
- Decompose total variance into systematic and idiosyncratic risk

### 2. Data
Stock price data was collected using the Python library yfinance.
Assets analyzed:
- Apple (AAPL)
- Tesla (TSLA)
- Samsung Electronics
- SK Hynix

  Market benchmark
  - S&P 500 Index

  Period
  - 2023 ~ Present

### 3. Methodology
#### Return Calculation
Daily returns were calculated as :

$R_t = (P_t - P_{t-1}) / P_{t-1})$

#### CAPM Regression
We estimate the following regression model :

R_i = α + β R_m +  ε

Where:
- R_i : stock return
- R_m : market return
- β : sensitivity to market movements

#### Risk Decomposition
Total variance of a stock return can be decomposed as:

Var(R_i) = β^2Var(R_m) + Var(ε)

This allows us to spearate risk into:
- Systematic risk (market risk)
- Idiosyncratic risk (firm-specific risk)

### 4. Results
1) Return Distribution \
Daily returns are centered around zero but exhibit fat tails compared to a normal distribution. This suggests the presence of extreme market movements.
<img width="800" height="500" alt="Histogram of Apple Daily Returns" src="https://github.com/user-attachments/assets/f1e269a8-185f-4e19-a2ae-b0073f89b1a4" />

2) CAPM Regression \
The regression analysis estimates the beta coefficient, which measures how sensitive the stock is to market movements.
<img width="700" height="500" alt="Scatter plot and Regression line" src="https://github.com/user-attachments/assets/cc8f09d8-b43a-4e47-98de-d6ee91b3ef1e" />

3) Risk Decomposition \
The total variance of stock returns can be decomposed into market-driven risk firm-specific risk.
This analysis shows how much of the stock's volatility is explained by overall market movements.
<img width="600" height="600" alt="Risk Decomposition" src="https://github.com/user-attachments/assets/8a0ab263-c750-43f2-ba49-237487719d7d" />

### 5. Conclusion
The analysis shows that a significant portion of stock volatility can be explained by market movements.
However, a large share of variance remains idiosyncratic, reflecting firm-specific factors.
Understanding this decomposition is important for portfolio diversification and risk management.

















