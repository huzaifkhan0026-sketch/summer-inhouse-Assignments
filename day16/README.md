Steps to Build the Project
Create employee.csv and add the employee dataset.
Create pyspark_app.py and write the PySpark RDD application.
Create requirements.txt and add:
pyspark==3.5.6

Create a Dockerfile with Java, Python, and Spark dependencies.
Build the Docker image:
docker build -t spark_rdd .

Run the Docker container:
Windows PowerShell
docker run --rm -v "${PWD}:/app" spark_rdd

Linux / macOS
docker run --rm -v $(pwd):/app spark_rdd

The application executes automatically and generates output.txt in the project directory.