import boto3
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')


region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

# Data Input
# Instance IDs stored as a dictionary....(key-value pair)
instance_id = {'id':'i-0fe84f2be7f19fc49'} 

# Business Logic
# Retrieving the id of the instance using the key.
ec2.stop_instances(InstanceIds=[instance_id['id']]) 
logging.info("Instance ID: {} is now stopped".format(instance_id))
