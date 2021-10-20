# NYC_Taxi_Trips
The NYC_Taxi_Trips project is a technical case testing the essential requirements for a job opening.  The main objective of the code is to answer questions about the taxi trips in New York for the years 2009, 2010, 2011, and 2012.

# Dataset
The dataset contains the taxi trips, their companies, and the payment specification, as detailed in the table below:

| Dataset            | Description                        | Type |
|--------------------|------------------------------------|------|
| nyctaxi-trips-2009 | taxi trips in NYC in the year 2009 | JSON |
| nyctaxi-trips-2010 | taxi trips in NYC in the year 2010 | JSON |
| nyctaxi-trips-2011 | taxi trips in NYC in the year 2011 | JSON |
| nyctaxi-trips-2012 | taxi trips in NYC in the year 2012 | JSON |
| vendor_lookup      | data of taxi service companies     | csv  |
| payment_lookup     | data of the payment type           | csv  |

# Questions
The case questions are:
  1. What is the average distance traveled for trips with a maximum of 2 passengers;
  2. Which are the top 3 vendors in a total amount of money raised;
  3. Make a histogram of the monthly distribution, over the 4 years, of runs paid for in cash;
  4. Make a time series graph counting the number of tips each day for the last 3 months of 2012.
  1. What is the average time of races on Saturday and Sunday?

# Code Organization
The main code is found in the "py_answers.py". Alternatively, there is "sql_answers.sql" answering the first two questions using SQL.

# How to run
Pre-requeriments: Python3, Pandas, NumPy, Matplotlib.
```bash
# clone repository
git clone https://github.com/leomakino/NYC_Taxi_Trips

# change directory to NYC_Taxi_Trips folder
cd NYC_Taxi_Trips

# run py_answers.py
python3 py_answers.py
```

# Author
Leonardo Villela Makino
https://www.linkedin.com/in/leonardo-makino-77a559185/
