import boto3
region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

# data input (Extracting Data Using Python Data Types: string, list & dictionaries)
ec2_list = ec2.describe_instances(InstanceIds=[])

instance_ids = []
ec2_1 = ec2_list['Reservations'][0]['Instances'][0]['InstanceId']
ec2_2 = ec2_list['Reservations'][0]['Instances'][1]['InstanceId']
ec2_3 = ec2_list['Reservations'][0]['Instances'][2]['InstanceId']

instance_ids.append(ec2_1) # instance_ids = []
instance_ids.append(ec2_2) # By declaring an empty list and appending the existing instances (3) to the empty list,
instance_ids.append(ec2_3) # instance_ids becomes a place holder of the (3) instances.
  # ptint(instance_ids)  

# business logic:
def stop (instance_ids):
    for instanceId in instance_ids:
        ec2.stop_instances(InstanceIds=[instanceId])
        print("Instance ID: {} is now stopped".format (instanceId))
stop(instance_ids)