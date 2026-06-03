# Telecom Customer Churn Analysis

## Background and Overview

Elist Electronics, established in 2018, is a global e-commerce telecom company selling popular electronics worldwide. The company loses 26.54% of customers annually. This project identifies which customers will churn and why, enabling targeted retention strategies worth $2-5M in annual revenue recovery.

---

## Data Structure Overview

Dataset: IBM Telecom Customer Churn | Records: 7,043 customers | Features: 21 variables

---

## Executive Summary

Key Finding: Customers in their first 18 months, with high monthly bills, and on fiber optic service are at greatest churn risk.

Model Performance: 78.7% accuracy | Revenue Opportunity: $2-5M annually

---

## Insights Deep Dive

### 1. New Customers Leave Too Quickly
Churned customers: 18 months avg | Loyal customers: 37.6 months avg

### 2. Price Sensitivity
Churned customers pay $74.44/month vs $61.27 for stayers (21% higher)

### 3. Fiber Optic Crisis  
Fiber optic churn: 42% | DSL churn: 19% | No internet: 7%


### 4. Protective Services Reduce Churn
Tech support and online security show 30%+ lower churn


---

## Recommendations

1. Fix fiber optic service (42% churn)
2. Launch first 18-month success program
3. Price optimization for high-spend customers


Expected Impact: Reduce churn 26.5% to <20% = $2-5M recovered

---

## Technical Details

Notebooks: 01_data_exploration, 02_data_cleaning, 03_churn_modeling

To run: pip install -r requirements.txt && jupyter notebook
