# Python-RestAPI-AWS

To run one command to deploy our entire application giving us:

1. A Virtual Private Cloud with private and public subnets
2. Multiple running container instances
3. A load balancer distributing traffic between the containers
4. Route53 to route the requests to ALB.
5. Auto scaling of your resources
6. Health checks and logs

#######

Inside the root of the project add a terraform directory.
Terraform config files use the file extension .tf

To make the terraform code modular and easy to investigate as well as look neat.
We will make different .tf file for all resources and connect them together using variables.

###########

This can be done in different ways but here we’re telling Terraform.
Our provider is AWS and that it can find our credentials in $HOME/.aws/credentials which is the default location for AWS credentials on Mac and Linux.

#########

Terraform offers “outputs” which are great for getting data back after a deploy is successful. 

###########

Commands to run the infrastructure :: 

1. terraform init terraform
2. terraform plan terraform

## check the configuration after the plan step and make sure you want to proceed...

3. terraform apply terraform

You can check all resources up and running in AWS console.

################