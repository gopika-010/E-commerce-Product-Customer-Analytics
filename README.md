# E-commerce-Product-Customer-Analytics

## 📊 Project Overview

This project focuses on analyzing e-commerce customer behavior and product performance using **Python and Power BI**.

The objective is to understand how users interact with products, identify drop-offs in the customer journey, analyze category, product and brand performance, and track business trends over time.

The project follows a complete Data Analyst workflow:

**Data Cleaning → Exploratory Data Analysis → KPI Analysis → Funnel Analysis → Business Insights → Dashboard**

---

## 🎯 Objectives

- Analyze customer interaction with products.
- Understand the View → Cart → Purchase journey.
- Measure conversion rates at different stages.
- Identify high- and low-performing product categories.
- Analyze product and brand revenue performance.
- Track revenue, purchases and active users over time.
- Generate actionable business insights.

---

## 🗂️ Dataset

The dataset contains approximately **885K e-commerce event records**.

Key columns include:

- `event_time` – Timestamp of the event
- `event_type` – View, Cart or Purchase
- `product_id` – Product identifier
- `category_id` – Category identifier
- `category_code` – Product category
- `brand` – Product brand
- `price` – Product price
- `user_id` – User identifier
- `user_session` – User session identifier

The original dataset is not included in this repository because of its large file size.

---

## 🛠️ Tools & Technologies

- **Python**
- **Pandas**
- **NumPy**
- **Power BI**
- **DAX**
- **Microsoft Excel** for supporting data work

---

## 🧹 Data Cleaning & Preparation

Python and Pandas were used to prepare the dataset for analysis.

The main preprocessing steps included:

- Checked and handled missing values.
- Identified and reviewed duplicate records.
- Checked data types.
- Converted event timestamps into datetime format.
- Validated price values.
- Created analysis fields for category and brand.
- Created monthly fields for trend analysis.
- Prepared the cleaned data for Power BI.

---

## 📈 Key Analysis

The project includes analysis of:

### Customer Funnel
- View Users
- Cart Users
- Purchase Users
- View-to-Cart Conversion
- Cart-to-Purchase Conversion
- View-to-Purchase Conversion

### Category Analysis
- Category Views vs Purchases
- Category Conversion Rate
- Revenue by Category

### Product & Brand Analysis
- Top 10 Products by Revenue
- Top 10 Brands by Revenue

### Time-Based Analysis
- Monthly Revenue
- Monthly Purchases
- Monthly Active Users
- Monthly View-to-Purchase Conversion

---

## 📊 Power BI Dashboard

The Power BI dashboard is organized into four pages.

### Page 1 — Business Overview

Provides a high-level view of business performance using:

- Total Users
- Total Purchases
- Total Revenue
- Average Purchase Value
- Monthly Revenue Trend
- Category Views vs Purchases

### Page 2 — Funnel & Conversion Analysis

Focuses on the customer journey:

**View → Cart → Purchase**

Includes:

- View Users
- Cart Users
- Purchase Users
- User Purchase Funnel
- View-to-Cart Conversion
- Cart-to-Purchase Conversion
- View-to-Purchase Conversion

### Page 3 — Category & Product Analysis

Provides deeper performance analysis across:

- Category Conversion Rate
- Revenue by Category
- Top 10 Products by Revenue
- Top 10 Brands by Revenue

### Page 4 — Trends & Customer Behavior

Tracks changes over time using:

- Monthly Revenue Trend
- Monthly Purchase Trend
- Monthly Active Users
- Monthly View-to-Purchase Conversion

---

## 🔍 Key Findings

- The dataset contains approximately **885K event records**.
- The analysis identified approximately **407K unique users**.
- There were **37,346 purchase events**.
- Total purchase revenue was approximately **5.13M**.
- Average purchase value was approximately **137.24**.
- **View-to-Cart conversion was 9.08%**, indicating a significant drop between product viewing and cart addition.
- **Cart-to-Purchase conversion was 57.65%**, showing substantially stronger movement after users reached the cart stage.
- Overall **View-to-Purchase conversion was 5.24%**.
- Conversion performance varied considerably across product categories.
- Monthly revenue, purchases and user activity changed over the observed period.

---

## 💡 Business Recommendations

Based on the analysis:

1. Investigate the low **View-to-Cart conversion** to understand why many users do not add viewed products to their carts.
2. Review product page quality, pricing, offers, product information and assortment for low-converting categories.
3. Monitor high-performing categories and brands to identify opportunities for targeted promotions.
4. Track monthly conversion and revenue trends to identify changes in customer behavior.
5. Use category and product-level analysis to support better merchandising and marketing decisions.

---

## 📁 Project Structure

```text
E-commerce-Product-Customer-Analytics/
│
├── events_analysis.py
├── README.md
└── screenshots/
    ├── page1-overview.png
    ├── page2-funnel.png
    ├── page3-category-product.png
    └── page4-trends.png
