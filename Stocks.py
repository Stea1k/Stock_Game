__author__ = 'nick_toffle'
import random
# Program: Mock Stock market
# Author: Nick Toffle
# Current Version: 9-11-15

# Description:
# This program attempts to emulate the stock market at a very basic level.
# A user is an investor who buys and sells stocks as the game progresses
# The game ends at the end of round 9.


# 4 different kinds of stock.
# 1: Blue Chip
# 2: Speculative
# 3: Warrants
# 4: Preferred
# 5: Bond

# All Stock have 2 characteristics
# 1: Current Values
# 2: Day to day variance/ Frequency of Stock

# Stocks are objects, but hold the above principles

# This game will move from the perspective of a single market player.
# Should be possible to adapt it to multiple users.

ROUNDS = 8

STOCKTYPE = ['Blue Chip', 'Speculative', 'Preferred', 'Bond', 'Warrant']

STOCKSTARTVALUE = [40, 20, 50, 90, 5]

WALLETSTART = 2000

stockList = []

MARKETTREND = ['Bear', 'Mixed', 'Bull']

BEAR = [[-2, -3, -5, -7, -10, -13],
        [-4, -7, -11, -16, -22, -50],
        [0, -1, -2, -3, -5, -7],
        [-4, -6, -10, -14, -20, -26],
        [-1, -1, -2, -2, -4, -8]]

MIXED = [[7, 6, 4, 0, -2, -4],
        [20, 10, 5, 0, -6, -15],
        [6, 4, 2, 0, -1, -3],
        [14, 12, 8, 0, -4, -8],
        [4, 2, 1, 0, -1, -3]]

BULL = [[14, 11, 8, 6, 4, 2],
        [44, 22, 10, 4, 0, -2],
        [10, 8, 6, 4, 2, 0],
        [28, 22, 16, 12, 8, 4],
        [8, 5, 3, 2, 1, 0]]

# Objects:
# 1: Stocks

class Stock:
    def __init__(self, type, value):
        self.type = type
        self.value = value
        self.invest = 0

    def getType(self):
        return self.type

    def getValue(self):
        return self.value

    def getInvest(self):
        return self.invest

    def setType(self, type):
        self.type = type

    def setValue(self, value):
        self.value = value

    def changeValue(self, change):
        self.value += change

    def setInvest(self, investors):
        self.invest += investors

    def increaseInvest(self):
        self.invest += 1

    def reduceInvest(self):
        self.invest -= 1

    def resetInvest(self):
        self.invest = 0

# Investor class:
# Investor has a given starting wallet, number of purchased stocks of varying types
# 1: Wallet
# 2: Number of  Blue Chips
# 3: Number of Speculative
# 4: Number of Preferred
# 5: Number of Bonds
# 6: Number of Warrants

class Investor:
    def __init__(self, wallet):
        self.wallet = wallet
        # StockQ(0) = Blue Chip
        # StockQ(1) = Speculative
        # StockQ(2) = Preferred
        # StockQ(3) = Bond
        # StockQ(4) = Warrant
        self.StockQ = [0, 0, 0, 0, 0]

    def getWallet(self):
        return self.wallet

    def getStockQ(self, i):
        return self.StockQ[i]

    def getStockList(self):
        return self.StockQ

    def setWallet(self, change):
        self.wallet += change

    def setStockQ(self, i, dif):
        self.StockQ[i] += dif

    def reduceStockQ(self, i, dif):
        self.StockQ[i] -= dif


# Game as it's own class?
# Need to determine how Stock Values will change.
# changes are typically considered random.

# Changes as a class?:
# 1: Bear - General decrease in value across the board
# 2: Bull - General increase in value across the board
# 3: Mixed - Combination of increase and decrease across the board

# pieces of a Market trend
# market trend name
# Investor buy/sell
# general market buy/sell
# trend shifts

trends = []

class marketTrend:
    def __init__(self, type):
        self.type = type
        self.Stocks = []

    # Stocks will be list of lists
    #
    # each item in the list will contain 6 values corresponding to market shifts
    # to get prices changes relating to a specific stock, an integer is required for the directory.
    #
    # delta Stock index ranges from 0 to 4
    # delta Price index ranges from 0 to 5

    def getStocks(self,index):
        deltaStock = self.Stocks[index]
        return deltaStock

    def getDPrice(self, index1, index2):
        deltaStock = self.getStocks(index1)
        deltaPrice = deltaStock[index2]
        return deltaPrice

    def setStocks(self, dStocks):
        self.Stocks = dStocks

    def getAllStockChanges(self):
        return self.Stocks

