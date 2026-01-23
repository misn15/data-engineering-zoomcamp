terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  project     = "project-7d17f79e-abaf-4458-8e4"
  region      = "us-east1"
}

resource "google_storage_bucket" "demo-bucket" {
  name          = "project-7d17f79e-abaf-4458-8e4-demo-bucket" // has to be globally unique across GCP
  location      = "US"
  force_destroy = true
  uniform_bucket_level_access = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}