import boto3
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

region = "us-east-1"
ec2 = boto3.client('ec2', region_name=region)

# Retrieving information of all existing (running) instances
ec2_list = ec2.describe_instances(InstanceIds=[])

# Extracting instance IDs from the response
instance_ids = []

def read_file():
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get directory of the script
    file_path = os.path.join(script_dir, "tags.txt")          # Construct absolute file path
    with open(file_path, mode='r') as file_data:
        for tag in file_data.readlines():
            tag_value = tag.strip()
            logging.info("Retrieving instance tag values: {}".format(tag_value))
            generate_instance_list(tag_value)
   
def generate_instance_list(tag_value):
    for instance_list in ec2_list['Reservations'][0]['Instances']:
        for tag_list in instance_list['Tags']:
               if tag_list['Key'] == "Name" and tag_list['Value'] == tag_value:
                    if instance_list['State']['Name'] == "stopped":
                        logging.info("Instance {} is already stopped".format(instance_list['InstanceId']))
                    else:
                        instance_ids.append(instance_list['InstanceId'])
 
# Defining a function to stop running instances
def stop(instance_ids):
    for instanceId in instance_ids:
        ec2.stop_instances(InstanceIds=[instanceId])
        while True: 
            instance_data = ec2.describe_instances(InstanceIds=[instanceId])
            state = instance_data['Reservations'][0]['Instances'][0]['State']['Name']
            if state == 'stopped':
                logging.info("Instance ID: {} is now stopped".format(instanceId))
                break
# Calling the stop function
read_file()
stop(instance_ids)
