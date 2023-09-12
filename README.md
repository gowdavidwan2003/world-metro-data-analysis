

---

# Metro Systems Data Visualization

This project involves visualizing data related to metro systems from various countries and regions. The goal is to provide insights into the characteristics of metro systems, such as length, number of stations, annual ridership, and more. The visualizations are created using Python and libraries like Plotly and Matplotlib.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Project Structure](#project-structure)
- [Visualizations](#visualizations)
- [contributing](#contributing)

## Introduction

Metro systems are an essential part of urban transportation infrastructure. This project aims to visualize and analyze data related to metro systems to gain insights into various aspects of their operations and characteristics.

## Installation

To run the code and visualize the data, you'll need Python and the required libraries installed. You can install the necessary libraries using the following command:

```bash
pip install pandas matplotlib plotly
```

## Usage

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/gowdavidwan2003/world-metro-data-analysis.git
   ```

2. Navigate to the project directory:

   ```bash
   cd world-metro-data-analysis
   ```

3. Run the Python script to generate the visualizations:

   ```bash
   python worldmetrodata.py
   ```

4. The generated visualizations will be displayed or saved (depending on the script settings) in the project directory.

## Data Sources

The data used for this project is sourced from the following CSV files:

- `metro_countries_total.csv`: Data related to metro systems at the country level.
- `metro_countries_cities.csv`: Data related to metro systems at the city level.
- `metro_countries_in_progress.csv`: Data about ongoing metro projects.

## Project Structure

The project directory contains the following files:

- `visualize_metro_data.py`: The main Python script for generating data visualizations.
- `metro_countries_total.csv`: CSV file containing country-level metro data.
- `metro_countries_cities.csv`: CSV file containing city-level metro data.
- `metro_countries_in_progress.csv`: CSV file containing ongoing metro projects data.
- `README.md`: This README file.

## Visualizations

The project generates various types of visualizations, including choropleth maps and bar plots. These visualizations provide insights into different aspects of metro systems data, such as system length, number of stations, annual ridership, ongoing projects, and more.

## Metro Systems All over the world
![World_metro_system_city_list](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/e2ccb8b1-a2a2-4d9d-a83a-24d45a78ec55)


1. Length of metro in a country
![newplot (1)](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/bbeab93b-e096-4d3b-ac02-91e83a4eeeaf)

2. Annual Ridership(in million)
![newplot](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/10ded738-212f-478e-957e-3e3c800e03df)

3. Number of Metro Stations in a country
![newplot (2)](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/bae2ddf6-e7b8-41b7-8af6-4c2269d75de5)

4. Number of Metro Systems in a country
![newplot (3)](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/4722a52d-c590-4625-8984-75eb17de7c4b)

5. Number of Metro lines in a country
![newplot (4)](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/af32ec52-4d09-4502-9dc4-1e38b12efb42)

6. Number of metro stations per each continent
![fig2](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/aa41c9fe-3bd1-4199-89f7-5c6fb36a8ec7)

7. Top 10 cities with highest number of stations
![fig3](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/3869c31a-a208-4f7a-b903-6c57cf78c602)

8. Top 10 cities with highest annual riderships(in million)
![fig5](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/76f48417-df11-4f03-a46f-51930ea2ad97)

9. Amount of ongoing construction in each continent
![fig6](https://github.com/gowdavidwan2003/world-metro-data-analysis/assets/107876507/513b58d7-3ca0-49cc-9ddb-2ba373b4e31f)

So we can conclude that asia as a continent is bullish on the metro systems as they are populous than any other continent

## Contributing

Contributions to this project are welcome! If you find any issues or have ideas for improvements, feel free to submit a pull request or open an issue.


---

Feel free to customize this README template to match the specifics of your project. It provides an overview of the project's purpose, installation instructions, data sources, project structure, visualizations, and information on how others can contribute to the project.
