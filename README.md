# Appsec Family sample container image

## Purpose

This repository is a hands-on educational resource for learning about application security (AppSec) and software supply chain security. It walks through building a Python-based container image, generating a Software Bill of Materials (SBOM), scanning for vulnerabilities, and signing the image with Sigstore Cosign to ensure authenticity and integrity.

### Key Aspects

- Automated CI/CD pipeline using GitHub Actions.
- SBOM generation with Syft.
- Vulnerability scanning with Trivy.
- Image signing with Cosign (private/public key & OIDC keyless signing).
- Signature storage in the container registry.
- Verification commands to confirm authenticity.

## CI Workflow Overview

The ci.yml file automates:

- Build & Push — Create the image and push to Docker Hub.
- Generate SBOM — List all dependencies and metadata for security review.
- Scan for Vulnerabilities — Identify CVEs in the image.
- Sign the Image — Sign using both a private key and GitHub OIDC keyless signing.
- Publish Results — Output SBOM and scan summary to GitHub Actions summary.


## SBOM

Software supply chain attacks are increasing, targeting build pipelines and dependencies. By integrating SBOM generation, vulnerability scanning, and image signing into CI/CD pipelines, we:

- Ensure visibility into dependencies.
- Detect known vulnerabilities early.
- Guarantee image provenance via cryptographic signatures.
- Protect against tampered images being deployed.

## Cosign Key Concepts
- Private Key — Kept secret, used to generate signatures (stored in GitHub Secrets as COSIGN_PRIVATE_KEY).
- Public Key — Shared openly to allow verification (cosign.pub).
- OIDC Keyless — Optional, uses GitHub’s identity to sign without manually managing keys.


### Verifying a Signed Image Locally

1. Install Cosign (Windows PowerShell)

`curl -LO https://github.com/sigstore/cosign/releases/latest/download/cosign-windows-amd64.exe`

`mv cosign-windows-amd64.exe cosign.exe`

#### Verify Using Public Key
.\cosign.exe verify docker.io/tiagome/appsec-family-cosign:d59d07e7763eaf1fc331ef394acf1936fe2cf3bf --key .\cosign.pub


If verification succeeds, Cosign confirms:

- Signature matches the public key.
- Image digest matches.
- Signature exists in the transparency log.


## Recommended Supply Chain Security Practices

- Always generate SBOMs for transparency.
- Integrate vulnerability scanning in CI.
- Sign all container images before deployment.
- Use keyless signing where possible to reduce key management risk.
- Store public keys in a trusted location.
- Verify signatures in production before running images.
