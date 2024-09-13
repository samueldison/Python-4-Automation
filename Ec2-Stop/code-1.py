import boto3
region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

# describes/retrieves specific instances or all instances.
ec2_list = ec2.describe_instances(InstanceIds=[])

ec2_1 = ec2_list['Reservations'][0]['Instances'][0]['InstanceId']
ec2_2 = ec2_list['Reservations'][0]['Instances'][1]['InstanceId']
ec2_3 = ec2_list['Reservations'][0]['Instances'][2]['InstanceId']

# business logic
ec2.stop_instances(InstanceIds=[ec2_1])
ec2.stop_instances(InstanceIds=[ec2_2])
ec2.stop_instances(InstanceIds=[ec2_3])
