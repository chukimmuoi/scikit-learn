import pandas as pd
import os
import quandl
import time

path = '/Users/chukimmuoi/AI/data/intraQuarter'


def Stock_Prices():
    df = pd.DataFrame()

    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    print(stock_list)

    for each_dir in stock_list[1:]:
        try:
            ticker = each_dir.split("/")[-1]
            print(ticker)
            name = "WIKI/" + ticker.upper()
            print(name)
            data = quandl.get(name,
                              start_date="2000-12-12",
                              end_date="2014-12-30",
                              api_key="35jpbo7DM1pCD6W_qzDY")
            data[ticker.upper()] = data["Adj. Close"]
            df = pd.concat([df, data[ticker.upper()]], axis=1)
        except Exception as e:
            print(str(e))

    df.to_csv("stock_peices.csv")


Stock_Prices()
