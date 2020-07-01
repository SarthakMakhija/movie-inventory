import os
from pathlib import Path
from typing import Set

from flaskr.configuration import Configuration

dir_path = os.path.abspath(os.path.dirname(__file__))


class TestConfiguration(Configuration):
    SQLALCHEMY_DATABASE_URI = "postgresql://mmaster:mmaster@localhost:5432/movie_snapshots"
    # DEBUG = True
    X_API_KEY = "fake_x_api_key"
    OMDB_URL = "http://www.omdbapi.com"
    SNS_ENDPOINT_URL = "http://localhost:4575"
    SNS_TOPIC_NAME = "arn:aws:sns:us-east-1:000000000000:app-events-topic"
    SQS_ENDPOINT_URL = "http://localhost:4576"
    SQS_QUEUE_NAME = "http://localhost:4576/queue/service-queue"
    AWS_REGION = "us-east-1"
    LOGGING_CONFIG_PATH: Path = Path(f"{dir_path}/logging_test_config.yaml")
    TRACING_PATCHABLE_LIBRARIES: Set[str] = []
