from flask import Flask, render_template 
app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/divisions", methods=["POST","GET"])
def divisions():
    return render_template("divisions.html")

@app.route("/aboutUs", methods=["POST","GET"])
def aboutUs():
    return render_template("aboutus.html")

@app.route("/sponsors", methods=["POST","GET"])
def sponsors():
    return render_template("sponsors.html")

@app.route("/divisionSpecificTemp", methods=["POST","GET"])
def divisionSpecificTemp():
    return render_template("divisionSpecificTemp.html")

# Specific divisions
@app.route("/divisionMarkets", methods=["POST","GET"])
def divisionMarkets():
    return render_template("divisionMarkets.html")

@app.route("/divisionQuantFinance", methods=["POST","GET"])
def divisionQuantFinance():
    return render_template("divisionQuantFinance.html")

@app.route("/divisionInvestmentBanking", methods=["POST","GET"])
def divisionInvestmentBanking():
    return render_template("divisionInvestmentBanking.html")

@app.route("/divisionVentureCapitalAndPrivateEquity", methods=["POST","GET"])
def divisionVentureCapitalAndPrivateEquity():
    return render_template("divisionVentureCapitalAndPrivateEquity.html")

@app.route("/divisionFintech", methods=["POST","GET"])
def divisionFintech():
    return render_template("divisionFintech.html")

@app.route("/divisionWomenInFinanceAndDiversity", methods=["POST","GET"])
def divisionWomenInFinanceAndDiversity():
    return render_template("divisionWomenInFinanceAndDiversity.html")

@app.route("/divisionInsights", methods=["POST","GET"])
def divisionInsights():
    return render_template("divisionInsights.html")

@app.route("/divisionStrategyAndMarketing", methods=["POST","GET"])
def divisionStrategyAndMarketing():
    return render_template("divisionStrategyAndMarketing.html")

@app.route("/divisionSponsorship", methods=["POST","GET"]) 
def divisionSponsorship():
    return render_template("divisionSponsorship.html")

@app.route("/divisionSpeakerSeries", methods=["POST","GET"])
def divisionSpeakerSeries():
    return render_template("divisionSpeakerSeries.html")

@app.route("/divisionCareers", methods=["POST","GET"])
def divisionCareers():
    return render_template("divisionCareers.html")
    
# Ensures framework works
if __name__ == "__main__":
    app.run(debug=True)
