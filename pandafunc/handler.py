
import requests
import pandas as pd

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    
    download_url = "https://www.datos.gov.co/resource/jhpq-24h2.csv"
target_csv_path = "jhpq-24h2.csv"

response = requests.get(download_url)
response.raise_for_status()    # Check that the request was successful
with open(target_csv_path, "wb") as f:
    f.write(response.content)
#print("Download ready.")
nba = pd.read_csv("jhpq-24h2.csv")
type(nba)
    return req
