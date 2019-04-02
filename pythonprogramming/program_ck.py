import pandas as pd
import os
import time
from datetime import datetime

path = "/Users/chukimmuoi/AI/data/intraQuarter"


def Key_Stats(gather="Total Debt/Equity (mrq)"):
    statspath = path + '/_KeyStats'
    stock_list = [x[0] for x in os.walk(statspath)]
    df = pd.DataFrame(columns=['Date',
                               'Unix',
                               'Ticker',
                               'DE Ratio',
                               'Price',
                               'stock_p_change',
                               'SP500',
                               'sp500_p_change'])

    sp500_df = pd.read_csv("YAHOO-INDEX_GSPC.csv")

    ticker_list = []

    for each_dir in stock_list[1:]:
        each_file = os.listdir(each_dir)
        ticker = each_dir.split("/")[-1]
        ticker_list.append(ticker)

        starting_stock_value = False
        starting_sp500_value = False

        if len(each_file) > 0:
            for file in each_file:
                date_stamp = datetime.strptime(file, '%Y%m%d%H%M%S.html')
                unix_time = time.mktime(date_stamp.timetuple())

                full_file_path = each_dir + '/' + file
                print(full_file_path)
                source = open(full_file_path, 'r', encoding='utf-8').read().replace("\n", "")

                try:
                    stock_price = source.split('</small><big><b>')
                    if len(stock_price) >= 2:
                        stock_price = stock_price[1].split('</b></big>&nbsp;&nbsp;<img')
                        if len(stock_price) >= 2:
                            stock_price = stock_price[0]
                        else:
                            stock_price = 0
                    else:
                        stock_price = 0

                    try:
                        sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df['Date'] == sp500_date)]
                        sp500_value = float(row['Adj Close'])
                    except:
                        sp500_date = datetime.fromtimestamp(unix_time - 259200).strftime('%Y-%m-%d')
                        row = sp500_df[(sp500_df['Date'] == sp500_date)]
                        sp500_value = float(row['Adj Close'])

                    if not starting_stock_value:
                        starting_stock_value = stock_price
                    if not starting_sp500_value:
                        starting_sp500_value = sp500_value

                    stock_p_change \
                        = ((float(stock_price) - float(starting_stock_value)) / float(starting_stock_value)) * 100
                    sp500_p_change \
                        = ((float(sp500_value) - float(starting_sp500_value)) / float(starting_sp500_value)) * 100

                    value = source.split(gather + ':</td><td class="yfnc_tabledata1">')
                    if len(value) >= 2:
                        value = value[1].split('</td>')
                        if len(value) >= 2:
                            value = value[0]
                            df = df.append({'Date': date_stamp,
                                            'Unix': unix_time,
                                            'Ticker': ticker,
                                            'DE Ratio': value,
                                            'Price': stock_price,
                                            'stock_p_change': stock_p_change,
                                            'SP500': sp500_value,
                                            'sp500_p_change': sp500_p_change}, ignore_index=True)
                except Exception as e:
                    pass

    save = gather.replace(' ', '').replace(')', '').replace('(', '').replace('/', '') + ('.csv')
    print(save)
    df.to_csv(save)


Key_Stats()
