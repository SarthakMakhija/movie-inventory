import os
import time

from flask_script import Manager

from main import app

manager = Manager(app)


def docker_compose_up():
    base_directory = os.getcwd()
    os.system(f"docker-compose -f {base_directory}/tests/docker-compose.yml up -d")


def docker_compose_down():
    base_directory = os.getcwd()
    os.system(f"docker-compose -f {base_directory}/tests/docker-compose.yml down")


def run_migrations():
    base_directory = os.getcwd()
    os.system(f"python3 {base_directory}/tests/migration/migration_execution_test.py db upgrade")


def create_sns_topic():
    os.system(f"aws sns create-topic --name app-events-topic --endpoint-url=http://localhost:4575")


def create_sqs_queue():
    os.system(f"aws sqs create-queue --queue-name service-queue --endpoint-url=http://localhost:4576")
    os.system(
        f"aws sns subscribe --topic-arn=arn:aws:sns:us-east-1:000000000000:app-events-topic --protocol sqs --notification-endpoint http://localhost:4576/queue/service-queue --attributes RawMessageDelivery=true --endpoint-url=http://localhost:4575")


def setup_event_store():
    create_sns_topic()
    create_sqs_queue()


def run_test_for(pattern: str):
    os.system(f"python3 -m unittest discover -s tests/ -p {pattern}")


@manager.command
def unit():
    run_test_for("test_unit_*.py")


@manager.command
def integration():
    docker_compose_up()
    time.sleep(30)
    run_migrations()
    setup_event_store()
    run_test_for("test_integration_*.py")
    docker_compose_down()


@manager.command
def all():
    unit()
    integration()


if __name__ == "__main__":
    manager.run()
