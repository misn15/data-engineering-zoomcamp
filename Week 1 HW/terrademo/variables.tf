variable "project" {
  description = "Project Name"
  default     = "project-7d17f79e-abaf-4458-8e4"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "region" {
  description = "Project Region"
  default     = "us-east1"
}

variable "bq_dataset_name" {
  description = "my bigquery dataset name"
  default     = "demo_dataset"
}

variable "gcp_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "project-7d17f79e-abaf-4458-8e4-demo-bucket"
}

variable "gcp_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
