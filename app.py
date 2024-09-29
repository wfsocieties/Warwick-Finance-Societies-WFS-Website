from flask import Flask, render_template, request, jsonify
import os
import io
import requests
import urllib.parse
from googleapiclient.discovery import build 
from googleapiclient.http import MediaIoBaseUpload 
from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.errors import HttpError
import time 
import random

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

# Resources

# Upload files to cloud
def getGDriveService():
    serviceAccountFile = '/home/WarwickFinanceSocieties/serviceKey.json'
    SCOPES = ['https://www.googleapis.com/auth/drive']

    creds = service_account.Credentials.from_service_account_file(serviceAccountFile, scopes=SCOPES)

    driveService = build("drive", "v3", credentials=creds)
    return driveService 

def getFolderID(folderName):
    driveService = getGDriveService()
    
    # Ensure this is the correct ID for "WFS Cloud"
    parentFolderID = "1q1MFF0mkI-H4VNrLaSn03Zkg7-jl6rGh"

    # List all folders in the specified parent folder
    try:
        query = f"'{parentFolderID}' in parents and mimeType='application/vnd.google-apps.folder' and trashed=false"
        
        print(f"Debug Query for listing folders: {query}")  # Log the query
        
        # Execute the query
        results = driveService.files().list(q=query, fields="files(id, name)").execute()
        folders = results.get("files", [])
        
        if folders:
            print("Folders found in the specified parent folder:")
            for folder in folders:
                print(f"Folder Name: {folder['name']}, Folder ID: {folder['id']}")
        else:
            print("No folders found in the specified parent folder.")
            
    except Exception as e:
        print(f"Error retrieving folders: {str(e)}")  # Log any errors
    
    # Adjusted query to search for a specific folder name
    query = f"name='{folderName}' and mimeType='application/vnd.google-apps.folder' and '{parentFolderID}' in parents and trashed=false"
    
    print(f"Debug Query for searching folder '{folderName}': {query}")  # Log the query
    
    try:
        results = driveService.files().list(q=query, fields="files(id, name)").execute()
        folders = results.get("files", [])
        
        if folders:
            print(f"Folder found: {folders[0]['name']} with ID: {folders[0]['id']}")  # Log found folder
            return folders[0]["id"]
        else:
            print(f"No folder found for: {folderName}")  # Log no folder found
            
            # List all subfolders in the parent folder for debugging
            allFolders = driveService.files().list(q=f"'{parentFolderID}' in parents and mimeType='application/vnd.google-apps.folder'",
                                                   fields="files(id, name)").execute()
            allFoldersList = allFolders.get("files", [])
            print("Subfolders in parent folder for debugging:")
            for folder in allFoldersList:
                print(f"Folder Name: {folder['name']}, Folder ID: {folder['id']}")
                
            return None
    except Exception as e:
        print(f"Error retrieving folder ID: {str(e)}")  # Log any errors
        return None

