from google.cloud import bigquery
from google.oauth2 import service_account
from pathlib import Path
import pandas as pd


path = Path.home() / 'PycharmProjects/analytics-training-samples'

def run_bigquery_to_df(sql_script: str)-> pd.DataFrame:
   # credentials 
   project_id = 'analytics-training-363804'
   credentials = service_account.Credentials.from_service_account_file(path/'credentials/analytics-training-363804-69390f659e9b.json')

   # covert to dataframe
   df = pd.read_gbq(query=sql_script, project_id=project_id, credentials=credentials)
   return df



