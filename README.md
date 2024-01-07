# python-helloworld
a hello world python code with flask

# Clone this repository

`$git clone git@github.com:addhe/python-helloworld.git`

`$pushd python-helloworld`

# Login to docker

`$docker login --username {{username}}`
e.g.

`$docker login --username awan`

# Build and Push the apps

## How to Build the Apps Image
`$docker build -t docker.io/{{username}}/flask-app:0.1.2 -f docker/Dockerfile .`

e.g.

`docker build -t docker.io/awan/flask-app:0.1.2 -f docker/Dockerfile .`

## Push the apps to docker registry

`$docker push {{username}}/flask-app:0.1.2`

e.g.

`$docker push awan/flask-app:0.1.2`

# Install k3d on Workstation ( this is for Mac / Linux )

`$brew install k3d`

# Create Cluster with k3d

`$k3d cluster create mycluster`

# Adding more nodes to cluster if you need more

`$k3d node create mynode --cluster mycluster --role agent --replicas 2`

# Deploy flask app hello world into k8s

`$pushd k8s`

`$kubectl apply -f deployment.yaml`

`$kubectl apply -f service.yaml`

`$kubectl apply -f ingress-hosts.yaml`

`$kubectl apply -f hpa.yaml`

# Testing with curl and kubectl ports forwarding

`$kubectl port-forward -n kube-system service/traefik 8080:80`

`$curl http://127.0.0.1:8080 --header 'Host: hello-world.oppna.local'`

# Get the cluster IP service of flask hello world app

`$kubectl get services`

# Testing from same network in k8s cluster

## create a temporary locust-ubuntu container and wait until it is created

`$kubectl run locust-ubuntu --image=ubuntu --restart=Never --command -- sleep 4200`

## login into locust-ubuntu container with kubectl executable once it is created

`$kubectl exec -it locust-ubuntu -- /bin/bash`

## Install curl, vim, netcat, python3, python3-pip once we inside the locust-ubuntu

`$apt update && apt install -y curl vim netcat python3 python3-pip`

## Testing with curl and pointing to cluster IP service of flask hello world app

`$curl http://{{ Change_me_to_cluster_ip_service }}:{{ Change_me_to_cluster_port_service }} --header 'Host: hello-world.oppna.local'`

e.g.

`$curl http://10.43.234.222:8080 --header 'Host: hello-world.oppna.local'`

## Output should look like:

`root@locust-ubuntu:/# curl http://10.43.234.222:8080 --header 'Host: hello-world.oppna.local'`

Hi, Hello world Writen With Python Using Flask and Waitress - version 0.1.2

# ------------------------------------------------

# Notes for testing k8s ( optional )

`$pushd k8s`

# Testing deploy and destroy pod on k8s cluster

## Deploy pod

`$kubectl apply -f pod.yaml`

## Get the IP of Pods

`$kubectl get pod/flask-app --output go-template="{{.metadata.name}} {{ .status.podIP }}" ; echo;`

## Destroy pod

`$kubectl delete -f pod.yaml`

# Testing deploy services on k8s cluster

## Deploy Pod and Service
`$kubectl apply -f pod.yaml`
`$kubectl apply -f service.yaml`

## Kubectl port forward service flask-svc
`$kubectl port-forward service/flask-svc 8080:8080`

## Testing with curl
`$curl http://127.0.0.1:8080 ;echo`

## Clean up pod and service
`$kubectl delete -f pod.yaml pod-b.yaml`

# Testing deployment service on k8s
`$kubectl apply -f deployment.yaml`

## testing port forward
`$kubectl port-forward service/flask-svc 8080:8080`

## testing with curl
`curl http://127.0.0.1:8080 ;echo`
Hi hi, Hello world Writen with Python using Flask and Waitress - version 0.1.0`

# testing deploy ingress as loadbalancer

## Apply ingress
`$kubectl apply -f ingress.yaml`

## Testing kubectl port forward to services
`$kubectl port-forward -n kube-system service/traefik 8080:80`

## Testing curl 10 times, now we will see the traffic distributed to all replicas

`for i in {1..10}; do curl http://127.0.0.1:8080; done`

## Check logs pods and the traffic distributed to all replicas

`$kubectl get pods`                                           

|NAME                        |READY   |STATUS      |RESTARTS   |AGE|
|----------------------------|--------|------------|-----------|---|
|flask-app-557594444-thw4c   |1/1     |Running     |0          |17m|
|flask-app-557594444-99rvg   |1/1     |Running     |0          |17m|
|flask-app-557594444-xv4lc   |1/1     |Running     |0          |17m|

`$kubectl logs pod/flask-app-557594444-thw4c`

`$kubectl logs pod/flask-app-557594444-99rvg`

`$kubectl logs pod/flask-app-557594444-xv4lc`

or from all app

`$kubectl logs -l app=flask-app --all-containers=true -f`

# Testing using ingress hostname and access it

## Deploy ingress host
`$kubectl apply -f ingress.yaml`

`$kubectl port-forward -n kube-system service/traefik 8080:80`

`$kubectl apply -f ingress-host.yaml`

## Check ingress hosts
`$kubectl get ingress`

## Testing curl with hostname
`$curl http://127.0.0.1:8080 --header "Host: hello-world.oppna.local"`

# Deploy hpa ( kindly adjust the file hpa.yaml cpu utilization )
`$kubectl apply -f hpa.yaml`
