from flask import Flask,render_template,request	#pip install Flask
app = Flask(__name__)

def stockCapitalGain(allotment,finalSharePrice,sellCommission,initialSharePrice,buyCommission,capitalGainTaxRate):
    global proceeds,cost,netProfit, returnOnInvestment,breakEvenSharePrice,capitalGain,cpaitalGainTax
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


@app.route("/", methods=['POST', 'GET'])
def hello():
    error = None
    if request.method == 'POST':
        stockSymbol = request.form['TickerSymbol']
        allotment = float(request.form['Allotment'])
        finalSharePrice = float(request.form['FinalSharePrice']) 
        sellCommission = float(request.form['SellCommission']) 
        initialSharePrice = float(request.form['InitialSharePrice'])
        buyCommission = float(request.form['BuyCommission'])
        capitalGainTaxRate = float(request.form['CapitalGainTaxRate'])
        stockCapitalGain(allotment,finalSharePrice,sellCommission,initialSharePrice,buyCommission,capitalGainTaxRate)
        return render_template('stock.html',TickerSymbol=stockSymbol, allotment = allotment, finalSharePrice = finalSharePrice,
        									sellCommission=sellCommission, initialSharePrice=initialSharePrice,
        									buyCommission=buyCommission, capitalGainTaxRate=capitalGainTaxRate,
        									proceeds='{:,.2f}'.format(proceeds),
        									cost= '{:,.2f}'.format(cost),
        									netProfit = '{:,.2f}'.format(netProfit),
        									returnOnInvestment = '{:,.2f}'.format(returnOnInvestment),
        									breakEvenSharePrice = '{:,.2f}'.format(breakEvenSharePrice),
        									capitalGain = '{:,.2f}'.format(capitalGain),
        									cpaitalGainTax = '{:,.2f}'.format(cpaitalGainTax),
        									initialInvestment = '{:,.2f}'.format(initialSharePrice*allotment)        									
        						)        
    return render_template('stock.html')
    #return "Hello World!"




@app.route('/login', )
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)





@app.route('/hello/<name>')
def helloName(name=None):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()