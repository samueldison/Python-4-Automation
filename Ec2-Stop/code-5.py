import boto3
region = "us-east-1"
ec2 = boto3.client('ec2', region_name=region)

# Retrieving information of all existing (running/stopped) instances.
ec2_list = ec2.describe_instances(InstanceIds=[])

# Extracting instance IDs from the response.
instance_ids = []

for instance_list in ec2_list['Reservations'][0]['Instances']:
    for tag_list in instance_list['Tags']:
        if tag_list['Key'] == "Name" and tag_list['Value'] == "webserver":
            instance_ids.append(instance_list['InstanceId'])   
                                
# Defining a function to stop running instances.
# Looping through the list of instance IDs.
def stop(instance_ids):
    for instanceId in instance_ids:
        ec2.stop_instances(InstanceIds=[instanceId])
        print ("Instance ID: {} is now stopped".format(instanceId))
       
# Calling the stop function
stop(instance_ids)