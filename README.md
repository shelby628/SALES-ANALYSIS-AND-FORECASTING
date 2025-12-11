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
   




## OVERVIEW / OBJECTIVES
To analyze and manage inventory, sales, and purchases data effectively in order to support business decisions, identify trends, and improve operational efficiency.
## Data Sources
- `Dataset` —    
-
## Tools Used
- Python (Jupyter Notebook)
- Python (script)
- Power BI

  
  
  
  ##  Process
1. Data Cleaning — handled missing values and removed duplicates  
2. Exploratory Data Analysis (EDA) — visualized distributions and correlations  
3. Visualization — built KPI dashboards in Power BI  
4. Reporting — summarized findings for decision making

  ## QUESTIONS (KPI)
1. Who are the top ten vendors by total sales?
2. Which are the underperforming  brands that require promotional adjustments?
3. Why are they Underperforming?
4.Assess inventory turnover to reduce holding costs and improve efficiency
5. Impact of bulk purchasing on unit costs
6. Investigating profitability varience between high performing and low performing vendors?
7.  How much of total procurement is dependent on top vendors?

 ## Key Insights
1- Brands sell in low quantities since they have poor customer demand.
2- Most brands are underperforming because they are not in customer demand so probably not purchasing them will be a greater benefit to the company as they hold up space
3-Most of inventory sells well at low stock levels, but a small group of items is massively overstocked and barely selling — these are the biggest cost drivers and need immediate correction.
4-High-performing vendors have stable profit margins despite high revenues.
 Low-performing vendors have unpredictable margins—some are very high, but others are very low. This variability could be risky.
Even though Low Vendors’ median is slightly higher, the consistency of High Vendors makes them more reliable.




<img width="854" height="367" alt="image" src="https://github.com/user-attachments/assets/c0839745-4238-4ff3-b242-8550eff67e6c" />

<img width="702" height="365" alt="image" src="https://github.com/user-attachments/assets/1d01b6fe-17e5-43ed-9852-e11e5f495592" />

<img width="482" height="331" alt="image" src="https://github.com/user-attachments/assets/a1aa210d-b66c-4e7d-86ce-10645222f2b6" />

High-performing vendors demonstrate reliability in profit margins, whereas low-performing vendors show unpredictable results, with both very low and very high extremes.

<img width="734" height="359" alt="image" src="https://github.com/user-attachments/assets/fd943e66-dd67-4c26-a9d6-53e809426b9a" />
Sales initially experienced a sharp decline, but later stabilized and began following a consistent weekly seasonal pattern. The forecast indicates that sales will remain steady with regular fluctuations, though long-term uncertainty increases.

<img width="816" height="365" alt="image" src="https://github.com/user-attachments/assets/e01e370b-75df-44c8-b9af-99692ca456ff" />

I built a weekly sales forecasting model using Prophet. First, I aggregated daily sales into weekly totals and removed extreme outliers to ensure stability. I then applied a log-transform to the sales data to reduce the effect of large variations and trained the model on the most recent 19 weeks of data. Predictions were converted back to the original scale, and the model was evaluated on the last 4 weeks. The results showed strong accuracy, with a MAPE of 13.55%, indicating the model reliably captures the underlying sales trend and can be used for short-term forecasting




   
##  Conclusion
The analysis in this project demonstrated the power of analytical tools in transforming raw sales data into meaningful insights that can support better business decisions, improve operational efficiency, and drive overall sales performance.

**Shelby Adede**  
- Data Analyst | Machine Learning Enthusiast  
-  shelbyadede@gmail.com  

 






  
