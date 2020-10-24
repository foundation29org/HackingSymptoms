## TA4Health_ClinPhen_AzureFunc.zip

Contains code used to deploy the Azure Function App (hpoannotator) in F29's Microsoft Azure Sponsorship subscription, in the ta4health resource group. 
This Azure Function App contains two functions, 

- 'TAforHealth_wrapper' which 
wraps the Text Analytics for Health endpoint, returning only the relevant HPO information, and 

- 'f29ClinPhen' which wraps the ClinPhen algorithm to return HPO information. 

Note that the Text Analytics for Health endpoint is configurable from the Azure portal as an environment variable. It is currently set to the endpoint for the ta4h-app-service 
in the ta4health resource group (which is no longer in operation). 

## TA4Health_AzureFunc.zip

Contains only the code required for the 'TAforHealth_wrapper' function.
