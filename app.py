import os

from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from fastapi import FastAPI

app = FastAPI()

# Replace with your Azure Key Vault URL
KEY_VAULT_URL = os.getenv("KEY_VAULT_URL") or "https://keyroboteight.vault.azure.net/"

# Secret name in Azure Key Vault
SECRET_NAME = os.getenv("SECRET_NAME") or "my-secret-name"


# Function to get the secret from Azure Key Vault
def get_secret_from_key_vault(secret_name: str):
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=KEY_VAULT_URL, credential=credential)
    secret = client.get_secret(secret_name)
    return secret.value


@app.get("/")
async def read_secret():
    try:
        # Get the secret from Azure Key Vault
        secret_value = get_secret_from_key_vault(SECRET_NAME)
        # Display the secret on the web page
        return {"message": f"The secret value is: {secret_value}"}
    except Exception as e:
        return {"error": str(e)}
