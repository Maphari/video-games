# ETL Data Engineering Project: Video Games

This project demonstrates the process of extracting, transforming, and loading (ETL) data, focusing on video game data. The data used in this project was obtained from Maven Analytics and is stored in CSV format. The ETL process was carried out using Azure Data Studio, and the transformed data is saved in a MySQL database.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Source](#data-source)
- [Technologies Used](#technologies-used)
- [ETL Process](#etl-process)
  - [Extraction](#extraction)
  - [Transformation](#transformation)
  - [Loading](#loading)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Overview

The aim of this project is to build an ETL pipeline for video game data, showcasing best practices in data engineering. The raw data includes various aspects of video games such as titles, genres, release dates, and sales figures. The final dataset is stored in a MySQL database for further analysis and querying.

## Data Source

The data for this project was sourced from Maven Analytics and is available in CSV format. It includes comprehensive information on video games, including:

- Game titles
- Genres
- Platforms
- Release dates
- Sales figures
- Publisher and developer information

## Technologies Used

- **Data Source:** Maven Analytics (CSV files)
- **ETL Tool:** Azure Data Studio
- **Database:** MySQL
- **Programming Language:** Python, SQL

## ETL Process

### Extraction

The extraction phase involves reading the raw CSV files containing the video game data. This data is loaded into Azure Data Studio for initial examination and basic cleaning.

### Transformation

During the transformation phase, the data undergoes several processing steps to ensure it is clean, consistent, and structured appropriately for analysis. This includes:

- Removing duplicates
- Handling missing values
- Standardizing date formats
- Normalizing text fields (e.g., converting all text to lowercase)
- Aggregating sales figures

### Loading

The cleaned and transformed data is then loaded into a MySQL database. The database schema is designed to optimize query performance and ensure data integrity. The following tables are created:

- `games`: Contains basic information about each game (title, genre, platform, etc.).
- `sales`: Contains sales figures for each game, broken down by region.
- `developers`: Contains information about the developers of each game.
- `publishers`: Contains information about the publishers of each game.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/video-games-etl.git
   cd video-games-etl
   ```

2. **Install MySQL:**
   Follow the instructions for your operating system to install MySQL.

3. **Setup the MySQL database:**
   - Create a new database in MySQL:
     ```sql
     CREATE DATABASE video_games_db;
     ```
   - Use the provided SQL scripts in the `sql` directory to create the necessary tables.

4. **Load the CSV data into Azure Data Studio:**
   - Open Azure Data Studio and connect to your MySQL database.
   - Use the import wizard to load the CSV files into the respective tables.

## Usage

Once the data is loaded into the MySQL database, you can perform various SQL queries to analyze the video game data. Some example queries might include:

- Finding the top-selling games of all time.
- Analyzing sales trends over the years.
- Comparing sales performance across different platforms.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue to discuss your ideas.
