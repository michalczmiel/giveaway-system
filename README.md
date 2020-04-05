# giveaway-service

## Architecture

The app consists of two parts: client and api.
Client is a React.js app, hosted on S3 which interacts with serverless API. 

Serverless architecture was chosen because:

- it offers almost unlimited scalability without the need to change the code or the infrastructure
- it offers flexible pricing because client is charged only when the resources are used

AWS Lambda was chosen as a deployment technology.
In order to ease the process of development and deployment, Serverless framework was used.

## Requirements

- Node.js
- Yarn
- Docker
