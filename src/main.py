from decision import *
from plot import *
from sendmail import *
import time
from logger import *
from configparser import ConfigParser
import sys


EXPORTED_FILES_DIR_PATH=".\\tests"
holdings_list = []
watchlist = []
DEBUG_MODE = False
SEND_NOTIFICATION=True

logObject = Logger.getObject("main").logger
def load_stocks_list(watchlist_path, holdings_path):
    logObject.info("loading holdings : ")
    myfile= open( holdings_path, "r" )
    for x in myfile:
        holdings_list.append(x.strip())
    myfile.close()

    logObject.info("loading watchlist : ")
    myfile= open( watchlist_path, "r" )
    for x in myfile:
        watchlist.append(x.strip())
    myfile.close()


if __name__ == "__main__":
    try:
        if DEBUG_MODE:
            # By default it is FAZE3AUTO.BO, change it to debug
            #df = yf.Ticker('FAZE3AUTO.BO').history(period='1y')[map(str.title, ['open', 'close', 'low', 'high', 'volume'])]
            #df.to_csv(EXPORTED_FILES_DIR_PATH + 'faze2auto.csv')
            #sys.exit()
            pass
       
        # Load Configuration
        try:
            config = ConfigParser()
            config.read('config.ini')
            watchlists_path = config.get('PATHS', 'watchlist_path', raw=True)
            holdings_path = config.get('PATHS', 'holdings_path', raw=True)
        except ex:
            print("Unable to load configuration", ex)
            sys.exit(1)

        load_stocks_list(watchlists_path, holdings_path) 
        print(holdings_list)
        print(watchlist)
        while True:
            logObject.info('scanning stocks in holding list')

            messege_buy = "List of stocks to buy from holdings:-\n"
            messege_sell = "List of stocks to sell from holdings:-\n"
            buy_list = check_trigger_for_buy(holdings_list)
            sell_list  = check_trigger_for_sell(holdings_list)

            if SEND_NOTIFICATION: 
                if len(buy_list):
                    send_mail(messege_buy + ' '.join(buy_list))
                if len(sell_list):
                    send_mail(messege_sell + ' '.join(sell_list))

            logObject.info('scanning stocks in watchlist list')
            messege_buy = "List of stocks to buy from watchlists :-\n"
            messege_sell = "List of stocks to sell from watchlists :-\n"
            buy_list = check_trigger_for_buy(watchlist)
            sell_list  = check_trigger_for_sell(watchlist)

            if SEND_NOTIFICATION:
                if len(buy_list):
                    send_mail(messege_buy + ' '.join(buy_list))
                if len(sell_list):
                    send_mail(messege_sell + ' '.join(sell_list))

            time.sleep(60*60*24) # Run once a day
        #create_plot(df)
    except KeyboardInterrupt:
        logObject.info("Application stopped")

