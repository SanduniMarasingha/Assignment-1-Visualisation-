
import pandas as pd
import matplotlib.pyplot as plt


def line_plot(path):
    """The line_plot function takes a path to a CSV file as an argument and creates a line plot 
    showing the GDP growth (annual %) for the countries listed in the CSV file.
    The function uses the pandas library to load the data from the CSV file and matplotlib to create the plot.
    It defines the x-axis as a list of years and adds a line for each country by iterating through the rows of the data
    and getting the GDP data and country name for each row.
    The function sets the title and axis labels, adds a legend, rotates the x-axis labels, and displays the plot using plt.show()."""

    # Load the CSV data using pandas
    data = pd.read_csv(
        "C:/Users/Sanduni Sakunthala/Desktop/Assignment/data_gdp.csv")

    # Define the x-axis as a list of years
    years = data.columns[4:]

    # Create a new figure
    fig, ax = plt.subplots()

    # Add a line for each country
    for i in range(len(data.iloc[:5, 2])):
        # Get the GDP data for the current country
        Y = data.iloc[i, 4:]

        # Get the name of the current country
        country = data.iloc[i, 2]

        # Add a line for the current country
        ax.plot(years, Y, label=country)

    # Set the title and axis labels
    ax.set_title('GDP Growth (Annual %)')
    ax.set_xlabel('Year')
    ax.set_ylabel('%')

    # Add a legend
    ax.legend()
    plt.xticks(rotation=90)
    # Show the plot
    plt.show()


# Call the line_plot function and pass the path to the CSV file as an argument
line_plot('data_gdp.csv')


# In[1]:


def bar_plot(path):
    """The bar_plot function takes a path to a CSV file as an argument and creates a bar plot showing 
    the GDP growth (annual %) for the countries listed in the CSV file.
    The function uses the pandas library to load the data from the CSV file and matplotlib to create the plot. 
    It creates a list of years to use as the x-axis and a list of colors for each country. It then iterates through 
    the rows of the data and gets the GDP data and country name for each row. It plots a bar plot for each country using
    the extracted data and sets the x-axis and y-axis labels, the plot title, and adds a legend to the plot. Finally,
    it rotates the x-axis labels and displays the plot using plt.show()."""

    # Read the data from a CSV file
    data = pd.read_csv(
        "C:/Users/Sanduni Sakunthala/Desktop/Assignment/data_gdp.csv")

    # Create a list of years to use as the x-axis
    years = data.columns[4:]

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Create a list of colors for each country
    colors = ['blue', 'red', 'green', 'orange', 'purple']

    # Create a bar plot for each country
    for i in range(len(data.iloc[:5, 2])):
        # Extract the GDP growth data for a country
        Y = data.iloc[i, 4:]
        # Extract the country name
        country = data.iloc[i, 2]
        # Plot the bar plot for the country
        ax.bar(years, Y, label=country, color=colors[i])

    # Set the x-axis and y-axis labels
    ax.set_xlabel('Year')
    ax.set_ylabel('%')

    # Set the plot title
    ax.set_title('GDP Growth (Annual %)')

    # Add a legend to the plot
    ax.legend()
    plt.xticks(rotation=90)
    # Show the plot
    plt.show()


# Call the bar_plot function with a CSV file path as an argument
bar_plot('data_gdp.csv')


# In[2]:

def scatter_plot(path):
    """The scatter_plot function takes a path to a CSV file as an argument and creates a scatter plot showing the GDP growth (annual %) for
    the countries listed in the CSV file over time.
    The function uses the pandas library to load the data from the CSV file and matplotlib to create the plot. 
    It creates a list of years to use as the x-axis and then iterates through the rows of the data and gets
    the GDP data and country name for each row. It plots a marker for each year of GDP growth for
    the current country using the extracted data. It sets the plot title and axis labels and adds a legend to the plot. 
    Finally, it rotates the x-axis labels and displays the plot using plt.show()."""

    # Read the data from a CSV file
    data = pd.read_csv(
        "C:/Users/Sanduni Sakunthala/Desktop/Assignment/data_gdp.csv")

    # Create a list of years to use as the x-axis
    years = data.columns[4:]

    # Create a plot with a marker for each country's GDP growth over time
    fig, ax = plt.subplots()
    for i in range(len(data.iloc[:5, 2])):
        # Extract the GDP growth data for a country
        Y = data.iloc[i, 4:]
       # Extract the country name
        country = data.iloc[i, 2]
        # Plot a marker for each year of GDP growth for the current country
        ax.scatter(years, Y, label=country)

    # Set the plot title and axis labels
    ax.set_title('GDP Growth (Annual %)')
    ax.set_xlabel('Year')
    ax.set_ylabel('%')

    # Add a legend to the plot
    ax.legend()
    plt.xticks(rotation=90)
    # Show the plot
    plt.show()


# Call the scatter_plot function with a CSV file path as an argument
scatter_plot('data_gdp.csv')
