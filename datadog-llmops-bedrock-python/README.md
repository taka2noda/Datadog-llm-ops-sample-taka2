## Procedure

Reference Guide: https://docs.datadoghq.com/llm_observability/setup/sdk/


### Env
On AWS Cloud9 or Cloud Shell

### Prerequisites

The latest `ddtrace` package must be installed:

```
pip install ddtrace
```

LLM Observability requires a Datadog API key

anthropic.claude-3-haiku is enabled on AWS Bedrock

### Command-line setup

Enable LLM Observability by running your application using the `ddtrace-run` command and specifying the required environment variables.

Command Template
```
DD_SITE=<YOUR_DATADOG_SITE> DD_API_KEY=<YOUR_API_KEY> DD_LLMOBS_ENABLED=1 DD_LLMOBS_AGENTLESS_ENABLED=1 \
DD_LLMOBS_ML_APP=<YOUR_ML_APP_NAME> ddtrace-run <YOUR_APP_STARTUP_COMMAND>
```

Command Sample
```
DD_LLMOBS_ENABLED=1 DD_LLMOBS_ML_APP=br-chat \
DD_API_KEY="自分のAPI Key" DD_SITE="datadoghq.com" DD_LLMOBS_AGENTLESS_ENABLED=1 \
ddtrace-run python br-chat.py
```

### Datadog Setting

Once LLM Trace is sent to Datadog, you need to enable "Evaluations" at "Configuration" tab

### Command history
```
[cloudshell-user@ip-10- ~]$ ls
work-bedrock
[cloudshell-user@ip-10- ~]$ cd work-bedrock/
[cloudshell-user@ip-10- work-bedrock]$ ls
br-chat.py
[cloudshell-user@ip-10- work-bedrock]$ DD_LLMOBS_ENABLED=1 DD_LLMOBS_ML_APP=br-chat1 DD_API_KEY="" DD_SITE="datadoghq.com" DD_LLMOBS_AGENTLESS_ENABLED=1 
ddtrace-run python br-chat.py