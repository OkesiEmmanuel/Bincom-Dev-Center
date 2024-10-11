# Dress Color Analysis Tool

This project analyzes the colors of dresses worn by BINCOM DEV CENTRE staff throughout the week. It scrapes a webpage, processes 
the color data, and provides statistical insights such as the most frequent color, median color, and mean color. Additionally,
it saves the color frequencies to a PostgreSQL database and implements several utility functions for tasks such as
Fibonacci sequence summation and random binary generation.

## Features
1. **Web Scraping**: Extracts color data from a webpage.
2. **Color Analysis**:
   - Most worn color.
   - Mean color.
   - Median color.
   - Variance of the colors.
   - Probability of selecting "red" randomly.
3. **Data Storage**: Saves the color frequencies into a PostgreSQL database.
4. **Utility Functions**:
   - Random 4-digit binary number generator and base 10 conversion.
   - Sum of the first 50 Fibonacci sequence numbers.
   - Recursive search for a number in a list.

## Project Structure
├── main.py # Main file that runs the program ├── databaseConnection.py # Database operations using PostgreSQL ├── helpers.py # Utility functions (fibonacci, recursive search, etc.) ├── README.md # Project documentation └── requirements.txt # Dependencies


## Prerequisites

- Python 3.x
- PostgreSQL installed and configured
- Required Python libraries:
  - `requests`
  - `psycopg2`

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/OkesiEmmanuel/Bincom-Dev-Center.git
cd Bincom-Dev-Center


