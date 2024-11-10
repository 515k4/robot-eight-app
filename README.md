# robot-eight-app

I am using Microsoft Entra Workload ID instead of Microsoft Entra pod-managed identities. Pod-managed identity was deprecated in 2022.

See:
- https://learn.microsoft.com/en-us/azure/aks/use-azure-ad-pod-identity
- https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview

I've created AKS with Authentication and Authorization: Microsoft Entra ID Authentication with Kubernetes RBAC. Cluster Admin is set to group AKSAdmin.

*AKS RBAC:* myself as Azure Kubernetes Service Contributor Role

*ACR RBAC:* AcrPull for AKS user-assigned Managed Identity, myself as Container Registry Repository Contributor

*Vault RBAC:* Key Vault Secrets User for user-assigned Managed Identity, myself as Key Vault Administrator

*Note:* Defender automatically sets lots of RBAC for all resources.

*AKS Networking:* Public access to API enabled, but authorized IP is set to my home public IP.

*ACR Networking:* Basic SKU does not allows disabling public access.

*Vault Networking:* Allow public access from specific virtual networks and IP addresses, Private endpoint

## Defender for Cloud recommendations

I did setup myself as Security Admin in Management Group.

### Azure Kubernetes Service clusters should have Defender profile enabled

Just clicked on Fix button.

### Secure access to the API server using authorized IP address:

I setup my public IP address.

```
az aks update --resource-group rg-robot-eight-sbx-euw-01 --name aks-robot-eight-sbx-euw-01 --api-server-authorized-ip-ranges xxx.xxx.xxx.236/32
```

### Azure Kubernetes Service clusters should have the Azure Policy add-on for Kubernetes installed

```
az provider register --namespace Microsoft.PolicyInsights
```

### Key vaults should have purge protection enabled

Just change setting in Properties page.

### Container registries should not allow unrestricted network access

Cannot change, because I would need to update plan from Basic to Premium.

### Running containers as root user should be avoided

Edited Dockerfile with user appuser, addded Security context to AKS deployment yaml.
