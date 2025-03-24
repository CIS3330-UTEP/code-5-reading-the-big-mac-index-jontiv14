import csv
import pandas as pd

big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year,country_code):
    df= pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]   #used ai
    df= df[df['iso_a3'].str.lower() == country_code.lower()]
    if df.empty:
        return None 
    return round(df['dollar_price'].mean(),2)


def get_big_mac_price_by_country(country_code):
    df= pd.read_csv(big_mac_file)
    df = df[df['iso_a3'].str.lower() == country_code.lower()]
    if df.empty:
        return None
    return round(df['dollar_price'].mean(), 2)


def get_the_cheapest_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]  # used ai
    if df.empty:
        return None
    min_price = df['dollar_price'].min()
    cheapest = df[df['dollar_price'] == min_price].iloc[0]
    return f"{cheapest['name']}({cheapest['iso_a3'].upper()}): ${round(cheapest['dollar_price'], 2)}"

def get_the_most_expensive_big_mac_price_by_year(year):
    df= pd.read_csv(big_mac_file)
    df = df[df['date'].str.startswith(str(year))]  #used ai
    if df.empty:
        return None
    max_price = df['dollar_price'].max()
    most_expensive = df[df['dollar_price'] == max_price].iloc[0]
    return f"{most_expensive['name']}({most_expensive['iso_a3'].upper()}): ${round(most_expensive['dollar_price'], 2)}"
##used chatgpt 4.0 to troubleshoot

if __name__ == "__main__":
   result_a = get_big_mac_price_by_year(2010, 'arg')
   print(result_a)

   result_b = get_big_mac_price_by_country('mex')
   print(result_b)

   result_c = get_the_cheapest_big_mac_price_by_year(2008)
   print(result_c)

   result_d = get_the_most_expensive_big_mac_price_by_year(2014)
   print(result_d)

