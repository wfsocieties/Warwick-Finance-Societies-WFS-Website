from flask import Flask, render_template, request, jsonify
import os
import requests
import urllib.parse

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("home.html")

@app.route("/executivesAndDivisions", methods=["POST","GET"])
def executivesAndDivisions():
    return render_template("executivesAndDivisions.html")

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

@app.route("/divisionAlternatives", methods=["POST","GET"])
def divisionAlternatives():
    return render_template("divisionAlternatives.html")

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

@app.route("/divisionShard", methods=["POST","GET"])
def divisionShard():
    return render_template("divisionShard.html")

@app.route("/divisionAlumni", methods=["POST","GET"])
def divisionAlumni():
    return render_template("divisionAlumni.html")

@app.route("/divisionTech", methods=["POST","GET"])
def divisionTech():
    return render_template("divisionTech.html")

@app.route("/divisionPhotographer", methods=["POST","GET"])
def divisionPhotographer():
    return render_template("divisionPhotographer.html")

@app.route("/divisionTour", methods=["POST","GET"])
def divisionTour():
    return render_template("divisionTour.html")

@app.route("/divisionSocials", methods=["POST","GET"])
def divisionSocials():
    return render_template("divisionSocials.html")

@app.route("/divisionBall", methods=["POST","GET"])
def divisionBall():
    return render_template("divisionBall.html")

@app.route("/divisionSport", methods=["POST","GET"])
def divisionSport():
    return render_template("divisionSport.html")

@app.route("/divisionAdvisory", methods=["POST","GET"])
def divisionAdvisory():
    return render_template("divisionAdvisory.html")

@app.route("/divisionBoard", methods=["POST","GET"]) 
def divisionBoard():
    return render_template("divisionBoard.html")

# Form for webhooks
@app.route("/webhook", methods=["POST"])
def tallyWebhook():
    try:
        print("Webhook received!")
        payload = request.json
        print("Payload:", payload)

        # Extract data from payload
        fields = payload.get('data', {}).get('fields', [])
        
        division = None
        fileURL = None

        for field in fields:
            if field.get('type') == 'DROPDOWN' and 'value' in field:
                # Get division text from options
                division = field.get('options', [{}])[0].get('text', 'Unknown')
            elif field.get('type') == 'FILE_UPLOAD' and 'value' in field:
                # Extract file URL from the list of file objects
                fileURL = field.get('value', [{}])[0].get('url')

        if division and fileURL:
            # Sanitise file name to remove query parameters
            fileName = urllib.parse.unquote(fileURL.split("/")[-1].split("?")[0])
            folderPath = os.path.join("uploads", division)
            os.makedirs(folderPath, exist_ok=True)

            filePath = os.path.join(folderPath, fileName)

            # Check if URL and file are accessible
            try:
                fileResponse = requests.get(fileURL)

                if fileResponse.status_code == 200:
                    with open(filePath, "wb") as f:
                        f.write(fileResponse.content)
                    return jsonify({"status": "success", "file_path": filePath})
                else:
                    return jsonify({"status": "failed", "message": "Failed to retrieve file"}), 400
            except Exception as e:
                return jsonify({"status": "error", "message": "Error retrieving file"}), 500
        
        return jsonify({"status": "failed", "message": "data not found"})
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

# Ensures framework works
if __name__ == "__main__":
    app.run(debug=True)
