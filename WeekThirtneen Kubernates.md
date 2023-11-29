<h1>Week13 Kubernates</h1>

<h2>Goals:</h2>

By the end of the week, the goal is to be able to answer "yes" to the week's primary questions:
- Can you explain what Container Orchestration is?
- Can you explain what problems Container Orchestration solves and what its main benefits are?
- Can you use Kubernetes to deploy and manage simple applications running on a cluster?
- Can you diagram the Kubernetes cluster architecture and the different pieces that take part in it?
- Can you use EKS to run a Kubernetes cluster on AWS?
- Can you describe the main differences between running your own K8s cluster as opposed to using a Cloud service like EKS?


<h3>Monday 27th November</h3>

Today we started a new module on Kubernates. I did a lot of research independently and in my project group to understand what Kubernates does. Kubernates is a container orchestration tool that manages the deployment, scaling and management of containerised applications. I set up a basic Kubernates cluster locally by downloading kubectl and k3d. Kubectl is used a management tool and k3d builds the necessary infrastructure. 

<h3>Tuesday 28th November</h3>

Today we further developed our understanding of how to set up kubernates locally. I created a cluster using "k3d cluster create <cluster name>" command. Then I created a worker node using "k3d node create <node name> -c <cluster name>". Then I created a deployment using a docker image "kubectl create deployment <name of deployment> --image <name of image>". Then I created a service using <kubectl create service loadbalancer <name of deployment> --tcp=8080:80>.

<h3>Wednesday 30th November</h3>