class StockMarketGame():
    def __init__(self):
        self.investor = Investor(WALLETSTART)
        self.stocks = []
        self.marketTrends = []
        self.currentTrend = 0

    def getInvestor(self):
        return self.investor

    def getStocks(self):
        return self.stocks

    def getMarketTrends(self):
        return self.marketTrends

    def getCurrentTrend(self):
        return self.currentTrend

    def getCurrentMarketTrend(self):
        trendsSet = self.marketTrends[self.getCurrentTrend()]
        return trendsSet

    def setStocks(self, types, values):
        for v in range(0, 5):
            aStock = Stock(types[v], values[v])
            self.stocks.append(aStock)

    def setMarketTrends(self):
        bear = marketTrend(MARKETTREND[0])
        mixed = marketTrend(MARKETTREND[1])
        bull = marketTrend(MARKETTREND[2])

        bear.setStocks(BEAR)
        mixed.setStocks(MIXED)
        bull.setStocks(BULL)

        self.marketTrends.append(bear)
        self.marketTrends.append(mixed)
        self.marketTrends.append(bull)

    def setCurrentTrend(self):
        self.currentTrend = random.randint(0, 2)

    def resetStockChanges(self):
        for i in range(0, 5):
            self.stocks[i].resetInvest()

    def stockInvestSet(self):
        setOfStocks = self.getStocks()
        for i in range(0, 5):
            aStock = setOfStocks[i]
            invNum = 5 - random.randint(0, 5)
            aStock.setInvest(invNum)

    def stockInvestSetInitial(self):
        setOfStocks = self.getStocks()
        for i in range(0, 5):
            aStock = setOfStocks[i]
            invNum = random.randint(0, 2)
            aStock.setInvest(invNum)

def cont():
    go = input('Press any key to continue\n')

