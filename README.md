# Overview

This program analyzes and visualizes the CO2 emissions data set provided by the global Carbon Atlas with the purpose of providing answers to specific questions about the CO2 emissions of the world.

The program utilizes basic functionalities of the pandas library like sorting, calculating average and calculating the sum of columns and rows.

This program was created with the purpose of learning basic data analysis fundamentals and how python libraries like matplotlib and pandas can be implemented to make large data sets easier to analyze.

The global Carbon Atlas is a detailed dataset that allows people to explore, visualize, and interpret carbon dioxide emissions and flux data at the national and global levels.It uses MtCO2 to quantify and represent the amount of carbon dioxide emissions or flux. MtCO2 stands for megatonnes of carbon dioxide, which is a unit of measurement used to express the quantity of carbon dioxide released or absorbed in the atmosphere.

The source for the data set is in the following website:

[Global Carbon Atlas](https://globalcarbonatlas.org/emissions/carbon-emissions/)

[Software Demo Video](https://youtu.be/XYJeHfn78f0)

# Data Analysis Results

## Question 1: How have yearly CO2 emissions changed over the years?

I started by adding each row to get the global emissions of each year, the data set goes from 1960 to 2021. After adding each row i displayed the data with a time chart that showed me that global emissions have been growing linearly, there are some small dips but global CO2 emissions are likely to keep rising over time.On average countries used to emit over 40 MtCO2, for the year 2021 this number has increased to over 160 MtCO2 per country.

## Question 2: Which countries are the top contributors to global CO2 emissions (for the most recent year)?

I started by locating the row that had the global emission information for the most recent year available in the data set, that year is 2021, once i had all the country emissions for that year i sorted the values so that the countries with the most CO2 emissions stayed at the top. This showed me that according to the data set the top countries that contribute to global CO2 emissions are China, the United Stated of America, India, the Russia Federation and Japan. Between all CO2 emissions per country for the year 2021 31.57% of these emissions were contributed by China.

## Question 3: What is the average annual global CO2 emissions?

I summed each row to get the total yearly global CO2 emissions, once i had this data i used the mean() method to get an average annual global CO2 emissions. On average the global yearly emissions are around 22519.46 MtCO2.

# Development Environment

- Visual Studio Code
- Python
- Pandas
- Matplotlib
- Github/Git

# Useful Websites

- [Matplotlib Documentation](https://matplotlib.org/stable/api/matplotlib_configuration_api.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Exploratory Data Analysis with Pandas](https://www.kaggle.com/code/kashnitsky/topic-1-exploratory-data-analysis-with-pandas/notebook)

# Future Work

- Enhance data visualization by exploring different types of plots and charts to present the CO2 emissions trends more effectively.
- Implement interactive features in the program, such as allowing the user to select specific years or countries for analysis.
- Incorporate machine learning techniques to predict future CO2 emissions based on historical data.
- Implement error handling and data validation to ensure the program can handle unexpected data formats or missing values.
