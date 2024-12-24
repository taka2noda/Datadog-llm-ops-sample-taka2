# application docker
Ref:
https://zenn.dev/schnell/articles/56a1f6bed65688

ssh -i "~/.ssh/taka2-demo-aws.cer" ec2-user@ec2-43-206-110-141.ap-northeast-1.compute.amazonaws.com

sudo yum update -y
sudo yum -y install docker

sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker ec2-user

docker info
*no need docker login

*Restart
newgrp docker

sudo systemctl start docker
docker info

docker build --tag dockerdemo ./
docker run -d --name dockerdemo -e name='schnell' -p 80:8080 dockerdemo

http://43.206.110.141/dockerdemo

# Datadog Agent install
docs:
https://docs.datadoghq.com/ja/containers/docker/?tab=amazonlinux&site=us

docker run -d --name dd-agent -v /var/run/docker.sock:/var/run/docker.sock:ro -v /proc/:/host/proc/:ro -v /cgroup/:/host/sys/fs/cgroup:ro -e DD_SITE=datadoghq.com -e DD_API_KEY=<API KEY> gcr.io/datadoghq/agent:7

→Able to see docker and host metrics on Datadog UI