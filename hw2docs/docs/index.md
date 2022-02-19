# CSE314 Homework 2 Documentation

This page lists the non-technical information about the datasets used in this project and answers required questions. For a list of callbacks for each dataset, refer to the corresponding tab on the navigation bar. 

## (Extra credits)
- Each dataset has callbacks in a separate file in assignments/hw2
- Doc is uploaded to [readthedoc](https://readthedocs.org/) and Github [link](https://readthedocs.org/) can be found on the top right corner. 


## Alcohol Consumption Dataset (eCDF)

- This dataset is about the rate of alcohol consumption among countries. 
- This dataset is visualized using a eCDF chart.
- My visualization is interesting because using a combination of both an eCDF graph (which is better than histograms) and a checklist, the eCDF graph can be updated to contains only the countries being selected, making it easy to visualize and compare the rate of alcohol consumption among only the countries of interest. 
- eCDF is preferrable to histograms because a histogram's structure depends on the number of bins. When changing the number of bins, a histogram generated from the same data can have different strucutres and distribution (this is called Binning Bias). For example, some number of bins may generate a histogram that is left-skewed while another may generate a histogram that is bell-shaped. Picking out the correct number of bins to optimally visualize your data and avoid Binning Bias can be tricky. Therefore, an eCDF is preferrable since it does not depend on the number of bins, so an eCDF's structure doesn't change when the number of bins change, and it is stil able to capture outliers ([source](https://medium.com/convergeml/why-ecdf-is-better-than-a-histogram-85deda4129ed)). 

## Apple Stock Dataset (Chained callback)

- This dataset contains the daily historical data of the AAPL ticker in 2014. 
- This dataset is visualized using a line chart.
- My visualization is interesting because the best and easiest way (in my opinion) to visualize stock prices over a period of time is through a line chart. A line chart, combined with a date selector, makes it even more conveinet to analyze Apple's stock price in 2014 since you have the option to focus on the price of some specific period in 2014. 

## School Earnings Dataset

- This dataset contains the average earnings of male and female employees in a set of universities in the U.S. 
- This dataset is visualized using a barchart.
- My visualization is interesting because not only is barchart a very good way to compare the values of distinct classes, my barchart also has different colors for different genders for the same bar (representing a school). Looking at this graph, you can easily compare the total earnings among schools, as well as how much males earn more than females in a specific school or compared to other schools. 
