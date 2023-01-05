"""
File Related to AWS IAM Service using BOTO3.
Documentation URL https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/iam.html
"""
import json

import boto3


def create_user(username):
    """
    Section 2 number: 12
    :param username:
    :return:
    """
    iam = boto3.client('iam')
    response = iam.create_user(UserName=username)
    return response


def all_users():
    """
    Section 2 number: 13
    :return:
    """
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')

    for resp in paginator.paginate():
        for user in resp['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print(f"Username: {username} and Arn: {Arn}")


def update_user(old_name, new_name):
    """
    Section 2 number: 14
    :param old_name:
    :param new_name:
    :return:
    """
    iam = boto3.client('iam')
    response = iam.update_user(UserName=old_name, NewUserName=new_name)
    return response


def create_policy():
    """
    Section 2: number 15
    :return:
    """
    user_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }
    iam = boto3.client('iam')
    response = iam.create_policy(PolicyName='UserCustomPolicy', PolicyDocument=json.dumps(user_policy))
    return response


def list_policies():
    """
    Section 2: number 16
    :return:
    """
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_policies')

    # scope = Local means that only User create policy will be show and not AWS.
    # To list AWS policy use scope = AWS.
    for response in paginator.paginate(scope='Local'):
        for policy in response['Policies']:
            policy_name = policy['PolicyName']
            Arn = policy['Arn']
            print(f"Custom User Policy details. Policy_name: {policy_name} and Policy_ARN: {Arn}")


def attach_policy():
    """
    Section 2: Number 17
    :return:
    """
    username = 'testuser2'
    policy_arn = 'arn:aws:iam::880291223494:policy/UserCustomPolicy'
    iam = boto3.client('iam')
    response = iam.attach_user_policy(UserName=username, PolicyArn=policy_arn)
    return response


def detach_policy():
    """
    Section 2: Number 18
    :return:
    """
    username = 'testuser2'
    policy_arn = 'arn:aws:iam::880291223494:policy/UserCustomPolicy'
    iam = boto3.client('iam')
    response = iam.detach_user_policy(UserName=username, PolicyArn=policy_arn)
    return response


def create_group():
    """
    Section 2: Number 19
    :return:
    """
    group_name = 'RDSAdmins'
    iam = boto3.client('iam')
    response = iam.create_group(GroupName=group_name)
    return response


def attach_policy_to_group():
    """
    Section 2: Number 20
    :return:
    """
    group_name = 'RDSAdmins'
    policy_arn = 'arn:aws:iam::aws:policy/AmazonRDSDataFullAccess'
    iam = boto3.client('iam')
    response = iam.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
    return response


def add_user_group():
    """
    Section 2: Number 21
    :return:
    """
    username = 'testuser2'
    group_name = 'RDSAdmins'
    iam = boto3.client('iam')
    response = iam.add_user_to_group(UserName=username, GroupName=group_name)
    return response


def detach_policy_from_group():
    """
    Section 2: Number 22
    :return:
    """
    group_name = 'RDSAdmins'
    policy_arn = 'arn:aws:iam::aws:policy/AmazonRDSDataFullAccess'
    iam = boto3.client('iam')
    response = iam.detach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
    return response


def create_access_key_for_user():
    """
    Section 2: Number 23
    :return:
    """
    response = create_user('testuser3')
    username = response['User']['UserName']
    iam = boto3.client('iam')
    response = iam.create_access_key(UserName=username)
    return response


def update_access_key_of_user():
    """
    Section 2: Number 23
    :return:
    """
    iam = boto3.client('iam')
    username = 'testuser3'
    response = iam.list_access_keys(UserName=username)
    access_id = response['AccessKeyMetadata'][0]['AccessKeyId']
    response = iam.update_access_key(UserName=username, AccessKeyId=access_id, Status='Inactive')
    return response


def create_user_login_profile():
    """
    Section 2: Number 24
    :return:
    """
    username = 'testuser3'
    iam = boto3.client('iam')
    response = iam.create_login_profile(Password='MyPassworddd@1', PasswordResetRequired=False, UserName=username)
    return response