@app.route("/webhook", methods=["POST"])
def formsWebhook():
    try:
        print("Webhook received!")
        payload = request.json
        print("Payload:", payload)

        fields = payload.get('data', {}).get('fields', [])
        
        division = None
        fileURL = None

        for field in fields: 
            if field.get("type") == "DROPDOWN" and "value" in field:
                division = next((option['text'] for option in field.get('options', []) if option['id'] in field['value']), None)
                print(f"Division selected: {division}")  # Log selected division

            elif field.get("type") == "FILE_UPLOAD" and "value" in field:
                fileURL = field.get('value', [{}])[0].get('url')
                print(f"File URL: {fileURL}")  # Log file URL

        if division and fileURL:
            print(division + " THIS IS THE DIVISION NAME")
            folderID = getFolderID(division)

            if not folderID: 
                print("Warning: Division folder not found in Google Drive")  # Warning message
                return jsonify({"status": "failed", "message": "Division folder not found in Google Drive"}), 400
            
            # Add initial delay before fetching the file
            time.sleep(3)  # Wait for 3 seconds

            fileResponse = requests.get(fileURL)
            print(f"File response status: {fileResponse.status_code}")  # Log file response status

            if fileResponse.status_code == 200:
                fileName = urllib.parse.unquote(fileURL.split("/")[-1].split("?")[0])
                print(f"File name determined: {fileName}")  # Log determined file name

                media = MediaIoBaseUpload(io.BytesIO(fileResponse.content), mimetype=fileResponse.headers['Content-Type'])
                
                driveService = getGDriveService() 
                fileMetadata = {
                    "name": fileName,
                    "parents": [folderID]
                }
                
                # Initialize retry parameters
                max_retries = 5
                for attempt in range(max_retries):
                    try:
                        # Upload file to Google Drive
                        driveService.files().create(body=fileMetadata, media_body=media, fields="id").execute()
                        print(f"File '{fileName}' uploaded successfully to folder ID: {folderID}")  # Log success
                        return jsonify({"status": "success", "file_name": fileName}), 200
                    except HttpError as e:
                        if e.resp.status == 429:  # Too Many Requests
                            wait_time = 2 ** attempt + random.uniform(0, 1)  # Exponential backoff with jitter
                            print(f"Rate limit exceeded. Retrying in {wait_time:.2f} seconds...")
                            time.sleep(wait_time)
                        else:
                            print(f"An error occurred during file upload: {str(e)}")
                            break  # Break if it's not a rate limit issue
                
                print("Max retries reached. File upload failed.")
                return jsonify({"status": "failed", "message": "File upload failed after multiple attempts"}), 500
            
            else:
                print(f"Failed to retrieve file: {fileResponse.status_code} - {fileResponse.text}")  # Log failure
                return jsonify({"status": "failed", "message": "Failed to retrieve file"}), 400

        print("Data not found in the payload")  # Log no data found
        return jsonify({"status": "failed", "message": "Data not found"}), 400
    
    except Exception as e:
        print(f"Error occurred in webhook: {str(e)}")  # Log the error
        return jsonify({"status": "error", "message": str(e)}), 500
    
# Get files from Google Drive folder
def getFilesInFolder(folderID):
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

    serviceAccountFile = '/home/WarwickFinanceSocieties/serviceKey.json'
    creds = service_account.Credentials.from_service_account_file(serviceAccountFile, scopes=SCOPES)
    driveService = build("drive", "v3", credentials=creds)

    try:
        results = driveService.files().list(
            q=f"'{folderID}' in parents and trashed=false",
            fields="files(id, name, mimeType, webContentLink, createdTime)",
            orderBy="createdTime desc"  # Sort by created time in descending order
        ).execute()
        
        return results.get("files", [])
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

# Resource pages
# Resource hub
@app.route("/resourcesHub", methods=["POST","GET"])
def resourcesHub(): 
    return render_template("resourcesHub.html")

# Markets
@app.route("/marketsResources")
def marketsResources():
    folderID = "12cb6VLtd-hv3zNr9nzg0MpkHiZ-PfPjL"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("marketsResources.html", files=files)

# Quant Finance
@app.route("/quantFinanceResources")
def quantFinanceResources():
    folderID = "1plTvwABxYHPjbMTMvjdrFhtkI2vHqEUE"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("quantFinanceResources.html", files=files)

# Investment Banking
@app.route("/investmentBankingResources")
def investmentBankingResources():
    folderID = "1RoeMko0CENKyIw0d8n29njSmdvU2s80f"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("investmentBankingResources.html", files=files)

# Alternatives
@app.route("/alternativesResources")
def alternativesResources():
    folderID = "1-gb6ZKnEpPRZR8XaBCfpVvFVMTlSOUlq"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("alternativesResources.html", files=files)

# Fintech
@app.route("/fintechResources")
def fintechResources():
    folderID = "17j84nZiisC1tc6GJ00wsYtDJy0DbNFgs"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("fintechResources.html", files=files)

# WIF
@app.route("/wifResources")
def wifResources():
    folderID = "1tBZP5p4oxyLLDeWzRvBsYANyow76a8ie"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("wifResources.html", files=files)

# Insights
@app.route("/insightsResources")
def insightsResources():
    folderID = "124FTau0kNnfcw03J_zqIPqaVlYcitofy"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("insightsResources.html", files=files)

# Speaker Series
@app.route("/speakerSeriesResources")
def speakerSeriesResources():
    folderID = "14jisQWA2f0XkVp_z9n-bs82zqNDZ1k-m"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("speakerSeriesResources.html", files=files)

# Careers
@app.route("/careersResources")
def careersResources():
    folderID = "16UwERHPBlrUYFUeS8Oh2mKF03WNgQiTV"  # This is the folder ID in Google Drive
    files = getFilesInFolder(folderID)
    return render_template("careersResources.html", files=files)

# Ensures framework works
if __name__ == "__main__":
    app.run(debug=True)
