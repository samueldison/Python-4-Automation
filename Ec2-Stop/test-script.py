from unittest.mock import MagicMock, patch
import logging
import threading
import time

# Mock setup
mock_ec2 = MagicMock()

# Simulated EC2 instances data
mock_instances = {
    'Reservations': [
        {
            'Instances': [
                {'InstanceId': 'i-0123456789abcdef0', 'State': {'Name': 'running'}, 'Tags': [{'Key': 'Name', 'Value': 'webserver'}]},
                {'InstanceId': 'i-0abcdef1234567890', 'State': {'Name': 'running'}, 'Tags': [{'Key': 'Name', 'Value': 'appserver'}]},
                {'InstanceId': 'i-0fedcba9876543210', 'State': {'Name': 'stopped'}, 'Tags': [{'Key': 'Name', 'Value': 'appserver'}]},
            ]
        }
    ]
}

# Patch the boto3 client to return our mock EC2 client
@patch('boto3.client', return_value=mock_ec2)
def test_ec2_instance_stop(mock_boto_client):
    # Mocking describe_instances call to return our mock instances
    mock_ec2.describe_instances.return_value = mock_instances

    # Running the script's logic
    instance_ids = []
    ec2_list = mock_ec2.describe_instances()
    
    def generate_instance_list(tag_value, tag_key="Name"):
        for reservation in ec2_list['Reservations']:
            for instance in reservation['Instances']:
                for tag in instance['Tags']:
                    if tag['Key'] == tag_key and tag['Value'] == tag_value:
                        if instance['State']['Name'] == "stopped":
                            logging.info("Instance {} is already stopped".format(instance['InstanceId']))
                        else:
                            instance_ids.append(instance['InstanceId'])
    
    def stop_instances(instance_ids):
        def stop_instance(instance_id):
            logging.info(f"Initiating stop for instance {instance_id}.")
            while True: 
                instance_data = mock_ec2.describe_instances(InstanceIds=[instance_id])
                state = instance_data['Reservations'][0]['Instances'][0]['State']['Name']
                if state == 'stopped':
                    logging.info(f"Instance ID: {instance_id} is now stopped")
                    break
                else:
                    logging.info(f"Waiting for instance ID: {instance_id} to stop...")
                    # Simulate instance stopping
                    time.sleep(1)
                    # Update the mock to show the instance has stopped
                    for res in mock_instances['Reservations']:
                        for inst in res['Instances']:
                            if inst['InstanceId'] == instance_id:
                                inst['State']['Name'] = 'stopped'
        
        threads = []
        for instance_id in instance_ids:
            thread = threading.Thread(target=stop_instance, args=(instance_id,))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    # Simulate reading from 'tags.txt' (using a list instead)
    tags_to_process = ['webserver', 'appserver']

    for tag in tags_to_process:
        generate_instance_list(tag)

    stop_instances(instance_ids)
    return instance_ids

# Run the test and capture the output
instance_ids_stopped = test_ec2_instance_stop()
print (instance_ids_stopped)
