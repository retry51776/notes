# AWS
docs.aws.amazon.com

AWS support prefer screen share

Edit premission will allow ticket creation

CloudWatch + CloudTrail = stackdriver

### Apps
- S3 `Disk Storage`
- Cloudfront `CDN`
- Route 53 `DNS`
- API Gateway `10,000 RPS (requests per second)` + Lambda `cloud function`
- App Load Balancer + EC2 `old VM`
- App Load Balancer `+100,000 RPS, since 16` + ECS `container`
- EKS `K8`
- Elastic Load Balancer (ELD) `since 09, container-based`

### Lambda
> job less than 15 mins
```
def xxx_handler(event, context):
    id = event['queryStringParameters']['id']
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'json'
        },
        'body': json.dumps({})

    }
```
### Elastic Container Service (ECS)

### Elastic Kubenete Service (EKS)

### DBs
https://aws.amazon.com/products/databases/

- RDS `amazon version mysql`
- Aurora

### Orchestration
Step Functions
SNS - `similar rabbitmq`
SQS - `simple message & consum` 
Cloud Formation

## AWS Enterprise Support
> Always keep ticket #

> always attch resource_id

> Cross Account needs open tickets in both accounts

Response Time
bussiness critical 15min
Production System Down 1h
Production Impaired 4h
System Impaired 12h
Guidance 24h

Enterprise Discount Program (EDP)

### Pricing Models
- On Demand
- Saving Plans
- Reserved Instances
- Spot Instances
- Delicated Host


```
~/.aws/credentials
[default]
aws_access_key_id=xxx
aws_secret_access_key=yyy

kubeconfig default /Users/xxx/.kube/config

//brew tap weaveworks/tap
apt-get install eksctl
```

# Aws Course
- AWS Cloud Practitioner Essentials


# GCP
GKE

Google Cloud’s containers as a service (CaaS)

StackDriver

Cloud Storage

Cloud Functions
