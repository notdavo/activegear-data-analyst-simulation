# Data Dictionary

## customers.csv
Customer master data.

- `customer_id`: Unique customer identifier.
- `first_name`: Customer first name.
- `last_name`: Customer last name.
- `email`: Customer email address.
- `country`: Customer country.
- `city`: Customer city.
- `segment`: Customer segment.
- `signup_date`: Date when the customer registered.
- `active`: Whether the customer is active.

## products.csv
Product catalog.

- `product_id`: Unique product identifier.
- `product_name`: Product name.
- `category`: Main product category.
- `subcategory`: Product subcategory.
- `supplier_id`: Supplier identifier.
- `cost`: Product cost for the company.
- `list_price`: Standard selling price.
- `active`: Whether the product is currently active.

## orders.csv
Order header data.

- `order_id`: Unique order identifier.
- `customer_id`: Customer who placed the order.
- `store_id`: Store where the order was processed.
- `order_date`: Date of the order.
- `channel`: Sales channel.
- `payment_method`: Payment method.
- `status`: Order status.
- `campaign_id`: Related marketing campaign, if any.

## order_items.csv
Order line items.

- `order_item_id`: Unique order item identifier.
- `order_id`: Related order.
- `product_id`: Product sold.
- `quantity`: Quantity sold.
- `unit_price`: Unit selling price.
- `discount_pct`: Discount percentage applied.

## stores.csv
Store master data.

- `store_id`: Unique store identifier.
- `store_name`: Store name.
- `country`: Store country.
- `city`: Store city.
- `channel`: Retail, outlet or online.
- `opened_date`: Store opening date.
- `active`: Whether the store is active.

## inventory_snapshots.csv
Inventory levels by date, store and product.

- `snapshot_date`: Inventory snapshot date.
- `store_id`: Store identifier.
- `product_id`: Product identifier.
- `stock_on_hand`: Units available.
- `reorder_level`: Minimum desired stock level.
