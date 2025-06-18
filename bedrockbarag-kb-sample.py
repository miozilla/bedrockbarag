import boto3

bedrock = boto3.client('bedrock-agent')

response = bedrock.create_knowledge_base(
    name='EnterpriseKB',
    description='Knowledge base for enterprise assistant',
    roleArn='arn:aws:iam::123456789012:role/BedrockAccessRole',
    vectorStoreConfiguration={
        'type': 'OPENSEARCH_SERVERLESS',
        'indexName': 'enterprise-index'
    },
    embeddingModelArn='arn:aws:bedrock:us-east-1::foundation-model/amazon.titan-embed-text-v1'
)