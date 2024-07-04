# Terraform Ubuntu Installation

## Update APT package index:

sudo apt-get update && sudo apt-get install -y gnupg software-properties-common

## Download HashiCorp GPG key:

wget -O- https://apt.releases.hashicorp.com/gpg | \
gpg --dearmor | \
sudo tee /usr/share/keyrings/hashicorp-archive-keyring.gpg > /dev/null

## Verify HashiCorp GPG key fingerprint:

gpg --no-default-keyring \
--keyring /usr/share/keyrings/hashicorp-archive-keyring.gpg \
--fingerprint

## Add HashiCorp APT repository:

echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] \
https://apt.releases.hashicorp.com $(lsb_release -cs) main" | \
sudo tee /etc/apt/sources.list.d/hashicorp.list

## Update APT package index:

sudo apt update

## Install Terraform:

sudo apt-get install terraform

## Verify installation:

terraform --version
