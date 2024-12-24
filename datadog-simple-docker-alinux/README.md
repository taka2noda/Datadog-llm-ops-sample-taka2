# Step1. Build Docker Application
Ref:
https://zenn.dev/schnell/articles/56a1f6bed65688

Login to EC2 instance
```
ssh -i "~/.ssh/taka2-demo-aws.cer" ec2-user@ec2-43-206-110-141.ap-northeast-1.compute.amazonaws.com
```

update yum and install docker
```
sudo yum update -y
sudo yum -y install docker
```

start docker
```
sudo systemctl start docker
```

enable auto start
```
sudo systemctl enable docker
```

Add privilege
```
sudo usermod -aG docker ec2-user
```

Check info *no need docker login
```
docker info
```

Restart to apply the change
```
newgrp docker
```

Start docker and check info
```
sudo systemctl start docker
docker info
```

build and run docker container
```
docker build --tag dockerdemo ./
docker run -d --name dockerdemo -e name='schnell' -p 80:8080 dockerdemo
```

Access application
http://<Public IP>:80/dockerdemo

![image](https://github.com/user-attachments/assets/17bb64ba-a305-4d2c-9fd7-fbf1189487a3)


# Step2. Insltall Datadog Docker Agent
docs:
https://docs.datadoghq.com/ja/containers/docker/?tab=amazonlinux&site=us

Install docker Datadog Agent
```
docker run -d --name dd-agent -v /var/run/docker.sock:/var/run/docker.sock:ro -v /proc/:/host/proc/:ro -v /cgroup/:/host/sys/fs/cgroup:ro -e DD_SITE=datadoghq.com -e DD_API_KEY=<API KEY> gcr.io/datadoghq/agent:7
```
→Able to see docker and host metrics on Datadog UI
![image](https://github.com/user-attachments/assets/f31b2be1-a061-4aaf-a094-a1a4b83793c2)
