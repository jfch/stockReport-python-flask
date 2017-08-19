def stockCapitalGain(allotment,finalSharePrice,sellCommission,initialSharePrice,buyCommission,capitalGainTaxRate):
    
    proceeds=allotment*finalSharePrice    
    cost= allotment*initialSharePrice+sellCommission+buyCommission+(allotment*finalSharePrice-(allotment*initialSharePrice
        +sellCommission+buyCommission))*capitalGainTaxRate/100
    netProfit = proceeds - cost
    returnOnInvestment = netProfit/(allotment*initialSharePrice) *100
    breakEvenSharePrice = (allotment*initialSharePrice+sellCommission+buyCommission)/allotment
    print("\n***PROFIT REPORT***");
    #print("Proceeds\n$"+ str(proceeds) +"\n");      #1,000.00; keep two decimal
    str1="Proceeds\n$"+ '{:,.2f}'.format(proceeds) + "\n"
    print(str1);  #1,000.00; keep two decimal
    print("Cost\n$"+ '{:,.2f}'.format(cost)+"\n");
    print("Cost details");
    print("Total Purchase Price:");
    print('{:,.2f}'.format(allotment) + " X $" + '{:,.2f}'.format(initialSharePrice) + " = " + '{:,.2f}'.format(initialSharePrice*allotment));
    print("Buy Commission = " + '{:,.2f}'.format(buyCommission));
    print("Sell Commission = " + '{:,.2f}'.format(sellCommission));
    capitalGain = allotment*finalSharePrice-(allotment*initialSharePrice+sellCommission+buyCommission)
    cpaitalGainTax = capitalGain * capitalGainTaxRate/100
    print("Tax on Capital Gain = " + '{:,.2f}'.format(capitalGainTaxRate) + "% of $" + '{:,.2f}'.format(capitalGain) + " = " + '{:,.2f}'.format(cpaitalGainTax));
    print("\nNet Profit")
    print("$" + '{:,.2f}'.format(netProfit));
    print("\nReturn on Investment")
    print('{:,.2f}'.format(returnOnInvestment) +"%");
    print("\nTo break even, you should have a final share price of")
    print("$" + '{:,.2f}'.format(breakEvenSharePrice));




if __name__ == '__main__':
    print("Compute Your Profit:")
    stockSymbol = raw_input("\nStock Symbol: \n")
    allotment = float(raw_input("\nAllotment(number of shares): \n"))
    finalSharePrice = float(raw_input("\nFinal Share Price(in dollars): \n"))
    sellCommission = float(raw_input("\nSell Commission(in dollars): \n"))
    initialSharePrice = float(raw_input("\nInitial Share Price(in dollars): \n"))
    buyCommission = float(raw_input("\nBuy Commission(in dollars): \n"))
    capitalGainTaxRate = float(raw_input("\nCapital Gain Tax Rate(in %): \n"))

    stockCapitalGain(allotment,finalSharePrice,sellCommission,initialSharePrice,buyCommission,capitalGainTaxRate)
