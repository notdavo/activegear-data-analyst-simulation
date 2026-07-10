"""
Ticket_DA-003 - Store Daily Sales Report

Write your solution here.
"""

from pathlib import Path
import pandas as pd

# Your code starts here

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = BASE_DIR / "datasets" / "raw"

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data():
    stores = pd.read_csv(RAW_DATA_DIR / "stores.csv")
    orders = pd.read_csv(RAW_DATA_DIR / "orders.csv")
    order_items = pd.read_csv(RAW_DATA_DIR / "order_items.csv")
    return stores, orders, order_items


def prepare_orders(orders):
    completed_orders = orders[orders["status"] == "Completed"].copy()
    return completed_orders


def prepare_order_items(order_items):
    prepared_items = order_items.copy()

    prepared_items["net_amount"] = (
        prepared_items["quantity"]
        * prepared_items["unit_price"]
        * (1 - prepared_items["discount_pct"] / 100)
    )

    return prepared_items


def create_customer_report(order_items, completed_orders, stores):
    orders_with_items = order_items.merge(completed_orders, how="left", on="order_id")
    orders_with_items_stores = orders_with_items.merge(
        stores, how="left", on="store_id"
    )

    grouped_order_full_data = (
        orders_with_items_stores.groupby(
            ["order_date", "store_id", "store_name", "country", "city"]
        )
        .agg(
            total_orders=("order_id", "nunique"),
            total_items_sold=("quantity", "sum"),
            total_revenue=("net_amount", "sum"),
        )
        .reset_index()
        .sort_values(["order_date", "total_revenue"], ascending=[True, False])
    )

    return grouped_order_full_data


def export_report(report):
    output_file = OUTPUT_DIR / "store_daily_sales.csv"
    report.to_csv(output_file, index=False)


def main():
    stores, orders, order_items = load_data()

    completed_orders = prepare_orders(orders)

    prepared_items = prepare_order_items(order_items)

    report = create_customer_report(prepared_items, completed_orders, stores)

    export_report(report)


if __name__ == "__main__":
    main()
