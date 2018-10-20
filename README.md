# Executing commands on EC2 using AWS Lambda

## About

Execute commands or scripts on Linux instances by using SSH and aws lambda when flie upload in s3 bucket.


### Create S3 Bucket

Open AWS Console and Select S3

![title](images/s31.png)

Click on Create Bucket

![title](images/s32.png)

Give it a name, select region then click next through each step

![title](images/s33.png)

![title](images/s34.png)

![title](images/s35.png)

![title](images/s36.png)

### Create Ubuntu 16.04 Instance


Open AWS Console and Select ec2

![title](images/s31.png)

Click on Launch Instance

![title](images/2.png)

Select Ubuntu Server 16.04 

![title](images/3.png)

Choose an Instance Type and click next throught each step

![title](images/4.png)

![title](images/5.png)

![title](images/6.png)

![title](images/7.png)

![title](images/8.png)

### Create User and Roles

Open AWS Console and Select IAM

![title](images/s31.png)

Click on users

![title](images/iam1.png)

Click on Add User

![title](images/iam2.png)

Add User name and check Programmatic access and click next and Click on create user

![title](images/iam3.png)

Reopen users and Click on Roles

![title](images/iam1.png)

Select Amazon services and lambda click next

![title](images/role1.png)

Search lambda and check AWSLambdaExecute

![title](images/role2.png)

Add Role Name and click create role

![title](images/role3.png)

Click on Add inline policy 

![title](images/role3.png)

Search DescribeInstances and  select DescribeInstances click on Review Policy

![title](images/role4.png)

Add Name and click on Create Policy

![title](images/role5.png)

![title](images/role6.png)


## Create Lambda Package

## Install python 3.6 in your machine or ec2 instance

Install virualenv

```
pip3 install virtualenv

```
Create Virtualenv

```
virtualenv demo

```

Active your virtual environment

```
source demo/bin/activate

```

## Install Required Packages

```
pip3 install boto3
pip3 install paramiko

```

## Go to demo/lib/python3.6/site-packages

## Create zip file

```
zip -r code_lambda.zip .

```
## Add your Code Files

```
zip -r code_lambda.zip code_lambda.py

```
### Create Lambda

Open AWS Console and Select lambda

![title](images/s31.png)


Click on Create Function

![title](images/lambda1.png)

Click on Blueprints and search python3 you will find Hello-World-python3 select that

![title](images/lambda2.png)

Add Name and Select Existing role which we create earlier and click on Create Function

![title](images/lambda3.png)

Click on S3 

![title](images/lambda4.png)

Select your Bucket

Add Prefix folder name where you storing your images in s3 bucket 

Add sufix like .jpg,.mp4 etc ..

Click on Create Function

![title](images/lambda5.png)

Select Upload .zip file and Select zip file which we created earlier and click on save button

![title](images/lambda6.png)

In Handle you need to add "your file name"."your function name"

![title](images/lambda7.png)

Set Timeout according your code execution

![title](images/lambda8.png)

Put your private/public Key inside "key" folder name on s3 bucket

Click on Test button

![title](images/lambda9.png)



