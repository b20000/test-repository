class CoinChange(object):
    '''
    def dpMakeChange(coinValueList,change,minCoins):
        for cents in range(change+1):
            coinCount = cents
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                   coinCount = minCoins[cents-j]+1
            minCoins[cents] = coinCount
 
        return minCoins[change]
    '''
    def dpMakeChange(self,coinValueList,change,minCoins,coinsUsed):
        for cents in range(change+1):
            coinCount = cents
            newCoin = 1
            for j in [c for c in coinValueList if c <= cents]:
                if minCoins[cents-j] + 1 < coinCount:
                    coinCount = minCoins[cents-j]+1
                    newCoin = j
            minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
        return minCoins[change]

    def printCoins(self,coinsUsed,change):
        coin = change
        while coin > 0:
            thisCoin = coinsUsed[coin]
            print thisCoin
            coin = coin - thisCoin
            
if __name__ == '__main__':
        
    amnt = 63
    #clist = [1,5,10,21,25]
    clist = [1,5,10,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print "Making change for " + str( amnt) + " requires :"   
    print str(CoinChange().dpMakeChange(clist,amnt,coinCount,coinsUsed))+ " coins"
    #print("They are:")
    #CoinChange().printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)