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

We used a monitoring tool called stern to view which pods are being used when accessing the application. We noticed it was only one pod that was being used and after further investigation it was the same one that we did port forwarding to. In order to allow all pods to be used when accessing the application, we needed to set up a loadbalancer. 

<h3>Wednesday 29 November</h3>

After getting comfortable using kubernates locally to create a cluster, deploy our application and expose the application to view it in the browser, it was time to use terraform and github actions to create an EKS cluster on AWS and deploy an application. We worked as a group to understand the steps we need to take to achieve this week's task. The steps to set up terraform and github actions were the same as last week so this was a good referesher. We configured an AWS user to manage the creation of different services. We created an S3 bucket to hold our terraform state. We set up a simple GitHub action to test our application and another to deploy our application. 

<h3>Thursday 30th November</h3>

Today we continued with the project. We set up an EKS cluster using github actions. We had some trouble initially as we were getting different errors that the name of our application was wrong. After some research to understand the error message better and find a solution, we realised that the local resource was missing that specified the name. We connected to this cluster which allowed us to check everything is set up correctly. We did this using "aws eks --region <region name> update-kubeconfig --name <cluster name>". We also set up a dashboard to view our cluster. We did this using the "kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml" and enabled it using "kubectl proxy".

Finally, we deployed our application by creating a deployment yaml file which specified our container port and the docker image that is being used. Then we ran the "kubectl apply -f deployment.yaml" command to deploy. 

<h3>Friday 1st December</h3>

Today we exposed our app using ingress and set up a loadbalancer to manage traffic to the different pods. This did not work for us.
