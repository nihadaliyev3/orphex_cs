# Orphex CS Django Project

## Overview

This project is a Django application designed for analyzing and reporting on user interactions, revenue, and conversions based on a provided CSV dataset. It includes endpoints to calculate conversion rates, analyze status distribution, evaluate category and type performance, and filter and aggregate conversion data.

## Features

- **Conversion Rate Calculation**: Compute conversion rates for each customer and identify the highest and lowest rates.
- **Status-Based Analysis**: Analyze the distribution of statuses across different types and categories, including total revenue and conversions for each status type.
- **Category and Type Performance**: Aggregate total revenue and conversions by category and type, and identify the top-performing combinations.
- **Filtered Aggregation**: Filter data by conversion type and compute average revenue and conversions per customer.

## Setup

### Installation

1. **Clone the Repository**
    ```bash
   git clone https://github.com/nihadaliyev3/orphex_cs.git
   cd orphex_cs
   ```
   
2. **Create and Activate a Virtual Environment**
    ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
    ```bash
   pip install -r requirements.txt
   ```
   
4. **Prepare the Data**
   Ensure the mockupinterviewdata.csv file is located in the root directory(orphex_cs/analytics_api/) of your project.


5. **Run the Development Server**
    ```bash
   cd analytics_api
   python manage.py runserver
   ```
   
## Results
   PDF files of results of API requests are api_results directory.