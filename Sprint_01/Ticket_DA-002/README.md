# Ticket_DA-002 - Product Sales Performance

## Business Request
The Merchandising team needs to know which products generated the highest revenue.

## Input Files
- `datasets/raw/products.csv`
- `datasets/raw/orders.csv`
- `datasets/raw/order_items.csv`

## Deliverable
`output/product_sales_performance.csv`

## Tasks
1. Load products, orders and order_items.
2. Keep only completed orders.
3. Merge order_items with orders.
4. Merge the result with products.
5. Create net_amount using quantity, unit_price and discount_pct.
6. Group by product_id, product_name, category and subcategory.
7. Calculate units_sold, order_count and total_revenue.
8. Sort by total_revenue descending.
9. Export the result as output/product_sales_performance.csv.

## Acceptance Criteria
- The output has one row per product.
- Cancelled and returned orders are not included.
- Revenue uses discounts correctly.
- The report is sorted by total_revenue descending.

## Notes
Do not change files inside `datasets/raw/`. Save your result inside this ticket's `output/` folder.
