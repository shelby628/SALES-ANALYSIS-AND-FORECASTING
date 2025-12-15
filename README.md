
# PART 1
# Sales Analysis 


## Table of Contents
1. [Overview](#overview)
2. [Data Sources](#data-sources)
3. [Tools Used](#tools-used)
4. [Process](#process)
5.  [QUESTIONS (KPI)](#QUESTIONS (KPI))
6. [Key Insights](#key-insights)
7. [Visualizations](#visualizations)
8. [Conclusion](#conclusion)
9. [Author](#author)
   




## Overview / Objectives
This project analyzes inventory, sales, and purchase data to support business decisions, identify trends, and improve operational efficiency. Insights from this analysis help optimize stock management, vendor performance, and overall sales strategy.
## Data Sources
- `Dataset` —   - Sales, Inventory, and Purchases CSV files provided by the companyhelp m 
-
## Tools Used
- Python (Jupyter Notebook)
- Python (script)
- Power BI for dashboards and KPI visualization

  
  
  
  ##  Process
Data Cleaning – handled missing values and removed duplicates

Exploratory Data Analysis (EDA) – analyzed distributions, correlations, and outliers

Visualization – built KPI dashboards and charts in Power BI

Reporting – summarized findings to support decision making

  Key Questions (KPI)

1.Who are the top ten vendors by total sales?

2.Which brands are underperforming and require promotional adjustments?

3.What are the reasons behind underperformance?

4.How can inventory turnover be optimized to reduce holding costs?

5.What is the impact of bulk purchasing on unit costs?

6.How does profitability vary between high-performing and low-performing vendors?

7.How much of total procurement is dependent on top vendors?

 ## Key Insights
1.Many brands sell in low quantities due to poor customer demand.

2.Most underperforming brands occupy inventory space unnecessarily; reducing their stock can improve efficiency.

3.High-performing items maintain steady sales even at low stock levels, while some overstocked items drive unnecessary costs.

4.High-performing vendors maintain stable profit margins; low-performing vendors show unpredictable margins, posing risk.

5.Although low-performing vendors have higher median profits, high-performing vendors are more consistent and reliable. <br> <br> <br>

## Visualizations


A bar chart showing units sold against Brand

<img width="854" height="367" alt="image" src="https://github.com/user-attachments/assets/c0839745-4238-4ff3-b242-8550eff67e6c" /><br>
---
This scatter plot illustrates the relationship between average inventory levels and inventory turnover across all items.

<img width="702" height="365" alt="image" src="https://github.com/user-attachments/assets/1d01b6fe-17e5-43ed-9852-e11e5f495592" /><br>
The visualization shows a strong concentration of items with high average inventory but very low turnover, indicating excess stock that is not converting into sales. Slow-moving goods are clustered near the lower turnover region, confirming that these items contribute significantly to inventory holding costs without generating proportional revenue.
---
This box plot compares profit margin distributions between high-performing vendors and low-performing vendors.

<img width="482" height="331" alt="image" src="https://github.com/user-attachments/assets/a1aa210d-b66c-4e7d-86ce-10645222f2b6" /><br>

High-performing vendors demonstrate reliability in profit margins, whereas low-performing vendors show unpredictable results, with both very low and very high extremes.<br>

This suggests that vendor reliability is driven not only by profitability but also by margin stability, making high-performing vendors more dependable for long-term procurement strategies.
---

<img width="734" height="359" alt="image" src="https://github.com/user-attachments/assets/fd943e66-dd67-4c26-a9d6-53e809426b9a" /><br>
Sales initially experienced a sharp decline, but later stabilized and began following a consistent weekly seasonal pattern. The forecast indicates that sales will remain steady with regular fluctuations, though long-term uncertainty increases.<br>
---

<img width="816" height="365" alt="image" src="https://github.com/user-attachments/assets/e01e370b-75df-44c8-b9af-99692ca456ff" /><br>
Dashboard <br>
<img width="595" height="338" alt="image" src="https://github.com/user-attachments/assets/8911dba1-7bf1-4dc1-8460-14ceaf92c98a" />

 # PART 2  PREDICTIVE ANALYSIS
A weekly sales forecasting model was built using Prophet:

1.Aggregated daily sales into weekly totals

2.Removed extreme outliers

3.Applied log-transform to reduce the effect of large variations

4.Trained on the most recent 19 weeks of data

5.Evaluated on the last 4 weeks (MAPE = 13.55%)

The model captures underlying trends accurately and provides reliable short-term sales forecasts.
---




   
##  Conclusion
This analysis demonstrates how data-driven insights can optimize inventory, improve vendor management, and enhance overall sales performance. Combining Python, Power BI, and forecasting techniques provides actionable recommendations for better decision-making and operational efficiency..<br>

**Shelby Adede**  
- Data Analyst | Machine Learning Enthusiast  
-  shelbyadede@gmail.com  

 






  
