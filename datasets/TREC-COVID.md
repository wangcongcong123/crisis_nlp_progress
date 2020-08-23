## TREC-COVID
There are five rounds in [TREC-COVID](https://ir.nist.gov/covidSubmit/index.html), each of which covid-related topics (i.e., queries) and relevance-annotated articles are added. In its last round - round 5, there are 50 topics accumulated and more than 50k relevance judgements made to the articles of [CORD-19](https://www.semanticscholar.org/cord19).

### Keywords
scientific-articles, ad-hoc information retrieval, ranking.

### Links
[details](https://ir.nist.gov/covidSubmit/index.html), [download data](https://ir.nist.gov/covidSubmit/data.html), [paper1](https://academic.oup.com/jamia/advance-article/doi/10.1093/jamia/ocaa091/5828938), [paper2](https://ir.nist.gov/covidSubmit/papers/Forum_TRECCOVID1.pdf).

### Topics examples, 
** [link](https://ir.nist.gov/covidSubmit/data/topics-rnd5.xml)

```xml
<topics task="COVIDSearch 2020" batch="5">
  <topic number="1">
    <query>coronavirus origin</query>
    <question>what is the origin of COVID-19</question>
    <narrative>seeking range of information about the SARS-CoV-2 virus's origin, including its evolution, animal source, and first transmission into humans</narrative>
  </topic>

  <topic number="2">
    <query>coronavirus response to weather changes</query>
    <question>how does the coronavirus respond to changes in the weather</question>
    <narrative>seeking range of information about the SARS-CoV-2 virus viability in different weather/climate conditions as well as information related to transmission of the virus in different climate conditions</narrative>
  </topic>
... (48 more)
</topics>
```

### Citation
```
@article{10.1093/jamia/ocaa091,
    author = {Roberts, Kirk and Alam, Tasmeer and Bedrick, Steven and Demner-Fushman, Dina and Lo, Kyle and Soboroff, Ian and Voorhees, Ellen and Wang, Lucy Lu and Hersh, William R},
    title = "{TREC-COVID: rationale and structure of an information retrieval shared task for COVID-19}",
    journal = {Journal of the American Medical Informatics Association},
    year = {2020},
    month = {07},
    abstract = "{TREC-COVID is an information retrieval (IR) shared task initiated to support clinicians and clinical research during the COVID-19 pandemic. IR for pandemics breaks many normal assumptions, which can be seen by examining 9 important basic IR research questions related to pandemic situations. TREC-COVID differs from traditional IR shared task evaluations with special considerations for the expected users, IR modality considerations, topic development, participant requirements, assessment process, relevance criteria, evaluation metrics, iteration process, projected timeline, and the implications of data use as a post-task test collection. This article describes how all these were addressed for the particular requirements of developing IR systems under a pandemic situation. Finally, initial participation numbers are also provided, which demonstrate the tremendous interest the IR community has in this effort.}",
    issn = {1527-974X},
    doi = {10.1093/jamia/ocaa091},
    url = {https://doi.org/10.1093/jamia/ocaa091},
    note = {ocaa091},
    eprint = {https://academic.oup.com/jamia/advance-article-pdf/doi/10.1093/jamia/ocaa091/33472866/ocaa091.pdf},
}

@article{voorhees2020trec,
  title={TREC-COVID: Constructing a Pandemic Information Retrieval Test Collection},
  author={Voorhees, Ellen and Alam, Tasmeer and Bedrick, Steven and Demner-Fushman, Dina and Hersh, William R and Lo, Kyle and Roberts, Kirk and Soboroff, Ian and Wang, Lucy Lu},
  journal={arXiv preprint arXiv:2005.04474},
  year={2020}
}
```