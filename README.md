# robot-eight-app

I am using Microsoft Entra Workload ID instead of Microsoft Entra pod-managed identities. Pod-managed identity was deprecated in 2022.

See: https://learn.microsoft.com/en-us/azure/aks/workload-identity-overview

## Defender for Cloud recommendations

### Azure Kubernetes Service clusters should have Defender profile enabled

Just clicked on Fix button.

### Secure access to the API server using authorized IP address:

I setup my public IP address.

```az aks update --resource-group rg-robot-eight-sbx-euw-01 --name aks-robot-eight-sbx-euw-01 --api-server-authorized-ip-ranges xxx.xxx.xxx.236/32
```

### Azure Kubernetes Service clusters should have the Azure Policy add-on for Kubernetes installed

```az provider register --namespace Microsoft.PolicyInsights
```

### Key vaults should have purge protection enabled

Just change setting in Properties page.

### Container registries should not allow unrestricted network access

Cannot change, because I would need to update plan from Basic to Premium.


