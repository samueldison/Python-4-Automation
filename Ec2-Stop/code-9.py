import boto3
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

# Define AWS region
region = "us-east-1"

# Create EC2 client
ec2 = boto3.client('ec2', region_name=region)

# Retrieve information of all available (running/stopped) instances
ec2_list = ec2.describe_instances()

# Initialize list to store instance IDs to stop
instance_ids = []

def read_file():
    """
    Read the tags from the tags.txt file and process each tag.
    """
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get directory of the script
    file_path = os.path.join(script_dir, "tags.txt")          # Construct absolute file path
    try:
        with open(file_path, mode='r') as file_data:
            for tag in file_data.readlines():
                tag_value = tag.strip()
                logging.info("Retrieving instance tag value: {}".format(tag_value))
                generate_instance_list(tag_value)
    except FileNotFoundError:
        logging.error("File '{}' not found.".format(file_path))
    except Exception as e:
        logging.error("An error occurred while reading the file: {}".format(str(e)))

def generate_instance_list(tag_value):
    """
    Generate a list of instance IDs based on the tag value.
    """
    try:
        for reservation in ec2_list['Reservations']:
            for instance in reservation['Instances']:
                for tag in instance['Tags']:
                    if tag['Key'] == "Name" and tag['Value'] == tag_value:
                        if instance['State']['Name'] == "stopped":
                            logging.info("Instance {} is already stopped".format(instance['InstanceId']))
                        else:
                            instance_ids.append(instance['InstanceId'])
    except KeyError:
        logging.error("KeyError: Unable to find 'Reservations' or 'Instances' key in EC2 response.")
    except Exception as e:
        logging.error("An error occurred while processing instances: {}".format(str(e)))

def stop_instances(instance_ids):
    """
    Stop the instances with the specified instance IDs.
    """
    try:
        if not instance_ids:
            logging.info("No instances to stop.")
            return

        ec2.stop_instances(InstanceIds=instance_ids)
        logging.info("Initiated stop for instances: {}".format(instance_ids))

        for instance_id in instance_ids:
            while True: 
                instance_data = ec2.describe_instances(InstanceIds=[instance_id])
                state = instance_data['Reservations'][0]['Instances'][0]['State']['Name']
                if state == 'stopped':
                    logging.info("Instance ID: {} is now stopped".format(instance_id))
                    break
                else:
                    logging.info("Waiting for instance ID: {} to stop...".format(instance_id))
    except Exception as e:
        logging.error("An error occurred while stopping instances: {}".format(str(e)))

# Main script execution
if __name__ == "__main__":
    read_file()
    stop_instances(instance_ids)
