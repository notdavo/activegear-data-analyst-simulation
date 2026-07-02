# Ticket_DA-001 - Customer Revenue Summary

## Business Request
The Sales Manager needs a customer-level revenue report for completed orders.

## Input Files
- `datasets/raw/customers.csv`
- `datasets/raw/orders.csv`
- `datasets/raw/order_items.csv`

## Deliverable
`output/customer_revenue_summary.csv`

## Tasks
1. Load the required CSV files.
2. Inspect the datasets using basic Pandas methods.
3. Keep only orders with status equal to Completed.
4. Ignore order items where unit_price is 0.
5. Create a new column called gross_amount using quantity * unit_price.
6. Create a new column called net_amount after applying discount_pct.
7. Merge orders with customers using customer_id.
8. Group the data by customer_id, first_name, last_name, country and segment.
9. Calculate purchase_count, total_quantity and total_revenue.
10. Sort the report by total_revenue in descending order.
11. Export the final report as output/customer_revenue_summary.csv.

## Acceptance Criteria
- The output has one row per customer.
- Only completed orders are included.
- Zero-value order items are excluded.
- The file is sorted by total_revenue descending.
- The output CSV is saved in the ticket output folder.

## Notes
Do not change files inside `datasets/raw/`. Save your result inside `output/` folder.
