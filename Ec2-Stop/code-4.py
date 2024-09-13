import boto3
region = "us-east-1"
ec2 = boto3.client('ec2', region_name=region)

# Retrieving information of all existing instances. 
ec2_list = ec2.describe_instances(InstanceIds=[])

instance_ids = []
for instance_list in ec2_list['Reservations'][0]['Instances']: 
    instance_ids.append(instance_list['InstanceId']) 

# Defining a function to stop all running instances.
def stop(instance_ids):
    for instanceId in instance_ids:
        ec2.stop_instances(InstanceIds=[instanceId])
        print("Instance ID: {} is now stopped".format(instanceId))
# Calling the stop function.
stop(instance_ids)