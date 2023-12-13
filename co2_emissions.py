import pandas as pd
import matplotlib.pyplot as plt


class CO2EmissionsAnalyzer:
    def __init__(self, filename):
        # Initializes the CO2EmissionsAnalyzer instance with the emissions data from the CSV file
        self.df = pd.read_csv(
            filename, header=[1], index_col=[0], skipinitialspace=True
        )

    def get_global_emissions_summary(self):
        # Creates a preview of the data frame
        return self.df.head(10)

    def get_global_yearly_emissions(self):
        # Sums each row
        yearly_total_emissions = self.df.sum(axis=1)
        return yearly_total_emissions

    def get_average_emissions(self):
        return self.get_global_yearly_emissions().mean()

    def get_top_emitting_countries(self, year):
        emissions_by_year = self.df.loc[year]
        sorted_emissions = emissions_by_year.sort_values(ascending=False)
        return sorted_emissions.head()

    def get_average_emissions_per_year(self):
        # Calculates average emissions per year
        average_emissions = self.df.mean(axis=1)
        return average_emissions

    def create_emissions_time_chart(self):
        # Displays a simple time chart for the global emissions changing over time
        yearly_emissions = self.get_global_yearly_emissions()
        plt.plot(yearly_emissions.index, yearly_emissions.values)
        plt.title("Global CO2 Emissions Over Time")
        plt.xlabel("Year")
        plt.ylabel("Emissions (MtCO2)")
        plt.show()

    def create_country_emissions_pie_chart(self, year):
        # Display a simple pie chart for the top countries that contribute to emissions for the given year
        top_emitting_countries = self.get_top_emitting_countries(year)
        plt.pie(
            top_emitting_countries,
            labels=top_emitting_countries.index,
            autopct="%1.1f%%",
        )
        plt.title(f"Top Emitter Countries in {year}")
        plt.show()

    def get_country_emissions_percent(self, year):
        # Get the emissions for the given year
        emissions_by_year = self.df.loc[year]

        # Calculate the total emissions for all countries
        total_emissions = emissions_by_year.sum()

        # Calculate the percentages for each country
        country_percentages = emissions_by_year / total_emissions * 100

        # Create the DataFrame with country and percentage columns
        emissions_df = pd.DataFrame(
            {
                "Country": country_percentages.index,
                "Percentage": country_percentages.values,
            }
        )

        # Sort the DataFrame by percentage in descending order
        emissions_df = emissions_df.sort_values(by="Percentage", ascending=False)

        return emissions_df

    def create_average_emissions_bar_chart(self):
        # Display a simple bar chart for the average emissions per year
        average_emissions = self.get_average_emissions_per_year()
        plt.bar(average_emissions.index, average_emissions.values)
        plt.title("Average CO2 Emissions per Year")
        plt.xlabel("Year")
        plt.ylabel("Average Emissions (MtCO2)")
        plt.xticks(rotation=90)
        plt.show()


# Create an instance of the analyzer
analyzer = CO2EmissionsAnalyzer("export_emissions.csv")

# Show a small overview of the data frame
print("\nData frame overview:")
print(analyzer.get_global_emissions_summary())

# Question 1: How have yearly CO2 emissions changed over the years?

print("\nTotal global yearly emissions:")
print(analyzer.get_global_yearly_emissions())

# Question 2: Which countries are the top contributors to global CO2 emissions (for the most recent year)?

most_recent_year = analyzer.df.index[-1]
top_emitting_countries = analyzer.get_top_emitting_countries(most_recent_year)
print(f"\nTop contributing countries in {most_recent_year}:")
print(top_emitting_countries)

# Question 3: What is the average annual global CO2 emissions?

print(
    f"\nAverage global yearly emissions: {analyzer.get_average_emissions():.2f} MtCO2"
)

# Additional visualization

# Show the average emissions per country for each year

analyzer.create_average_emissions_bar_chart()

# Show the yearly emissions time chart

analyzer.create_emissions_time_chart()

# Show top contributors to global CO2 emissions

analyzer.create_country_emissions_pie_chart(most_recent_year)

# Create DataFrame for country emission percentages
country_emissions_df = analyzer.get_country_emissions_percent(most_recent_year)
print("\nCountry Emission Contributions Percentages:")
print(country_emissions_df)
