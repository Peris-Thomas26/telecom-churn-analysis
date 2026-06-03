# Telecom Customer Churn Analysis

## Background and Overview

Elist Electronics established in 2018 is a global e-commerce telecom company that sells popular electronic products worldwide via its website and mobile app. The company has significant amounts of data on its sales, marketing efforts, operational efficiency, product offerings, and loyalty program that has been previously underutilized.

This project thoroughly analyzes and synthesizes customer data to uncover critical insights that will improve customer retention and reduce annual churn losses.

**Project Goals:**
- Identify which customers are at risk of churning
- Understand the key drivers behind customer attrition
- Provide actionable recommendations to reduce churn and recover revenue

---

## Data Structure Overview

**Dataset:** IBM Telecom Customer Churn Dataset
- 7,043 customer records
- 21 features including billing, services, demographics, and churn status
- Time period: Historical snapshot (no time series)

**Key Tables/Variables:**
- Customer Demographics: gender, age, partner status, dependents
- Service Information: internet service type, online security, tech support, streaming services
- Billing Data: monthly charges, total charges, contract type
- Target Variable: Churn (Yes/No)

**Data Quality:** No missing values. All features complete and ready for analysis.

---

## Executive Summary

**Main Finding:**
The company loses 26.54% of its customers annually (1,869 out of 7,043). A predictive model identifies that new customers with high monthly bills on fiber optic service are at greatest risk. Early intervention during the first 18 months of customer tenure and service quality improvements for fiber optic users present significant opportunities to reduce churn and recover $2-5M in annual revenue.

**Key Metrics:**
- Model Accuracy: 78.7%
- Customers At Risk: 1,869 (26.54% of base)
- Potential Revenue Recovery: $2-5M annually
- Critical Issue: Fiber optic customers churn at 42% (vs 19% for DSL)

---

## Insights Deep Dive

### Insight 1: New Customers Leave Quickly

**Finding:**
Customers who churned averaged only 18 months with the company, while loyal customers averaged 37.6 months. This 2.1x difference shows that the first 18 months is the critical retention window.

**Business Impact:**
New customers represent a revenue leakage point. Without early intervention, roughly half of new customers are at risk.

**Recommendation:**
Assign dedicated account managers to new customers with monthly check-ins at months 6, 12, and 18.

---

### Insight 2: Price Sensitivity Drives Churn

**Finding:**
Customers who churned paid an average of $74.44 per month, while loyal customers paid $61.27. This 21% price difference indicates price sensitivity among at-risk customers.

**Business Impact:**
Higher-priced customer segments are more likely to explore competitors. Pricing power is limited without value-add services.

**Recommendation:**
Implement loyalty discounts (5-10%) for customers paying >$75/month and tenure-based pricing incentives.

---

### Insight 3: Fiber Optic Service Quality Crisis

**Finding:**
Fiber optic customers churn at 42%, compared to 19% for DSL and 7% for no internet service. This represents 2.2x higher attrition than the next best alternative.

**Business Impact:**
Fiber optic is the company's highest-value service but suffers from the worst retention. This is the single biggest revenue leak.

**Recommendation:**
Immediate service quality audit. Investigate speed, reliability, and support issues. Consider service guarantees or price adjustments if quality cannot be improved.

---

### Insight 4: Protective Services Reduce Churn

**Finding:**
Machine learning analysis shows that customers with tech support (4.0% importance) and online security (4.3% importance) have significantly lower churn rates. These services are protective factors.

**Business Impact:**
Add-on services increase customer engagement and switching costs, improving retention.

**Recommendation:**
Bundle protective services with fiber optic plans (offer 6 months free). Market these services to high-risk customer segments.

---

## Model Performance

**Accuracy: 78.7%** - The model correctly predicts customer outcomes 4 out of 5 times

**Precision: 62.8%** - When the model predicts churn, it is correct 62.8% of the time (low false alarms)

**Recall: 48.1%** - The model identifies about half of actual churners (conservative approach, appropriate for retention programs)

**Top Predictive Factors:**
1. Total Charges (18.9%) - Lifetime customer value
2. Tenure (16.4%) - How long they have been a customer
3. Monthly Charges (16.2%) - Monthly bill amount

---

## Business Recommendations

### URGENT PRIORITY

**1. Fix Fiber Optic Service Quality**
- Problem: 42% churn rate is unacceptable and unsustainable
- Action: Conduct service quality audit, survey customers on pain points
- Expected Impact: Reduce fiber churn from 42% to <25%

**2. Launch First 18-Month Success Program**
- Problem: New customers leave too quickly
- Action: Assign account managers, implement check-in schedule
- Expected Impact: Reduce early churn by 10-15%

**3. Implement Price Optimization**
- Problem: High-spend customers are price-sensitive
- Action: Loyalty discounts (5-10%) for customers >$75/month
- Expected Impact: Retain $1.5-2M in annual revenue

### IMPORTANT PRIORITY

**4. Bundle Protective Services with Fiber Optic**
- Action: Include 6 months free tech support and security with new fiber connections
- Expected Impact: Increase service adoption, improve retention

**5. Market Protective Services to At-Risk Segments**
- Action: Promote bundled packages to high-bill, new, and fiber optic customers
- Expected Impact: Improve loyalty across customer base

---

## Expected Business Impact (Year 1)

| Metric | Current | Target | Impact |
|--------|---------|--------|--------|
| Overall Churn Rate | 26.54% | <20% | Save $1.5M |
| Fiber Optic Churn | 42% | <25% | Save $1.5M |
| New Customer Retention | ~60% | 90% | Save $1M+ |
| **Total Revenue Recovery** | — | — | **$2-5M annually** |

---

## Caveats and Assumptions

**Data Limitations:**
- Analysis uses billing and service data only (no customer satisfaction scores)
- No support ticket or complaint history included
- Snapshot data without time series trends
- Does not account for competitive market activity

**Assumptions:**
- Historical patterns will continue into the future
- Churn reasons are primarily service and price related
- Recommended interventions will be executed with fidelity

**Recommended Next Steps:**
- Survey churned customers on actual reasons for leaving
- Analyze support tickets for complaint patterns
- Competitive market analysis on pricing and service
- Time-series analysis to identify seasonal churn patterns

---

## Technical Details

For code, notebooks, and visualizations, see:
- `notebooks/01_data_exploration.ipynb` - Data exploration and discovery
- `notebooks/02_data_cleaning.ipynb` - Data preparation
- `notebooks/03_churn_modeling.ipynb` - Model building and evaluation
- `results/visualizations/` - Charts and visualizations
- `INSIGHTS_AND_RECOMMENDATIONS.md` - Detailed analysis

---

## Files in This Project

All code is reproducible. To run:

```bash
pip install -r requirements.txt
jupyter notebook
```

Then execute notebooks 01, 02, 03 in order.

---

**Created for:** Portfolio demonstration of data analysis and business communication skills
