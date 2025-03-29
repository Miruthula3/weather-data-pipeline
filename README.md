# weather-data-pipeline
This is a repository to store all files related to my weather data pipeline, that extracts data from an API and stores them in AWS S3 database as parquet files.

#Project Title & Description
Weather Data Pipleine (Public API Ingestion):
This pipeline extracts data from OpenWeatherMap API to collect daily weather data for 5 cities.

#Tech Stack (e.g., Python, AWS Lambda, S3, Pandas):
Use OpenWeatherMap API to collect daily weather data for 5 cities.
Store data in S3 in parquet format.

Installation Steps:
Write code in Python locally and use the .py file in AWS Lambda with AWS SDK Layer for installing depency packages and libraries like pandas, boto3 and request.
Set up lamba configuration runtime to 15 seconds.
Used Python version is Python 3.17 for both function and layer to be compatible.
Set up S3 bucket and folder to store parquet files.


How It Works:
Data Fetching: The weather data for cities (Melbourne, Sydney, Brisbane, Perth, Adelaide) was successfully fetched using the OpenWeatherMap API.
Data Processing: The weather data was converted into a Pandas DataFrame.
Saving to Parquet: The DataFrame was saved as a Parquet file at /tmp/weather_data_2025-03-28_12-21-41.parquet.
Uploading to S3: The Parquet file was uploaded to the S3 bucket weather-miru-bucket under the weather-data/ folder.

Example Output:


Future Enhancements:
Use Glue Crawler to create tables.
Use Athena (SQL) to query data for temperature trends, etc.
Add Lambda Trigger to run daily
