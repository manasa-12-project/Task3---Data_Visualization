"""
CodeAlpha - Task 3: Data Visualization
Turns the book data (from Task 1) and the EDA findings (from Task 2) into
clear, portfolio-ready charts using Matplotlib and Seaborn.

Run locally (place Data.csv):
    pip install pandas matplotlib seaborn
    python Data Visual .py
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set_style("whitegrid")
sns.set_palette("Set2")

OUTPUT_DIR = "charts"


def load_data(path: str = "Data.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded {len(df)} rows for visualization\n")
    return df


def price_distribution(df: pd.DataFrame) -> None:
    """Histogram showing how book prices are spread out."""
    plt.figure(figsize=(8, 5))
    sns.histplot(df["price_gbp"], bins=20, kde=True, color="#4C72B0")
    plt.title("Distribution of Book Prices")
    plt.xlabel("Price (£)")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/price_distribution.png", dpi=150)
    plt.close()
    print("Saved: price_distribution.png")


def avg_price_by_rating(df: pd.DataFrame) -> None:
    """Bar chart of average price per star rating."""
    avg_price = df.groupby("rating")["price_gbp"].mean().reset_index()

    plt.figure(figsize=(8, 5))
    sns.barplot(data=avg_price, x="rating", y="price_gbp", hue="rating",
                legend=False, palette="Blues_d")
    plt.title("Average Book Price by Star Rating")
    plt.xlabel("Star Rating")
    plt.ylabel("Average Price (£)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/avg_price_by_rating.png", dpi=150)
    plt.close()
    print("Saved: avg_price_by_rating.png")


def rating_counts(df: pd.DataFrame) -> None:
    """How many books fall into each star rating."""
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x="rating", hue="rating", legend=False,
                  palette="Greens_d")
    plt.title("Number of Books by Star Rating")
    plt.xlabel("Star Rating")
    plt.ylabel("Number of Books")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/rating_counts.png", dpi=150)
    plt.close()
    print("Saved: rating_counts.png")


def stock_breakdown(df: pd.DataFrame) -> None:
    """Pie chart of in-stock vs out-of-stock books."""
    counts = df["in_stock"].value_counts()
    labels = ["In Stock" if v else "Out of Stock" for v in counts.index]

    plt.figure(figsize=(6, 6))
    plt.pie(counts.values, labels=labels, autopct="%1.1f%%",
            colors=["#55A868", "#C44E52"], startangle=90)
    plt.title("Stock Availability")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/stock_breakdown.png", dpi=150)
    plt.close()
    print("Saved: stock_breakdown.png")


def price_by_stock_status(df: pd.DataFrame) -> None:
    """Boxplot comparing price spread for in-stock vs out-of-stock books."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=df, x="in_stock", y="price_gbp", hue="in_stock",
                legend=False, palette="Set2")
    plt.title("Price Spread: In Stock vs Out of Stock")
    plt.xlabel("In Stock")
    plt.ylabel("Price (£)")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/price_by_stock_status.png", dpi=150)
    plt.close()
    print("Saved: price_by_stock_status.png")


if __name__ == "__main__":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    df = load_data()

    price_distribution(df)
    avg_price_by_rating(df)
    rating_counts(df)
    stock_breakdown(df)
    price_by_stock_status(df)

    print(f"\nAll charts saved to the '{OUTPUT_DIR}/' folder.")