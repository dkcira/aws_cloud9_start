{"filter":false,"title":"s3.py","tooltip":"/s3.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":51,"column":0},"action":"insert","lines":["import boto3","import sys","import botocore","","if len(sys.argv) < 3:","  print('Usage: python s3.py <the bucket name> <the AWS Region to use>\\n' +","    'Example: python s3.py my-test-bucket us-east-2')","  sys.exit()","","bucket_name = sys.argv[1]","region = sys.argv[2]","","s3 = boto3.client(","  's3',","  region_name = region",")","","# Lists all of your available buckets in this AWS Region.","def list_my_buckets(s3):","  resp = s3.list_buckets()","","  print('My buckets now are:\\n')","","  for bucket in resp['Buckets']:","    print(bucket['Name'])","","  return","","list_my_buckets(s3)","","# Create a new bucket.","try:","  print(\"\\nCreating a new bucket named '\" + bucket_name + \"'...\\n\")","  s3.create_bucket(Bucket = bucket_name,","    CreateBucketConfiguration = {","      'LocationConstraint': region","    }","  )","except botocore.exceptions.ClientError as e:","  if e.response['Error']['Code'] == 'BucketAlreadyExists':","    print(\"Cannot create the bucket. A bucket with the name '\" +","      bucket_name + \"' already exists. Exiting.\")","  sys.exit()","","list_my_buckets(s3)","","# Delete the bucket you just created.","print(\"\\nDeleting the bucket named '\" + bucket_name + \"'...\\n\")","s3.delete_bucket(Bucket = bucket_name)","","list_my_buckets(s3)",""],"id":1}]]},"ace":{"folds":[],"scrolltop":420,"scrollleft":0,"selection":{"start":{"row":2,"column":12},"end":{"row":2,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1555472992998,"hash":"6c0fbf6599fbaf2ee38456fab8f80fc9cc944c33"}