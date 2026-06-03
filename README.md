# Telecom Customer Churn Analysis & Prediction

## Project Overview
Built a machine learning model with 78.7% accuracy to predict customer churn.

## Business Problem
Company loses 26.54% of customers annually. Need to identify who will leave and why.

## Key Findings

**Finding 1: New Customers Leave Quickly**
- Customers who stayed: 37.6 months average
- Customers who churned: 18 months average
- Action: Focus retention on first 18 months

**Finding 2: Price Sensitivity**
- Churned customers: $74.44/month average
- Stayers: $61.27/month average
- Action: Offer loyalty discounts

**Finding 3: Fiber Optic is Broken**
- DSL: 19% churn
- Fiber optic: 42% churn (CRITICAL)
- No internet: 7% churn
- Action: Fix fiber optic service

**Finding 4: Protective Services Work**
- Tech support reduces churn
- Online security reduces churn
- Action: Bundle and promote these

## Model Performance
- Accuracy: 78.7%
- Precision: 62.8%
- Recall: 48.1%

## Recommendations

HIGH PRIORITY:
1. Fix Fiber Optic Service
2. Launch First 18-Month Program
3. Price Optimization for High-Spend Customers

MEDIUM PRIORITY:
4. Bundle Protective Services
5. Promote Tech Support & Security

Expected Impact: Save $2-5M annually through retention improvements

## Files
- notebooks/ - Analysis code
- results/visualizations/ - Charts
- data/raw/ - Customer data (7,043 records)

## Run It
pip install -r requirements.txt
jupyter notebook

Then run notebooks 01, 02, 03 in order.
