import pandas as pd
import numpy as np

# =========================================================
# 1. LOAD DATA
# =========================================================

file_path = r"C:\Users\GOPIKA\Downloads\events.csv\events.csv"

df = pd.read_csv(file_path)

print("Original Shape:", df.shape)

# Convert event_time to datetime
df["event_time"] = pd.to_datetime(df["event_time"], errors="coerce")

# =========================================================
# 2. DATA QUALITY CHECK
# =========================================================

print("\n================ DATA QUALITY ================")

print("\nMissing Values:")
print(df.isna().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nEvent Types:")
print(df["event_type"].value_counts())

print("\nInvalid Prices:")
print((df["price"] <= 0).sum())

print("\nMissing User IDs:")
print(df["user_id"].isna().sum())

print("\nMissing Timestamps:")
print(df["event_time"].isna().sum())

# =========================================================
# 3. REMOVE EXACT DUPLICATES
# =========================================================

df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)

# =========================================================
# 4. HANDLE MISSING VALUES FOR ANALYSIS
# =========================================================

# Keep original columns unchanged.
# Create separate analysis columns.

df["brand_analysis"] = df["brand"].fillna("Unknown")
df["category_analysis"] = df["category_code"].fillna("Unknown")

# =========================================================
# 5. BASIC DATA OVERVIEW
# =========================================================

print("\n================ BASIC OVERVIEW ================")

print("Unique Users:", df["user_id"].nunique())
print("Unique Sessions:", df["user_session"].nunique())
print("Unique Products:", df["product_id"].nunique())
print("Unique Categories:", df["category_analysis"].nunique())

print("\nDate Range:")
print("Start:", df["event_time"].min())
print("End:", df["event_time"].max())

# =========================================================
# 6. BUSINESS KPIs
# =========================================================

purchases = df[df["event_type"] == "purchase"]

total_purchase_events = len(purchases)
total_revenue = purchases["price"].sum()
average_purchase_value = purchases["price"].mean()
unique_buyers = purchases["user_id"].nunique()

print("\n================ BUSINESS KPIs ================")

print("Total Purchase Events:", total_purchase_events)
print("Total Revenue:", round(total_revenue, 2))
print("Average Purchase Value:", round(average_purchase_value, 2))
print("Unique Buyers:", unique_buyers)

# =========================================================
# 7. BASIC USER FUNNEL
# =========================================================

view_users = df.loc[
    df["event_type"] == "view", "user_id"
].nunique()

cart_users = df.loc[
    df["event_type"] == "cart", "user_id"
].nunique()

purchase_users = df.loc[
    df["event_type"] == "purchase", "user_id"
].nunique()

view_to_cart = cart_users / view_users * 100
cart_to_purchase = purchase_users / cart_users * 100
view_to_purchase = purchase_users / view_users * 100

print("\n================ FUNNEL ================")

print("View Users:", view_users)
print("Cart Users:", cart_users)
print("Purchase Users:", purchase_users)

print("View → Cart:", round(view_to_cart, 2), "%")
print("Cart → Purchase:", round(cart_to_purchase, 2), "%")
print("View → Purchase:", round(view_to_purchase, 2), "%")

# =========================================================
# 8. CATEGORY PERFORMANCE
# =========================================================

category_data = df.groupby("category_analysis").agg(
    views=("event_type", lambda x: (x == "view").sum()),
    carts=("event_type", lambda x: (x == "cart").sum()),
    purchases=("event_type", lambda x: (x == "purchase").sum())
).reset_index()

# Conversion rates
category_data["view_to_cart_rate"] = np.where(
    category_data["views"] > 0,
    category_data["carts"] / category_data["views"] * 100,
    0
)

category_data["cart_to_purchase_rate"] = np.where(
    category_data["carts"] > 0,
    category_data["purchases"] / category_data["carts"] * 100,
    0
)

category_data["view_to_purchase_rate"] = np.where(
    category_data["views"] > 0,
    category_data["purchases"] / category_data["views"] * 100,
    0
)

print("\n================ TOP CATEGORIES BY VIEWS ================")

print(
    category_data
    .sort_values("views", ascending=False)
    .head(10)
    .to_string(index=False)
)

# =========================================================
# 9. CATEGORIES NEEDING ATTENTION
# =========================================================

