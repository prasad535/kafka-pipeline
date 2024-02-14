import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s - %(message)s]")

project = "src"

list_of_files = [
    "sample_data/kafka-topic",
    "experiments/trails.ipynb",
    f"{project}/__init__.py",
    f"{project}/constant/__init__.py",
    f"{project}/database/__init__.py",
    f"{project}/database/mongodb.py",
    f"{project}/entity/__init__.py",
    f"{project}/entity/generic.py",
    f"{project}/kafka_config/__init__.py",
    f"{project}/kafka_consumer/__init__.py",
    f"{project}/kafka_cosumer/json_consumer.py",
    f"{project}/kafka_logger/__init__.py",
    f"{project}/kafka_producer/__init__.py",
    f"{project}/kafka_producer/json_producer.py",
    "Dockerfile",
    "producer_main.py",
    "consumer_main.py",
    "requirements.txt",
    "setup.py",
    "schema.json",
    "start.sh",
    "test.py"
]

for file in list_of_files:

    filepath = Path(file)

    filedir, filename = os.path.split(filepath)

    if filedir != "":

        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(path) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty: {filename}")
    else:
        logging.info(f"{filename} : is already exists")