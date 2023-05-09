# lambda-r-demo 

This repository contains source code and supporting files demonstrating how to run R on AWS Lambda functions using two approaches: 

1. Using the [rpy2](https://rpy2.github.io/) Python package. 
2. Using the [lambdr](https://lambdr.mdneuzerling.com/) R package. 

## Directory structure 
This repository uses the [Serverless Application Model (SAM)](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide) to define the necessary infrastructure. It includes the following files and folders:
- `lambdr/`: Code for the `lambdr` implementation. 
- `rpy2/`: Code for the `rpy2` implementation. 
- `template.yaml`: A template that defines the application's AWS resources. 

```
├── lambdr
│   ├── Dockerfile
│   ├── app.R
│   └── requirements.txt
├── rpy2
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── utils.R
└── template.yaml
```

## Deploy the application

To build and deploy this application, you will need to install [the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html) and [Docker](https://hub.docker.com/search/?type=edition&offering=community). 

To deploy this application for the first time, run the following:

```bash
sam build
sam deploy --guided
```

The first command will build a Docker image from a Dockerfile and then copy the source of the application inside the Docker image. The second command will package and deploy the application to AWS, with a series of prompts. 

See the [AWS SAM developer guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html) for an introduction to SAM specification, the SAM CLI, and serverless application concepts.

## Invoke the functions 

To invoke the functions, run the following: 

```bash
aws lambda invoke \
    --function-name r-lambda-demo-rpy2 \
    --cli-binary-format raw-in-base64-out \
    --payload '{"number": "24"}' \
    response.json
```

```bash
aws lambda invoke \
    --function-name r-lambda-demo-lambdr \
    --cli-binary-format raw-in-base64-out \
    --payload '{"number":  "24"}' \
    response.json
```