# python-helloworld
a hello world python code with flask

## install required packages
`$pip install -r requirements.txt`

# Login to docker

`$docker login --username {{username}}`
e.g.

`$docker login --username awan`

# Build and Push the apps

## Build
`$docker build -t docker.io/{{username}}/flask-app:0.1.1 .`
e.g.

`$docker build -t docker.io/awan/flask-app:0.1.1 .`

## Push

`$docker push {{username}}/flask-app:0.1.1`

e.g.

`$docker push awan/flask-app:0.1.1`

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
NAME                        READY   STATUS      RESTARTS   AGE
flask-app-557594444-thw4c   1/1     Running     0          17m
flask-app-557594444-99rvg   1/1     Running     0          17m
flask-app-557594444-xv4lc   1/1     Running     0          17m

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