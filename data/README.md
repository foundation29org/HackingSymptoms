# Source Code

To generate artificial medical records using OpenAI GPT-3 API, execute the following from the root directory of the repository:

```bash
python code/generate_medical_records_from_openaigpt3.py
```

### Azure Functions
Code stored in code/AzureFunctions contains the code used to deploy the Azure Text Analytics for Health and ClinPhen function wrappers.

### extract_GSC_HPO_data.ipynb
This code can be used to create the Gold Standard Corpus + (GSC+) csv file used in analyses. Source data from https://github.com/lasigeBioTM/IHP.

### parseTAResult.py
This code was used to parse pickled output from Text Analytics for Health called on the GSC+ dataset to retreieve only the HPO information. The Text Analytics for Health Azure Function wrapper was based on this code.
