# Datadog-llm-ops-sample-taka2

Datadog LLM Observability Sample Applications.

## ディレクトリ構成

サンプルアプリは技術要素ごとに以下のディレクトリに分類されています。

```
.
├── docker/       # Dockerコンテナとして直接実行するサンプル
├── ecs/          # AWS ECSでオーケストレーションするサンプル
├── ec2/          # EC2インスタンス上で直接実行するサンプル
└── llmops/       # LLM Observability / Agentlessモードのサンプル
```

---

## docker/

### [datadog-flask-docker-apm](./docker/datadog-flask-docker-apm/)
- **言語/FW:** Python / Flask
- **概要:** FlaskアプリをDockerコンテナで動かし、ddtraceでAPMトレースを収集する基本デモ
- **Datadog機能:** APM (ddtrace)

### [datadog-simple-docker-alinux](./docker/datadog-simple-docker-alinux/)
- **言語/FW:** Python / Flask
- **概要:** Amazon Linux EC2上でDockerコンテナを起動し、Datadog AgentもDockerで動かすデモ
- **Datadog機能:** APM, Infrastructure Metrics

---

## ecs/

### [Datadog-aws-ecs-ec2](./ecs/Datadog-aws-ecs-ec2/)
- **言語/FW:** Python / Flask
- **概要:** ECS on EC2構成でFlaskアプリとDatadog Agentをサイドカーとしてデプロイするデモ。ECSタスク定義JSON付き
- **Datadog機能:** APM (ddtrace), CloudWatch Logs

### [datadog-aws-ecs-handson-rubyrails](./ecs/datadog-aws-ecs-handson-rubyrails/)
- **言語/FW:** Ruby / Ruby on Rails 7
- **概要:** ECS上でRailsアプリを動かし、FirelensでログをDatadogに転送するハンズオン。ECSタスク定義JSON付き
- **Datadog機能:** APM (datadog gem), Logs (Firelens / Fluent Bit)

---

## ec2/

### [datadog-integration-openai-python](./ec2/datadog-integration-openai-python/)
- **言語/FW:** Python
- **概要:** EC2上でDatadog AgentとOpenAI Python SDKを組み合わせ、LLMのPrompt/Completionをトレースするデモ。DALL-E-3画像生成やエラーケースのサンプルも含む
- **Datadog機能:** APM (ddtrace), OpenAI Integration, LLM Observability

---

## llmops/

### [datadog-llmops-bedrock-python](./llmops/datadog-llmops-bedrock-python/)
- **言語/FW:** Python
- **概要:** AWS Bedrock (Claude 3 Haiku) をddtraceのAgentlessモードでモニタリングするデモ。Datadog Agentのインストール不要
- **Datadog機能:** LLM Observability (Agentless), LLM Evaluations
