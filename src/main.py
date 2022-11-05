from indicators import *
from plot import *

DEPLOY_DIR_PATH="E:\AlgoTrading\Stock-Market\deploy\list-of-stock"
stock_list = []

def check_trigger_for_buy():
    df = calculate_macd()
    print(df)
    df_last_2 = df.tail(2)
    # if macd histogram last day is -ve and today is +ve and macd today is greater than macd signal
    if ( 
            df_last_2.at[df_last_2.index[0], 'macdh_12_26_9'] < 0 and 
            df_last_2.at[df_last_2.index[1], 'macdh_12_26_9'] > 0 and 
            df_last_2.at[df_last_2.index[1], 'macd_12_26_9'] >  df_last_2.at[df_last_2.index[1], 'macds_12_26_9']
        ):
            print("yes today you can buy")


def load_stocks_list():
    myfile= open( DEPLOY_DIR_PATH, "r" )
    for x in myfile:
        stock_list.append(x.strip())
    myfile.close()


if __name__ == "__main__":
    load_stocks_list() 
    print(stock_list)

    for stock in stock_list:
        check_trigger_for_buy()
    #df.to_csv('dataframe.csv')
    #create_plot(df)
