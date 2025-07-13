# Overview
This project involves building a **Python 3 data analysis tool** to extract insights from population datasets provided by the Australian Bureau of Statistics (ABS). The program processes two CSV files containing demographic data and generate statistics on population distribution across age groups and statistical areas.

# Program Requirements
  - No module imports
  - No input()
  - No print()
  - Columns and row order may vary
  - Does not enforce .csv file extensions
  - All returned values must be rounded to 4 decimal places
  - Strings are case-insensitive; all outputs should be in lowercase
  - Must define the top-level function main()

# Project1 Expected Outputs
Function to implement: def main(csvfile_1, csvfile2, age, sa2_1, sa2_2)
  - csvfile_1: File with area relationships between states, SA2 and SA3 levels.
  - csvfile_2: File with population data by age group.
  - age: Age to find matching age group.
  - sa2_2, sa2_2: Two SA2 area codes.

  1. Age group bounds: [lower_bound, upper_bound]
  2. SA3 statistics; list of 2 lists, each containing:
    - SA3 area code
    - Average population in selected age group
    - Standard deviation
  3. Highest age-group population per state; list of lists for each state containing:
    - State name
    - SA3 area name
    - Percentage of population in selected age group
  4. Correlation coefficient between SA2 areas for age groups

# Project2 Expected Outputs
Function to implement: def main(csvfile_1, csvfile2)
  - csvfile_1: File with area relationships between states, SA2 and SA3 levels.
  - csvfile_2: File with population data by age group.

  1. A dictionary mapping age group strings (eg., '0-9', '80-None') to a list of:
    - State with the highest population in the age group
    - SA3 area with the highest population
    - SA2 area with the highest population
    (Tie-breaking is done alphabetically based on area/state codes)
  2. A nested dictionary:
    - Outer keys: state codes
    - Inner keys: SA3 codes (with population >= 150,000)
      Values: a list of:
        - SA2 code with the highest population
        - Population of that SA2
        - Standard deviation of the SA2 population across age groups
  3. A dictionary mapping SA3 area names (with >= 15 SA2 areas) to a list:
    - First SA2 name (alphabetically first)
    - Second SA2 name (alphabetically second)
    - Cosine similarity between their age distribution percentages

# Assumptions
  - All string and numeric data has no missing values
  - Column headers are always in the first row
  - No hardcoding - work dynamically with any valid input file
  - Input arguments will be valid; code must gracefully handle exceptions
