import boto3

def get_all_snapshots():
    # Prompt for AWS credentials
    access_key_id = input("*")
    secret_access_key = input("*")

    # Create a Boto3 session with provided credentials
    session = boto3.Session(
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )

    # Create an EC2 client using the session
    ec2_client = session.client('ec2')

    # Retrieve all snapshots
    response = ec2_client.describe_snapshots()

    # Extract the snapshot information from the response
    snapshots = response['Snapshots']

    # Print the details of each snapshot
    for snapshot in snapshots:
        snapshot_id = snapshot['SnapshotId']
        volume_id = snapshot['VolumeId']
        start_time = snapshot['StartTime']
        description = snapshot['Description']
        status = snapshot['State']
        encrypted = snapshot['Encrypted']

        print(f"Snapshot ID: {snapshot_id}")
        print(f"Volume ID: {volume_id}")
        print(f"Start Time: {start_time}")
        print(f"Description: {description}")
        print(f"Status: {status}")
        print(f"Encrypted: {encrypted}")
        print("")

# Call the function to retrieve all snapshots
get_all_snapshots()
