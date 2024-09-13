import boto3
region = 'us-east-1'
ec2 = boto3.client('ec2', region_name=region)

# Data input:
ec2_list = ec2.describe_instances(InstanceIds=[])
ec2_1 = ec2_list['Reservations'][0]['Instances'][0]['InstanceId']
ec2_2 = ec2_list['Reservations'][0]['Instances'][1]['InstanceId']
ec2_3 = ec2_list['Reservations'][0]['Instances'][2]['InstanceId']

# Business logic:
# (instance_id) is a variable that iterates through the list of ec2 instances.
# Every time the function is called it picks up a value and gives an output/InstanceID.
#
def stop(instance_id):
    ec2.stop_instances(InstanceIds=[instance_id])
    print ("Instance ID: {} is now stopped".format (instance_id))
stop(ec2_1)
stop(ec2_2)
stop(ec2_3)