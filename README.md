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


I built a weekly sales forecasting model using Prophet. First, I aggregated daily sales into weekly totals and removed extreme outliers to ensure stability. I then applied a log-transform to the sales data to reduce the effect of large variations and trained the model on the most recent 19 weeks of data. Predictions were converted back to the original scale, and the model was evaluated on the last 4 weeks. The results showed strong accuracy, with a MAPE of 13.55%, indicating the model reliably captures the underlying sales trend and can be used for short-term forecasting<br>
---




   
##  Conclusion
The analysis in this project demonstrated the power of analytical tools in transforming raw sales data into meaningful insights that can support better business decisions, improve operational efficiency, and drive overall sales performance.<br>

**Shelby Adede**  
- Data Analyst | Machine Learning Enthusiast  
-  shelbyadede@gmail.com  

 






  
