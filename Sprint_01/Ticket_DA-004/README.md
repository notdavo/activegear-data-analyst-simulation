# Ticket_DA-004 - Basic Data Quality Check

## Business Request
Before the next sprint, the Data team wants a basic quality check of the raw datasets.

## Input Files
- `datasets/raw/customers.csv`
- `datasets/raw/orders.csv`
- `datasets/raw/order_items.csv`
- `datasets/raw/products.csv`
- `datasets/raw/stores.csv`

## Deliverable
`output/data_quality_summary.csv`

## Tasks
1. Load the required CSV files.
2. For each dataset, calculate the number of rows and columns.
3. Count missing values per dataset.
4. Count duplicated rows per dataset.
5. Identify how many order records reference a customer_id that does not exist in customers.
6. Identify how many order records reference a store_id that does not exist in stores.
7. Identify how many order_items records reference a product_id that does not exist in products.
8. Create a summary table with dataset_name, row_count, column_count, missing_values, duplicate_rows and notes.
9. Export the summary as output/data_quality_summary.csv.

## Acceptance Criteria
- The output includes one row per dataset.
- Missing values and duplicate rows are counted.
- Invalid foreign keys are mentioned in the notes column.
- The output CSV is saved in the ticket output folder.

## Notes
Do not change files inside `datasets/raw/`. Save your result inside this ticket's `output/` folder.
