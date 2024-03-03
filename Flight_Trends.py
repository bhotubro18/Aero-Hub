import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("flight_data.csv")
df = pd.DataFrame(data)
df.head(11000)

def min_price(df):
    return df['money'].min()

def max_price(df):
    return df['money'].max()

def avg_price(df):
    return df['money'].mean()

def median_price(df):
    return df['money'].median()

def plot_trends():
    flag = "1"
    while flag != "0":
        print("Available cities:")
        print("0: Delhi, 1: Mumbai, 2: Kolkata, 3: Hyderabad, 4: Bangalore, 5: Chennai")

        try:
            src_city = int(input("Enter source city: "))
            arr_city = int(input("Enter arrival city: "))
            print('\n')

            cities = {0: "Delhi", 1: "Mumbai", 2: "Kolkata", 3: "Hyderabad", 4: "Bangalore", 5: "Chennai"}

            if src_city not in cities or arr_city not in cities:
                print("Invalid city selection. Please choose from the available cities.")
                continue

            print("\n")
            
            df1 = df[(df['source_city'] == cities[src_city]) & (df['destination_city'] == cities[arr_city])]
            z = int(input("Do you want to see details of the flight of the two citites? press 0 for no and 1 for yes."))
            if(z==0):
                print("")
            else:
                print(df1)
                
            
            plt.figure(figsize=(10, 6))
            plt.title(f'Price Trend from {cities[src_city]} to {cities[arr_city]}')
     
            plot_type = int(input("\nSelect plot type:\n1: Line Plot\n2: Scatter Plot\n\n"))

            if plot_type == 1:
                plt.plot(df1['days_left'], df1['money'], marker='o', color='b', linestyle='-')
            elif plot_type == 2:
                plt.scatter(df1['days_left'], df1['money'], color='r', alpha=0.5)

            plt.xlabel('Days Left')
            plt.ylabel('Price')
            plt.grid(True)
            plt.show()

            print("Statistical Analysis:")
            print("Minimum price:", min_price(df1))
            print("Maximum price:", max_price(df1))
            print("Average price:", avg_price(df1))
            print("Median price:", median_price(df1))
            print('')

            flag = input("Press Enter to see another price trend, or 0 to exit.\n")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

