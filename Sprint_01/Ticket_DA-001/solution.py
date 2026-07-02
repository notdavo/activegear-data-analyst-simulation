"""
Ticket_DA-001 - Customer Revenue Summary

Write your solution here.
"""
from pathlib import Path
import pandas as pd

# Your code starts here

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = BASE_DIR / "datasets" / "raw"

OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)

customers = pd.read_csv(RAW_DATA_DIR / "customers.csv")
orders = pd.read_csv(RAW_DATA_DIR / "orders.csv")
order_items = pd.read_csv(RAW_DATA_DIR / "order_items.csv")

completed_orders = orders[orders['status'] == 'Completed'].copy()

valid_items = order_items[order_items['unit_price'] != 0].copy()

valid_items['gross_amount'] = (valid_items['quantity'] * valid_items['unit_price'])

valid_items['net_amount'] = (valid_items['gross_amount'] * (1 - valid_items['discount_pct']))

orders_by_customers = completed_orders.merge(customers, how='left', on='customer_id')

final_dataframe = orders_by_customers.merge(valid_items, how='left', on='order_id')

grouped_customer = final_dataframe.groupby(['customer_id', 'first_name', 'last_name', 'country', 'segment']).agg(purchase_count = ('order_id', 'nunique'), total_quantity = ('quantity', 'sum'), total_revenue = ('net_amount','sum')).reset_index()

grouped_customer.sort_values(by='total_revenue', ascending=False)

output_file = OUTPUT_DIR / "customer_revenue_summary.csv"

grouped_customer.to_csv(output_file, index=False)