def Main():
    agame = StockMarketGame()
    agame.setStocks(STOCKTYPE, STOCKSTARTVALUE)
    agame.setMarketTrends()

    # need to find something that requests for 'Enter to continue'.

    #//////////////////////////////////////////////////////////////

    # Start of interactive main code

    #//////////////////////////////////////////////////////////////

    # description of game
    print('Welcome to the Stock Market Game!\n')
    cont()
    print('To begin trading stocks, please make a selection based on the options available.\n')
    cont()
    print('You will have 8 periods to buy and sell your stocks, so good luck!')
    print("Don't forget to buy low and sell high.\n")
    cont()

    period = 0

    rnd = ROUNDS

    # while loop that initiates the main sequence
    while rnd >= 0:
        period += 1

        # checks if a stock value has dropped below or to 0. If it has, then it should be returned to 1
        for s in range(0, 5):
            if agame.getStocks()[s].getValue() <= 0:
                agame.getStocks()[s].setValue(1)

        # prints out a general set of information for the investor to look over.
        print('Period: ' + str(period))
        prices = agame.getStocks()
        for s in range(0,5):
            astock = prices[s]
            print(str(s+1)+': ' + astock.getType() + ' : ' + str(astock.getValue()))
        print('\n')

        # an initial loop to begin an investors options.
        purchase = ''
        while purchase != 'end':
            purchase = input(
                        "Would you like to start buying or selling any stock?\nType 'buy' or 'sell', otherwise type 'end'"
                        " for the next round.")
            print('')

            # sets up the selling option.
            if purchase == 'sell':
                investments = agame.getInvestor().getStockList()
                sum = 0
                for i in range(0, 5):
                    sum += investments[i]

                # just in case an investor has no investments, but is still trying to sell items.
                if sum <= 0:
                    print('You have no investments to sell.\nRequest has been denied.')
                    cont()
                else:
                    # a summary
                    while sum > 0:
                        print('Summary of Investments:')
                        for i in range(0,5):
                            invs = agame.getInvestor().getStockList()[i]
                            val = agame.getStocks()[i].getValue()
                            invName = STOCKTYPE[i]
                            print(str(i+1) + ':' +invName + ': ' + str(invs) + ' | ' + str(invs * val))
                        print('')
                        try:
                            quit = str(input("Type 'n' or 'no' to quit now. Otherwise hit enter to continue"))
                            print('\n')
                        except:
                            print('You must enter n, no, or enter')
                        else:
                            if quit == 'n' or quit == 'no':
                                print('sell order cancelled')
                                break
                            else:
                                try:
                                    # how many would you like ot sell?
                                    stockToSell = int(input("Please enter the index number of the stock you wish to sell."))
                                    print('')
                                except:
                                    print('You must enter an index number linked to the stock of interest.\n')
                                    cont()
                                else:
                                    stockToSell -= 1
                                    theStock = STOCKTYPE[stockToSell]
                                    theStockPrice = agame.getStocks()[stockToSell].getValue()
                                    print(theStock + ': ' + str(theStockPrice)+'\n')
                                    try:
                                        validate = str(input('Is this the stock type you would like to sell? y/n\n'))
                                    except:
                                        print("Only inputs available are 'y' or 'n'.")
                                        cont()
                                    else:
                                        if validate == 'n':
                                            print('\n')
                                        elif validate == 'y':
                                            invs = agame.getInvestor().getStockList()[stockToSell]
                                            val = agame.getStocks()[stockToSell].getValue()
                                            t = agame.getStocks()[stockToSell].getType()
                                            # a quick summary of an investors holdings
                                            print('This is your current stock holding of that type: \n')
                                            print(t + ": " + str(invs) + ' | ' + str(val) + ' | ' + str(invs*val) + '\n')
                                            cont()
                                            try:
                                                sale = int(input('How many would you like to sell?\n'))
                                            except:
                                                print('You must enter a whole number')
                                                cont()
                                            else:
                                                if sale > agame.getInvestor().getStockQ(stockToSell):
                                                    # verifies the amount of stock being sold.
                                                    # cancels the transaction if the investor does not have adequate inventory
                                                    print('You do not have enough stock for that sale.\n')
                                                    print('The transaction has been cancelled.\n')
                                                else:
                                                    # applies the changes as are relevant
                                                    agame.getInvestor().reduceStockQ(stockToSell, sale)
                                                    deltaWallet = sale * val
                                                    agame.getInvestor().setWallet(deltaWallet)
                                                    agame.getStocks()[stockToSell].increaseInvest()

                                                    results = agame.getInvestor()
                                                    finalWallet = results.getWallet()
                                                    finalStocks = results.getStockList()

                                                    print('Transaction completed successfully\n')

                                                    print('Your current funds: $' + str(finalWallet))

                                                    print('Your current Investments: \n')

                                                    for i in range(0, 5):
                                                        print(STOCKTYPE[i] + ": " + str(finalStocks[i]))

                                                    print('\n')
                                                    cont()

                        # sum = 0
                        # for i in range(0,5):
                        #     sum += investments[i]

            # The start of the buy option
            elif purchase == 'buy':
                stop = ''
                while agame.getInvestor().getWallet() > 0:
                    # summary of current stock market prices
                    print('Current Stock Prices:\n')
                    for s in range(0,5):
                        astock = prices[s]
                        print(str(s+1)+': ' + astock.getType() + ' : ' + str(astock.getValue()))
                    print('\n')
                    try:
                        stop = str(input("Type 'n' or 'no' to cancel purchasing stocks.\nOtherwise, hit 'enter' to continue."))
                    except:
                        print("You must declare 'n' or 'no'")
                    else:
                        # if the investors does not wish to purchase any more stocks
                        if stop == 'n' or stop == 'no':
                            print("Buy order cancelled")
                            break
                        else:
                            stockToBuy = int(input('Please enter the index number of the stock you wish to purchase:'))
                            print('\n')

                            # if the investor has not applied the correct input
                            if stockToBuy > 5 or stockToBuy < 0:
                                print('You must enter an index number linked to the stock of interest.\n')
                                cont()

                            # if the investor would like to buy stock
                            else:
                                stockToBuy -= 1
                                theStockName = ''
                                theStockPrice = 0
                                for s in range(0,5):
                                    if s == stockToBuy:
                                        theStock = prices[s]
                                        theStockName = theStock.getType()
                                        theStockPrice = theStock.getValue()
                                        print(theStockName + ": " + str(theStockPrice))
                                print('\n')
                                try:
                                    # verifies the stock being purchased
                                    verify = str(input('Is this the stock you would like? y/n\n'))
                                    print('\n')
                                except:
                                    print('You entered a number, please try again.\n')
                                    cont()
                                else:
                                    # ensures verification
                                    if verify == 'n' or verify == 'no':
                                        print('\n')
                                    elif verify == 'y' or verify == 'yes':
                                        try:
                                            # summary of current funds and current Stock holdings
                                            inv = agame.getInvestor()
                                            print('Your current funds: $' + str(inv.getWallet())+'.00\n')
                                            print('Your current investments: \n')
                                            invested = inv.getStockList()
                                            for i in range(0, 5):
                                                stockName = STOCKTYPE[i]
                                                investedQ = invested[i]
                                                print(stockName + ': ' + str(investedQ))
                                            print('\n')

                                            # Investor is queried as to how many stocks they would like to purchase
                                            print('Shares of '+theStockName+' '
                                                        + 'will cost you $'+ str(theStockPrice)+'.00 each.')
                                            quantity = int(input('How many '+ theStockName
                                                                 + ' stocks would you like to purchase?'))
                                        except:
                                            # purchases cannot be made in decimal format, only whole numbers
                                            print('You must enter a whole number.')
                                            cont()
                                        else:

                                            # purchase is correct and applied
                                            total = quantity * theStockPrice

                                            # an inveostors current funds and a summary of the purchase
                                            print('Your current funds: '+str(inv.getWallet())+'\n')
                                            verify = str(input(("Are you sure you would like to purchase "+ str(quantity)+
                                                  " "+theStockName+" stocks for a total of $"+str(total)+".00? y/n")))
                                            print('\n')

                                            # if the purchase is incorrect, it is cancelled
                                            if verify == 'n' or verify == 'no':
                                                print('Purchase has been cancelled.')
                                                cont()
                                                print('\n')

                                            # verifies that the investor has enough funding to make the purchase
                                            elif agame.getInvestor().getWallet() < total:
                                                print('You do not currently have enough funds to make this transaction.\n')
                                                print('Transaction has been cancelled\n')
                                                cont()

                                            # purchase goes through properly.
                                            elif verify == 'y' or verify == 'yes':
                                                change = total - 2*total
                                                agame.getInvestor().setWallet(change)
                                                inv.setStockQ(stockToBuy, quantity)
                                                agame.getStocks()[stockToBuy].reduceInvest()
                                                inv = agame.getInvestor()
                                                print('Transaction completed successfully.\n')
                                                print('Your current funds: ' + str(inv.getWallet())+'\n')
                                                print('Your current investments: \n')
                                                invested = inv.getStockList()
                                                for i in range(0, 5):
                                                    stockName = STOCKTYPE[i]
                                                    investedQ = invested[i]
                                                    print(stockName + ': ' + str(investedQ) + ' ' +
                                                              str(investedQ * agame.getStocks()[i].getValue()))
                                                print('\n')
                                                cont()
            # either no action taken, or actions are finished.

    # ends the round by changing the values
        rnd -= 1
        # this assigns random values to all stock investments
        if period < 2:
            agame.stockInvestSetInitial()
        else:
            agame.stockInvestSet()

        # this randomly assigns a trend
        agame.setCurrentTrend()
        # print(str(agame.getCurrentTrend()))
        # this grabs said trend
        trendIndex = random.randint(0, 2)
        # print('trend index: ' + str(trendIndex))

        aTrend = agame.getMarketTrends()[trendIndex]
        for i in range(0, 5):
            theStockInvestValue = agame.getStocks()[i].getInvest()
            if theStockInvestValue > 5:
                theStockInvestValue = 5
            elif theStockInvestValue < 0:
                theStockInvestValue = 0
            theChange = aTrend.getDPrice(i, theStockInvestValue)
            # print(str(theChange))
            agame.getStocks()[i].changeValue(theChange)
    # once game is over, the game should print out the investors final liquid tally.
    endWallet = agame.getInvestor().getWallet()

    # this adds the value of each stock to the investors wallet
    for n in range (0, 5):
        endGameValue = agame.getStocks()[n].getValue()
        endGameInventory = agame.getInvestor().getStockQ(n)
        endWallet += endGameInventory * endGameValue

    # printed sum of wallet.
    print('Your final liquid value is: ' + str(endWallet))

# initiate stock game
Main()