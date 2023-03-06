import time
import boto3
import os
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]


# specify the path of the file to watch
def s3uploader(bucket_name, file_path):
    file_name = 'myfile.txt'
    s3 = boto3.client('s3')

    # Get the last modified time of the file
    last_modified_time = os.path.getmtime(file_path)
    last_contents = open(file_path, 'rb').read()
    result = False
    flag = False
    while not flag:
        # Check if the file exists
        check_file = s3.list_objects_v2(Bucket=bucket_name, Prefix=file_name)
        if not result:
            if check_file.get('Contents'):
                print(f'File {file_name} already exists')
                result =True
                continue
            else:
                with open(file_path, 'rb') as file:
                    s3.upload_file(file_path, bucket_name, file_name)
                    print(f'File {file_name} was missing in s3 bucket {bucket_name}, now uploaded')
                    continue
        else:  
            # Check if the file is modified
            if os.path.getmtime(file_path) > last_modified_time:
                # Get the current contents of the file
                current_contents = open(file_path, 'rb').read()
                # Check if the contents are the same
                if current_contents != last_contents:
                    # Upload the file to S3
                    s3.upload_file(file_path, bucket_name, file_name)
                    print(f'{file_name} is uploaded to s3://{bucket_name}')
                    # Update the last modified time and contents
                    last_modified_time = os.path.getmtime(file_path)
                    last_contents = current_contents
                else:
                    print(f'{file_name} is not uploaded')
            # Wait for some time before checking again
            time.sleep(5)


s3uploader(arg1, arg2)
