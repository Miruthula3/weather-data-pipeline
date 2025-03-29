import requests
import pandas as pd
import boto3
from datetime import datetime

print("Imports successful")

API_KEY = '1ef33e1f992da337d2c31b80ac30f4e1'
S3_BUCKET = 'bucket_name'
S3_FOLDER = 'weather-data/'

CITIES = ['Melbourne', 'Sydney', 'Brisbane', 'Perth', 'Adelaide']

def fetch_weather_data(city):
    print(f"Fetching weather data for {city}")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data for {city}. Response: {data}")
    
    return {
        'city': city,
        'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'weather': data['weather'][0]['description']
    }

def lambda_handler(event, context):
    print("Lambda handler started")
    weather_data = []

    for city in CITIES:
        try:
            print(f"Fetching data for: {city}")
            weather_data.append(fetch_weather_data(city))
        except Exception as e:
            print(f"Error fetching data for {city}: {e}")

    print("All data fetched. Converting to DataFrame")
    df = pd.DataFrame(weather_data)
    print(df)

    file_name = f'weather_data_{datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")}.parquet'
    temp_file = f'/tmp/{file_name}'

    print(f"Saving to Parquet: {temp_file}")
    df.to_parquet(temp_file, engine='pyarrow')

    s3 = boto3.client('s3')
    print(f"Uploading {file_name} to s3://{S3_BUCKET}/{S3_FOLDER}")
    s3.upload_file(temp_file, S3_BUCKET, f'{S3_FOLDER}{file_name}')

    print(f"Uploaded {file_name} to s3://{S3_BUCKET}/{S3_FOLDER}")

    return {
        'statusCode': 200,
        'body': f'Successfully uploaded {file_name} to {S3_BUCKET}/{S3_FOLDER}'
    }

if __name__ == '__main__':
    print("Running script directly...")
    lambda_handler({}, {})
