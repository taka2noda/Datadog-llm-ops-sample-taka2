#AWS Python SDK(boto3) ライブラリの読み込み
import boto3

# Amazon Bedrock Runtime クライアントを作成
brt = boto3.client('bedrock-runtime')

# JSON ライブラリの読み込み
import json

body=json.dumps({
        'anthropic_version': 'bedrock-2023-05-31',
            'max_tokens': 4096,
                'system': '以下はユーザーと優秀なAIアシスタントのやりとりです',
                    'messages': [{'role': 'user', 'content': 'ここをプロンプトのInputに変える'}],
                    })
response = brt.invoke_model(body=body, modelId='anthropic.claude-3-haiku-20240307-v1:0')
output = json.loads(response['body'].read())['content'][0]['text']
print(output)