category_attention = (
    category_data[
        (category_data["views"] >= 10000) &
        (category_data["purchases"] > 0)
    ]
    .sort_values("view_to_purchase_rate")
)

print("\n================ LOW-CONVERSION CATEGORIES ================")

print(
    category_attention
    .head(10)
    .to_string(index=False)
)

# =========================================================
# 10. CATEGORY REVENUE
# =========================================================

category_revenue = (
    purchases
    .assign(category_analysis=purchases["category_code"].fillna("Unknown"))
    .groupby("category_analysis")
    .agg(
        purchases=("product_id", "count"),
        revenue=("price", "sum")
    )
    .reset_index()
    .sort_values("revenue", ascending=False)
)

print("\n================ TOP CATEGORIES BY REVENUE ================")

print(
    category_revenue.head(10).to_string(index=False)
)

# =========================================================
# 11. TOP PRODUCTS BY VIEWS
# =========================================================

product_views = (
    df[df["event_type"] == "view"]
    .groupby(["product_id", "category_analysis"])
    .size()
    .reset_index(name="views")
    .sort_values("views", ascending=False)
)

print("\n================ TOP PRODUCTS BY VIEWS ================")

print(product_views.head(10).to_string(index=False))

# =========================================================
# 12. TOP PRODUCTS BY PURCHASES
# =========================================================

product_purchases = (
    purchases
    .groupby(["product_id", "category_analysis"])
    .agg(
        purchases=("product_id", "count"),
        revenue=("price", "sum")
    )
    .reset_index()
    .sort_values("purchases", ascending=False)
)

print("\n================ TOP PRODUCTS BY PURCHASES ================")

print(product_purchases.head(10).to_string(index=False))

# =========================================================
# 13. MONTHLY PERFORMANCE
# =========================================================
df["month"] = df["event_time"].dt.tz_localize(None).dt.to_period("M")
df["month_name"] = df["event_time"].dt.strftime("%b")
df["month_order"] = (
    (df["event_time"].dt.year - df["event_time"].dt.year.min()) * 12
    + df["event_time"].dt.month
)
monthly_data = df.groupby("month").agg(
    views=("event_type", lambda x: (x == "view").sum()),
    carts=("event_type", lambda x: (x == "cart").sum()),
    purchases=("event_type", lambda x: (x == "purchase").sum())
).reset_index()

monthly_data["revenue"] = (
    df[df["event_type"] == "purchase"]
    .groupby(df.loc[df["event_type"] == "purchase", "month"])["price"]
    .sum()
    .reindex(monthly_data["month"])
    .fillna(0)
    .values
)

monthly_data["view_to_purchase_rate"] = np.where(
    monthly_data["views"] > 0,
    monthly_data["purchases"] / monthly_data["views"] * 100,
    0
)

print("\n================ MONTHLY PERFORMANCE ================")

print(monthly_data.to_string(index=False))

# =========================================================
# 14. BRAND PERFORMANCE
# =========================================================

brand_data = df.groupby("brand_analysis").agg(
    views=("event_type", lambda x: (x == "view").sum()),
    carts=("event_type", lambda x: (x == "cart").sum()),
    purchases=("event_type", lambda x: (x == "purchase").sum())
).reset_index()

brand_data["view_to_purchase_rate"] = np.where(
    brand_data["views"] > 0,
    brand_data["purchases"] / brand_data["views"] * 100,
    0
)

print("\n================ TOP BRANDS BY VIEWS ================")

print(
    brand_data
    .sort_values("views", ascending=False)
    .head(10)
    .to_string(index=False)
)

# =========================================================
# 15. SAVE ANALYSIS TABLES
# =========================================================

category_data.to_csv("category_analysis.csv", index=False)
category_revenue.to_csv("category_revenue.csv", index=False)
product_views.to_csv("product_views.csv", index=False)
product_purchases.to_csv("product_purchases.csv", index=False)
monthly_data.to_csv("monthly_analysis.csv", index=False)
brand_data.to_csv("brand_analysis.csv", index=False)

print("\n================ DONE ================")
print("Analysis tables saved successfully.")


# Save cleaned dataset
df.to_csv(
    r"C:\Users\GOPIKA\Downloads\events_cleaned.csv",
    index=False
)

print("Cleaned dataset saved successfully!")
