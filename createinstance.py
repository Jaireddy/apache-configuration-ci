#!/ usr/bin/python
import boto3
import sys

ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-922914f7',
    MinCount=1,
    MaxCount=count,
    KeyName="jai-keys",
    SecurityGroups=["opentoworld"],
    InstanceType='t2.micro')
print instance[0].id
