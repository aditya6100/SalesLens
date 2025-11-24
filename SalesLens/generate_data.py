import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Configuration
num_records = 1000
start_date = datetime(2022, 1, 1)
end_date = datetime(2023, 12, 31)

# Data generation lists
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego"]
categories = ["Electronics", "Apparel", "Home Goods", "Books", "Toys"]
products = {
    "Electronics": ["Laptop", "Smartphone", "Headphones", "Smartwatch"],
    "Apparel": ["T-Shirt", "Jeans", "Jacket", "Sneakers"],
    "Home Goods": ["Coffee Maker", "Blender", "Lamps", "Towels"],
    "Books": ["Fiction Novel", "Cookbook", "History Book", "Sci-Fi Classic"],
    "Toys": ["Action Figure", "Board Game", "Lego Set", "RC Car"]
}
payment_modes = ["Credit Card", "Debit Card", "PayPal", "Cash on Delivery"]

# Generate data
data = []
for i in range(num_records):
    order_date = start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    category = random.choice(categories)
    product = random.choice(products[category])
    
    data.append({
        "order_id": 1001 + i,
        "order_date": order_date.strftime('%Y-%m-%d'),
        "customer_id": random.randint(101, 200),
        "city": random.choice(cities),
        "category": category,
        "product": product,
        "quantity": random.randint(1, 5),
        "price": round(random.uniform(20.0, 500.0), 2),
        "discount": round(random.uniform(0.0, 0.2), 2),
        "payment_mode": random.choice(payment_modes)
    })

# Create DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv("SalesLens/sales_data.csv", index=False)

print("sales_data.csv generated successfully.")
