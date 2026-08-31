import sys
import pandas as pd

# goals:
# how much revenue from each country
# how much revenue 
# how much profit (51% of revenue after ad_spend is subtracted)


def main():
    file = sys.argv[1]
    #ad_spend = sys.argv[2]
    

    try:
        df = pd.read_csv(file) 
        print("Spend by Country:")
        print(f"{df.groupby("Card Address Country")["Total Spend"].sum().sort_values(ascending=False).rename_axis(None).to_string()}")
        print(f"Revenue: ${df['Total Spend'].sum():.2f}")
        print(f"Profit: ${df['Total Spend'].sum() * .51:.2f}")
        
                       
    except FileNotFoundError:
       print(f"{file} not found")

if __name__ == "__main__":
    main()
