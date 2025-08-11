
# AWS
docs.aws.amazon.com

AWS support prefers screen sharing.

Edit permissions will allow ticket creation.

CloudWatch + CloudTrail = Stackdriver equivalent.

### Apps
- **S3** – object storage  
- **CloudFront** – CDN  
- **Route 53** – DNS  
- **API Gateway** – 10,000 RPS (requests per second) + Lambda (serverless functions)  
- **Application Load Balancer** + EC2 – classic VMs  
- **Application Load Balancer** – > 100 000 RPS (since 16) + ECS (containers)  
- **EKS** – Kubernetes  
- **Elastic Load Balancer (ELB)** – container‑based (available since 09)

### Lambda
> Test with Serverless Framework or SAM.

> Max execution time: 15 minutes.  

> Not ideal for application‑level caching (AWS keeps a function warm for only 30–45 min).  

> Cold starts are slower when the function runs in a VPC.  

> You can keep functions warm manually, but AWS does not provide a built‑in option.

```python
def xxx_handler(event, context):
    id = event['queryStringParameters']['id']
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({})
    }
```

```bash
sam local invoke -e ./xx.json XXX_Function
sam local start-api
```

```yaml
AWSTemplateFormatVersion: '2010-01-01'
Transform: AWS::Serverless-2010-01-01
Description: >
  xxx

Resources:
  LambdaDemoFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: lambda/
      Handler: lambda.xxx_handler
      Runtime: python3.10
```

## Step Functions
> Server‑side business logic state machine.

```json
{
  "StartAt": "x_step",
  "States": {
    "x_step": {
      "Type": "Choice",
      "Choices": [
        {
          "Variable": "$.choice",
          "StringEquals": "Confirmed",
          "Next": "confirmed"
        }
      ]
    },
    "confirmed": {
      "Type": "Task",
      "Resource": "confirm_lambda_function",
      "End": true
    }
  }
}
```

### Elastic Container Service (ECS)

### Elastic Kubernetes Service (EKS)

## DBs
https://aws.amazon.com/products/databases/

- **RDS** – Amazon‑managed MySQL, PostgreSQL, etc.  
- **Aurora**  

## Orchestration
- Step Functions  
- SNS – similar to RabbitMQ  
- SQS – simple queue service  
- CloudFormation  

## AWS Enterprise Support
> Always keep the ticket number.  
> Always attach the resource ID.  
> Cross‑account issues require tickets in both accounts.

**Response Times**
- Business‑critical: 15 min  
- Production system down: 1 h  
- Production impaired: 4 h  
- System impaired: 12 h  
- Guidance: 24 h  

Enterprise Discount Program (EDP)

### Pricing Models
- On‑Demand  
- Savings Plans  
- Reserved Instances  
- Spot Instances  
- Dedicated Host  

```
~/.aws/credentials
[default]
aws_access_key_id=xxx
aws_secret_access_key=yyy
```

```bash
kubeconfig default /Users/xxx/.kube/config

# brew tap weaveworks/tap
apt-get install eksctl
```

# AWS Course
- AWS Cloud Practitioner Essentials

#### AWS CLI
```bash
aws ec2 run-instances
```

### Direct Connect
> Private connection between a data centre and AWS.

### Amazon Elastic Block Store (EBS)
Database storage.

## Simple Storage Classes (S3)

### S3 Standard
(11 9s) of data durability.

S3 lifecycle management – automatically moves data between tiers.

## AWS Lake Formation
- Athena – interactive query service  
- Glue – data catalog and ETL  
  - Data Catalog databases – storage for crawlers  
  - Crawler – detects S3 folder changes & creates tables  
  - Kinesis Firehose  
  - Job – creates ETL pipelines (Spark, streaming, Python shell)

## AWS IAM
- Groups → users  
- Role – temporary access  
- Policy  
  - Effect: Allow or Deny  
  - Action: `xxx_api`  
  - Resource: `xxx_resource`  

### Key Management Service (KMS)

### Inspector

## CloudWatch
- Dashboard  
- Alarm
