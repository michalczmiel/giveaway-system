from diagrams import Diagram
from diagrams.onprem.client import User
from diagrams.aws.compute import Lambda
from diagrams.aws.storage import S3
from diagrams.aws.integration import SNS
from diagrams.aws.database import Dynamodb
from diagrams.aws.network import APIGateway

with Diagram("Giveaway System", filename="architecture", show=False):
    website_bucket = S3("website bucket")
    user = User()
    user >> website_bucket

    api_gateway = APIGateway("api gateway")
    website_bucket >> api_gateway

    get_giveaway_entry_lambda = Lambda("get-giveaway-entry")
    create_giveaway_entry_lambda = Lambda("create-giveaway-entry")
    api_gateway >> [create_giveaway_entry_lambda, get_giveaway_entry_lambda]

    entries_database = Dynamodb("entries database")
    create_giveaway_entry_lambda >> entries_database
    get_giveaway_entry_lambda << entries_database

    entries_topic = SNS("entries topic")
    create_giveaway_entry_lambda >> entries_topic

    notify_on_entry_lambda = Lambda("notify-on-entry")
    entries_topic >> notify_on_entry_lambda
