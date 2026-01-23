# Question 1. Understanding Docker images
Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

What's the version of pip in the image?

``` 
docker run -it python:3.13 bash
pip -V 
```
# Questions 3-6

See `green taxi data.py`

# Question 7 Terraform

See `terrademo` for creating a GCP Bucket and Big Query Dataset

Which of the following sequences, respectively, describes the workflow for:

1. Downloading the provider plugins and setting up backend
2. Generating proposed changes and auto-executing the plan
3. Remove all resources managed by terraform

```
terraform init
terraform apply -auto-approve
terraform destroy 
```
