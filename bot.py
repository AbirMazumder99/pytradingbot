def getBalances():
    # DO: GET request to exchange API for your account's balances
    return Balances

def getMarketPrice():
    # DO: GET request to exchange API for current price of the asset
    return Market_Price

def placeBuyOrder():
    # PSEUDO
    # cashpositon = 15 percent of total
    # longposition = 75 percent of total
    # chunk = 10percent of long position
    
    # if price < 95PercentOfPrice5SecondsAgo
    # invest chunk
    # longposition = longposition - chunk
        # if price < 85PercentOfPrice5SecondsAgo
        # stall chunk

def placeSellOrder():
    # if price > 105PercentOfPrice5SecondsAgo
    # sell chunk
        # longposition = longposition + chunk
        # if price < 115PercentOfPrice5SecondsAgo
        # stall chunk

def getOperationDetails():
    # DO: GET request to API for the details of an operation
    return Details


def startBot():
    # INFINITE LOOP:
        # attemptToMakeTrade()
        # sleep(30 seconds)



bool isNextOperationBuy = True

UPWARD_TREND_THRESHOLD = 1.5
DIP_THRESHOLD = -2.25

PROFIT_THRESHOLD = 1.25
STOP_LOSS_THRESHOLD = -2.00

float lastOpPrice = 100.00

def attemptToMakeTrade():
    float currentPrice = getMarketPrice()
    float percentageDiff = (currentPrice - lastOpPrice)/lastOpPrice*100
    if isNextOperationBuy:
        tryToBuy(percentageDiff)
    else:
        tryToSell(precentageDiff)





def tryToBuy(float percentageDiff):
    if percentageDiff >= UPWARD_TREND_THRESHOLD or percentageDiff <= DIP_THRESHOLD:
        lastOpPrice = placeBuyOrder()
        isNextOperationBuy = False


def tryToBuy(float percentageDiff):
    if percentageDiff >= PROFIT_THRESHOLD or percentageDiff <= STOP_LOSS_THRESHOLD:
        lastOpPrice = placeSellOrder()
        isNextOperationBuy = True





def createLog(string msg):
    # DO:
        # Print msg to terminal
        # Append msg to log file with timestamp