"""
Ticket_DA-002 - Product Sales Performance

Write your solution here.
"""

from pathlib import Path
import pandas as pd

# Your code starts here

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = BASE_DIR / "datasets" / "raw"

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

products = pd.read_csv(RAW_DATA_DIR / "products.csv")
orders = pd.read_csv(RAW_DATA_DIR / "orders.csv")
order_items = pd.read_csv(RAW_DATA_DIR / "order_items.csv")

completed_orders = orders[orders["status"] == "Completed"].copy()

full_orders = completed_orders.merge(order_items, how="left", on="order_id").copy()

orders_with_products = full_orders.merge(products, how="left", on="product_id").copy()

orders_with_products["net_amount"] = (
    orders_with_products["quantity"]
    * orders_with_products["unit_price"]
    * (1 - orders_with_products["discount_pct"] / 100)
)

grouped_products = (
    orders_with_products.groupby(
        ["product_id", "product_name", "category", "subcategory"]
    )
    .agg(
        units_sold=("quantity", "sum"),
        order_count=("order_id", "nunique"),
        total_revenue=("net_amount", "sum"),
    )
    .reset_index()
    .sort_values(by="total_revenue", ascending=False)
)

output_file = OUTPUT_DIR / "product_sales_performance.csv"

grouped_products.to_csv(output_file, index=False)
