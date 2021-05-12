# k8s-artifacts
Simple-flask-Web-Application deploy using Kubernetes Artifacts

## Prerequisites
```
Docker
Minikube
Kubectl
```

## Installation

1. [Docker](https://www.docker.com/) &nbsp; &nbsp; : If you don't have docker install, please install it from [Here](https://docs.docker.com/engine/install/).
2. [Minikube]() : You can install Minikube on docker as well on virtual machine[Here](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/) is link to install Minikube using virtual machine.
3. [Kubectl]() &nbsp; &nbsp;: You can install Kubectl from [Here](https://kubernetes.io/docs/tasks/tools/).



## Getting Started

1. Clone the project.
2. Go to k8s-artifacts/ repository
3. build docker image by executing `docker build . -t test` command
4. Start the minikube by executing `minikube start` command
5. Execute `eval $(minikube docker-env)` command to configure environment to use minikube's docker daemon. 
6. Execute `kubectl apply -f .` 
7. Grab the IP address of the Minikube by executing `kubectl cluster-info` command.
8. Enter `kubectl get svc` command to get the port of the service.
9. Open browser and enter `http://minikube-ip:port/pucsd`, replace minikube-ip and port from the output of the 6th and 7th command respectively 
10. You can use postman also. just hit the url `http://minikube-ip:port/pucsd`, replace minikube-ip and port from the output of the 6th and 7th command respectively 

## Built With Stack

* [Docker](https://www.docker.com/) &nbsp;&nbsp;&nbsp;&nbsp;- &nbsp;Used to build the custom images
* [Minikube](https://v1-18.docs.kubernetes.io/docs/tasks/tools/install-minikube/) - &nbsp;Used start the cluster for kubernetes
* [Kubectl](https://kubernetes.io/docs/tasks/tools/) &nbsp;&nbsp;&nbsp;- &nbsp;Used to execute `.yaml` files
