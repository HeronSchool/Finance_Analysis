import tkinter as tk
from tkinter import messagebox
import yfinance as yf
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# -----------------------------
# 분석 함수
# -----------------------------

def run_analysis():

    ticker = ticker_entry.get()
    start = start_entry.get()

    if ticker == "":
        messagebox.showerror("Error", "Enter a ticker")
        return

    stock = yf.download(ticker, start=start)
    market = yf.download("^GSPC", start=start)

    stock["Return"] = stock["Close"].pct_change()
    market["Return"] = market["Close"].pct_change()

    df = pd.concat([stock["Return"], market["Return"]], axis=1)
    df.columns = ["Stock", "Market"]
    df = df.dropna()

    # regression
    X = sm.add_constant(df["Market"])
    y = df["Stock"]

    model = sm.OLS(y, X).fit()

    beta = model.params["Market"]

    messagebox.showinfo("Result", f"Beta: {beta:.3f}")

    # regression plot
    plt.scatter(df["Market"], df["Stock"], alpha=0.5)

    x = df["Market"]
    y_line = model.params["const"] + beta * x

    plt.plot(x, y_line)

    plt.xlabel("Market Return")
    plt.ylabel("Stock Return")
    plt.title(f"{ticker} vs Market")

    plt.show()

# -----------------------------
# GUI
# -----------------------------

root = tk.Tk()
root.title("Stock Risk Analysis")

tk.Label(root, text="Ticker").grid(row=0, column=0)
ticker_entry = tk.Entry(root)
ticker_entry.grid(row=0, column=1)

tk.Label(root, text="Start Date (YYYY-MM-DD)").grid(row=1, column=0)
start_entry = tk.Entry(root)
start_entry.insert(0, "2023-01-01")
start_entry.grid(row=1, column=1)

run_button = tk.Button(root, text="Run Analysis", command=run_analysis)
run_button.grid(row=2, column=0, columnspan=2)

root.mainloop()