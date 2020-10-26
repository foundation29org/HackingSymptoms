# Hacking Symptoms
Resources, docs and code repository for Microsoft 2020 Hackathon: Diagnosing rare diseases with AI - Hacking symptoms.

## Background information
Rare diseases are more common than what one could initially estimate. They are reported (sorry that I am no including references in this document) to affect ~6-8 % of the global population, although each one of them has a much smaller prevalence. Many patients take a very long time to be diagnosed, a time that can be greatly reduced by new technological developments on precision medicine. One technology that can greatly impact the diagnostic odyssey is the utilization of NLP to analyze patient medical records and identify the symptoms a patient presents. These symptoms can then be fed to a prediction algorithms of simply shown to a clinician for interpretation with or without genetic information.
 
Therefore, providing the patient symptoms stands as the entry point to leveraging the power of accurate disease clinical descriptions and, if available, the information contained in the patient genetic information. The symptoms are represented by Human Phenotype Ontology (HPO) terms, you have a short introduction at the HPO section.

## Objectives
The goal of this team is to:
1. Develop a framework (MVP-like) in which NLP algorithms capable of recognising medical concepts (HPO terms) can be compared.
2. Perform a comparison between such algorithms and establish a performance baseline.
3. If possible, further develop or improve the models.

## Algorithms to compare
We will focus the comparison on the following algorithms:
1. Neural Concept Recognizer (NCR).
2. Microsoft's Text Analytics.

However, if time permits, I'd like to include others:
1. Biolink NLP Annotator.
2. IHP
3. ClinPhen

### Neural Concept Recogniser (NCR)
This algorithm, by Arbabi et al [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6533869/], is deployed in Foundation 29's Azure subscription. An API will be provided. It was trained in the 228 pubmed abstracts here used, which implies that it's performance will be overestimated. Clearly suboptimal.
 
### Microsoft Text Analytics
You deployed this, so you are well aware about how to use it. I simply want to raise the case that probably it has already seen the data used in this project. I don't know how it was developed.

