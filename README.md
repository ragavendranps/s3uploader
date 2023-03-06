# S3uploader

S3uploader is a python application to continuously monitor a file and uploads to S3 bucket when a new file is created or content of the existing file is changed.

## Installation

Application uses boto3 to access and upload the file to s3.

```bash
pip install boto3
```

## Usage

AWS secret key and access key are passed as stored under ./aws/credentials
```
ragav@RagavendransAir .aws % cat credentials 
[default]
aws_access_key_id = ################7HXK
aws_secret_access_key = ###################T3og
```

```python
python3 s3uploader.py  ido-ragavendran-ps20230302174514020500000001 ./myfile.txt

# if the file exists
File myfile.txt already exists

# when the content of myfile.txt is changed
myfile.txt is uploaded to s3://ido-ragavendran-ps20230302174514020500000001

# when the content of myfile.txt is not modified
myfile.txt is not uploaded
```
