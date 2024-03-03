import pandas as pd

data= pd.read_csv(r"Show_Flights.csv")
df = pd.DataFrame(data)
pd.set_option('display.max_rows', 20000, 'display.max_columns', 20) 

def timing():
    flag = "1"
    while flag != "0":
        src_city = int(input("0: Delhi,\n1: Mumbai,\n2: Kolkata,\n3: Hyderabad,\n4: Bangalore,\n5: Chennai \nEnter source city: "))
        arr_city = int(input("Enter arrival city: "))
        print('\n')

        cities = {0: "Delhi",
                  1: "Mumbai",
                  2: "Kolkata",
                  3: "Hyderabad",
                  4: "Bangalore",
                  5: "Chennai"
                  }

        for i in cities:
            for j in cities:
                if (src_city == i and arr_city == j):
                    df1 = df[(df['source_city'] == cities[i]) & (df['destination_city'] == cities[j])]
                    x=(df1['departure_time'], df1['arrival_time'], df1['airline'], df1['flight'])
                    print(x)
        flag = input("\nDo you want to see another details? \nPress any key to continue and 0 to exit: ")
                    