### Add-ons if you are interested and there is time:
1. Biolink NLP annotator: A rule-based annotation engine deployed at the biolink API (https://api.monarchinitiative.org/api/nlp/annotate).
2. IHP: Developed by Lobo et al (https://doi.org/10.1155/2017/8565739) and, again, trained on the GSC data. Downloadable from: https://github.com/lasigeBioTM/IHP.
3. ClinPhen: Developed by Deisseroth et al. (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6551315/), it can be obtained here: https://bitbucket.org/bejerano/clinphen/src/master/. Hopefully the PIP package is still valid. If not, give it a try to this one: https://github.com/kingmanzhang/clinphen.
4. Want a real challenge? It would be interesting to develop a matching strategy between HPO terms and the concepts trained on clinicalBERT (https://github.com/EmilyAlsentzer/clinicalBERT) so that they can be used directly for HPO term recognition.

## Data availability
Public data is very scarce in this context with limited available resources. The datasets required would be medical text labelled with HPO terms (see HPO section for details on what HPO is). In principle, there are two datasets that we could use: the Gold Standard Corpora and OMIM.
 
### Gold Standard Corpora
In order to test (or train) the algorithms we will use the dataset known as Gold Standard Corpora (GSC). The data consists of 228 annotated abstracts cited by OMIM (http://www.omim.org). The data can be found here: https://github.com/lasigeBioTM/IHP.
 
There is an improved version of the corpora fixing some issues as identified by Lobo et al. (https://doi.org/10.1155/2017/8565739).
 
We are requesting access to the OMIM API in order to be able to download clinical synopsis along with HPO annotations. This could bring the whole dataset to the order of 5000 annotated documents. But it is uncertain if they will be available for the Hackathon.
 
It is worth noting that the GSC is the same dataset that has been used by IHP and NCR for training, therefore there is a clear bias in the results that is difficult to solve. Ideas are welcomed.
 
### PubMed Phrases
NCBI has collected a large list of phrases and their related pulications (PMID). The data is freely accesible here (
PubMed Phrases): https://www.ncbi.nlm.nih.gov/research/bionlp/Data/. An interesting task would be to:
1. Find phrases that represent HPO symptoms and build a "hpo-subset".
2. Gather all documents that are related to the hpo-subset.
3. Invert the index and establish all the hpo terms related to each document. This could serve as an automatic annotation.
4. Get the documents and store the text annotating it with the HPO terms.
5. Evaluate the algorithms above on this dataset.

So the steps above look fairly simple... but they might not be. There are big uncertainties in each of them:
1. There is no guarantee that all relevant phrases will be found. Is this a huge problem? Possibly not. This will mean that the hpo-subset will be incomplete. Another issue would be if we find a lot of false positives. Again, is this an issue? 2. Probably not. It would mean a loss of computing power.
2. No uncertainty here.
3. Again, no uncertainty aside from the one carried from the step 1.
4. How can the documents be retrieved programmatically? I think PubMed has an API or there are bulk downloads available.
5. The evaluation in itself is fine... the analysis of the results is a different issue. This will be reviewed in the Bronze caliber dataset evaluation section (if this section has not been written, ping Pablo Botas).

### MedMention
The Chan-Zuckerberg Initiative is very involved in rare diseases nowadays and has produced MedMention, a dataset annotated with UMLS. The good news is that UMLS supports HPO codes in its metathesaurus. The HPO ontology in itself hosts xrefs to UMLS concepts, so we could gather all those references and use them to gather HPO terms to annotate MedMention. Then the dataset can be included in the corpora used in the project.

### Wikipedia
Wikipedia holds a LOT of information (citation needed citing wikipedia attributing this feat to themselves). Among many other pages there is one dedicated to a list of OMIM diseases and links to disease-specific pages: https://en.wikipedia.org/wiki/List_of_OMIM_disorder_codes.

The goal of this task is to iterate over those (valid = blue) pages and retrieve the text sections. For example, for Dravet syndrome (https://en.wikipedia.org/wiki/Dravet_syndrome), we should get the introduction/header, the Sign and symptoms, the causes (why not?), diagnosis, treatment, epidemiology and history. Basically everything about references. Please also gather in a separate entry/item any blue table with list of symptoms. If this is complicated, leave that last piece of info out.

This dataset can then be incorporated to the current corpora.

### GAN generated data
There are current efforts towards generating medical text with GANs. There is a paper describing how this could be done and available code. The goal is to re-train such system with available sources to augment the dataset. Link to paper: https://www.nature.com/articles/s41746-018-0070-0

### GPT-3 generated data
GPT-3 has taken the World by storm. It is capable of amazing feats thought impossible for the present just some months ago. The team has gained access are is trying to develop a set of input queries such that GPT-3 can generate technical and layperson text related to specific conditions. The challenge is to do this in the current preview version.

Manual testing has produced amazing results, I must add.
 
### OMIM
OMIM has collected a large set of genetic diseases along with their phenotypic (symptom) description. They have an API available to which we have requested access and through which we can query the clinical synopsis of the disease and the disease symptoms. Then, we can compare what terms each algorithm extracts.

We have not managed to get access to OMIM so far, so we are not using this source.

## Performance evaluation
See results at Results.md.

### Introduction 
There are 2 types of performance evaluations:
- Direct evaluation.
- Semantic evaluation.
We will start with direct evaluations due to its simplicity and once the framework has matured enough we suggest to implement the more accurate semantic evaluations.
 
## Direct evaluations
The simplest way to evaluate the performance of a given algorithm is to directly compare the list of detected HPO terms with the list of labelled HPO terms. This can be done with metrics such as the Jaccard Index or similar.
 
## Semantic evaluations
First, an introduction to what semantic similarity means and why it is necessary. The structure of the HPO not only creates a common language through its identifiers, but also creates term dependencies that allow the definition of semantic distances (sometimes referred to as topological distances). A small example of this is that the structure in itself can be leveraged to deduce that short stature is closer to Abnormality of body height than to Hyperglycemia. Also, the fact that a patient presents short stature implies that (s)he has abnormality of the height. However it is clear that knowing that a patient presents Short stature is more informative than knowing that a patient has some height abnormality. Therefore it is important during performance evaluation that we consider the specificity of the terms when doing our evaluations.

![HPO diagram from https://hpo.jax.org/app/tools/loinc2hpo](resources/hpo-diagram.png)

There are many models to evaluate this distances with higher or lower degree of attachment to the graph topology, but an explanation of them is out of the scope of this document. What is important to mention is that not all terms carry the same amount of information towards a diagnosis. For example, the term Phenotypic abnormality does not point to any specific rare disease because any term implies some type of phenotypic abnormality. Formally this is usually expressed by saying that the information content of the term is 0 following the equation `IC = -log(p)`. Being `p` the term probability (`p = n/N`) over the rare diseases. There are variations of this definition, but the core concept remains the same.

## Semantic evaluation metric
There are many metrics to compare phenotype profiles. Topological distance can the be transformed into semantic distance once the term specificity is considered. Our suggestion is to use 2 semantic similarity metrics in order to evaluate how close to the correct set of HPO terms another set of HPO terms is.
1. Patient-similarity package: 
2. Biolink API: The Monarch Initiative develops and maintains Biolink, an API that allows semantic similarity comparisons. The method /sim/compare can be used to compare the extracted HPO set to the original HPO term (comparisons are symmetric). This API also allows the selection of different metrics, including Jaccard (although it would be better to directly implement Jaccard ourselves to reduce traffic to the API). You can use different metrics if desired.
3. Mutual Information (Add-on): All methods in the Biolink API are Jaccard-based or too tight to individual term occurence, rather than coocurence. It would be interesting to also deploy a mutual information model as in https://bmcsystbiol.biomedcentral.com/articles/10.1186/s12918-019-0697-8. In order to do this you need precalculated term information content and crossed information content. Please, do not worry about this for the moment, we will only pay attention to this if time allows it. The reason why trying also this approach is important is that the evaluation with only Biolink heavily relies on the definition of its metrics, which may, for instance overestimate the information provided by generic terms.
 
Each dataset has a different nature and should be analyzed differently.
