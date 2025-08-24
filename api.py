import requests

def getWaterData():
    url = "https://aikosha-api.indiaai.gov.in/akp/idp/api/v1/dataset-public/download-dataset?datasetIdentifier=jjm_water_source_water_quality_data&versionNumber=1"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data.")
        exit(1)

    data = response.json()
    