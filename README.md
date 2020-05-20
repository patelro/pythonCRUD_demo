# pythonCRUD_demo

How to deploy a Pyhton Flask web application on Google Cloud Platform 

1. Create a Cloud SQL Instance. 
Instructions: https://cloud.google.com/sql/docs/mysql/create-instance

2. Create a database in your Cloud SQL Instance. 
Instructions: https://cloud.google.com/sql/docs/mysql/create-manage-databases

3. Change the envirnment variables in app.yaml
env_variables:
  CLOUD_SQL_USERNAME: "YOUR_USERNAME" // root user 
  CLOUD_SQL_PASSWORD: "YOUR_PASSWORD" // root password
  CLOUD_SQL_DATABASE_NAME: "DATABASE_NAME" // name of the database in the SQL Instance
  CLOUD_SQL_CONNECTION_NAME: "CLOUD_SQL_INSTANCE_NAME" // MY-PROJECT:INSTANCE-REGION:INSTANCE-NAME

4. Deploy it to the Cloud
Instructions: https://cloud.google.com/appengine/docs/standard/python3/quickstart#before-you-begin
  - run the command "gcloud init" to initialize the sdk
  - run the command "gcloud app deploy" to deploy it to the App Engine
