import boto3
import paramiko
def code_lambda(event, context):
	host = 0
	s3_client = boto3.client('s3')
	ec2 = boto3.resource('ec2')
	running_instances = ec2.instances.filter(Filters=[{'Name': 'instance-id','Values': ['Add your instance id']}])
	for instance in running_instances:
	    host = instance.public_ip_address
	        
	s3_client.download_file('Add your bucket name','key/Add your key name.pem', '/tmp/Add your key name.pem')

	k = paramiko.RSAKey.from_private_key_file("/tmp/Add your key name.pem")
	c = paramiko.SSHClient()
	c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	print("Connecting to " + host)
	c.connect( hostname = host, username = "ubuntu", pkey = k )
	print("Connected to " + host)
	commands = ["/home/ubuntu/demo.sh"]
	for command in commands:
		print("Executing {}".format(command))
		stdin , stdout, stderr = c.exec_command(command)
		print(stdout.read())
		print(stderr.read())
	return
	{
	    'message' : "Done"
    }

