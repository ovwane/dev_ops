#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'ovwane'
__time__ = '2017.12.11 10:29'


import boto3


ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
