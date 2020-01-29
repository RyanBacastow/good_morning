from os import environ as env
import boto3


def publish_message_sns(sns_client, sns_arn, message):
    try:
        response = sns_client.publish(
            TopicArn=sns_arn,
            Message=message
        )

        if response is None:
            raise Exception("No Response.")

    except Exception as e:
        print("ERROR PUBLISHING MESSAGE TO SNS: {}".format(e))


def handler(event, context):
    if event:
        sns_client = boto3.client('sns')
        sns_arn = env['SNS_ARN']
        message = "Good Morning! Here's your journal: {}. Do future you a favor today.".format(env['JOURNAL_URL'])

        publish_message_sns(
            sns_client,
            sns_arn,
            message
        )
