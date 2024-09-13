# Stop EC2 servers with (webservers) as tags:
import boto3
region = "us-east-1"
ec2 = boto3.client('ec2', region_name=region)
 
# Retrieving information of all existing (running/stopped) instances
ec2_list = ec2.describe_instances(InstanceIds=[])

# Extracting instance IDs from the response
instance_ids = []

for instance_list in ec2_list['Reservations'][0]['Instances']:
    for tag_list in instance_list['Tags']:
        if tag_list['Key'] == "Name": 
            if tag_list['Value'] == "webserver":
                if instance_list['State']['Name'] == "stopped":
                    print ("Instance {} is already stopped".format(instance_list['InstanceId']))
                else:
                    instance_ids.append(instance_list['InstanceId'])
                           
# Defining a function to stop running instances
def stop(instance_ids):
    for instanceId in instance_ids:
       ec2.stop_instances(InstanceIds=[instanceId])
       instance_data = ec2.describe_instances(InstanceIds=[instanceId])
       while True:
          state = instance_data['Reservations'][0]['Instances'][0]['State']['Name']
          if state == 'stopped':
            print("Instance ID: {} is now stopped".format(instanceId))
            break
        
# Calling the stop function
stop(instance_ids)