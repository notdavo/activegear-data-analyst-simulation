# Ticket_DA-003 - Store Daily Sales Report

## Business Request
The Operations team needs a daily sales report by store.

## Input Files
- `datasets/raw/stores.csv`
- `datasets/raw/orders.csv`
- `datasets/raw/order_items.csv`

## Deliverable
`output/store_daily_sales.csv`

## Tasks
1. Load stores, orders and order_items.
2. Keep only completed orders.
3. Create net_amount using quantity, unit_price and discount_pct.
4. Merge order_items with orders.
5. Merge the result with stores.
6. Group by order_date, store_id, store_name, country and city.
7. Calculate total_orders, total_items_sold and total_revenue.
8. Sort by order_date ascending and total_revenue descending.
9. Export the result as output/store_daily_sales.csv.

## Acceptance Criteria
- The output has one row per store per day.
- Only completed orders are included.
- The report includes store name and location.
- The output file is saved correctly.

## Notes
Do not change files inside `datasets/raw/`. Save your result inside this ticket's `output/` folder.
