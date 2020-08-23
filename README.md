## Crisis-NLP-Progress: Tracking resources related to computational linguistical techniques for emergency response.

### Table of contents

- [Datasets](#datasets)
- [Tools](#tools)
- [Papers](#papers)
- [Conferences and Journals](#conferences)
- [Misc](#misc)


<a name="datasets"></a>
### Datasets

- [TREC-COVID](datasets/TREC-COVID.md) - scientific articles annotated by relevance (relevant, partially-relevant, and non-relevant) from [the TREC COVID track](https://ir.nist.gov/covidSubmit/) using [CORD-19 dataset](https://www.semanticscholar.org/cord19).
- [Covid-category](datasets/Covid-category.md) - tweets for training [CT-BERT](https://github.com/digitalepidemiologylab/covid-twitter-bert), annotated with either "category_personal" (33.3%) or "category_news" (66.7%).
- [Covid-vaccine-sentiment](datasets/Covid-vaccine-sentiment.md) - covid-related tweets on vaccine sentiment annotated with three sentiments "1", "-1" or "0".
- [Covid-event](datasets/Covid-event.md) - tweets categorised in five covid-related events, "Tested Positive", "Tested Negative", "Can not test", "Death", "Cure and Prevention". For each event, tweets are annotated with different several slot questions.
- [COVID-QA](datasets/COVID-QA.md) -  a question answering   dataset consisting of 2,019 question/answer pairs annotated  by volunteer biomedical experts on scientific articles related to  COVID-19. The articles are 147 scientific articles selected from the [CORD-19 dataset](https://www.semanticscholar.org/cord19).
- [CrisisLexT26](datasets/CrisisLexT26.md) - tweets categorised in 26 crises, annotated by 8 information types, 4 types of informativeness, and 8 types of information sources. 
- [CrisisLexT6](datasets/CrisisLexT6.md) - tweets categorised in 6 crises, annotated by binary relatedness, either "off-topic" or "on-topic".
- [Crisis-eyewitness](datasets/Crisis-eyewitness.md) -  comprises around 14,000 tweets categorised in four types of disaster, i.e., hurricanes, earthquakes, floods, and forest fires. These tweets are annotated by a taxonomy of eyewitness types, such as "direct-eyewitness", "indirect-eyewitness", "vulnerable-direct witness", etc.
- [TREC-IS](datasets/TREC-IS.md) - around 50k as of the 2020-a round of [the IS track](http://dcs.gla.ac.uk/~richardm/TREC_IS/). These tweets are annotated by a taxonomy of 25 information types (multi-label annotations), and 4 levels of priority describing the criticality of the tweets (single-label annotations).
 - to add  un-labeled data. For adding a new relevant dataset to this repository, please refer to [this guide](datasets/)

<a name="tools"></a>
### Tools
- [TweetsRetrieval](tools/TweetsRetrieval) - very fast Java-based tweets retrieval via tweets ids.
- [TweepyCalls](tools/TweepyCalls) - various functions for calling Twitter-API using Tweepy.
- [Twarc](https://github.com/DocNow/twarc) - A command line tool (and Python library) for archiving Twitter JSON.

<a name="papers"></a>
### Papers

#### Transformers relevant
- 2020: [COVID-Twitter-BERT: A Natural Language Processing Model to Analyse COVID-19 Content on Twitter](https://arxiv.org/abs/2005.07503)
- 2020: [CrisisBERT: a Robust Transformer for Crisis Classification and Contextual Crisis Embedding](https://arxiv.org/abs/2005.06627) -crisis tweets recognition and classification

#### Other NNs relevant
- 2020: [On Identifying Hashtags in Disaster Twitter Data](https://arxiv.org/abs/2001.01323) - Multi-task learning, classification, LSTM.
- 2020: [A deep multi-modal neural network for informative Twitter content classification during emergencies](https://link.springer.com/article/10.1007/s10479-020-03514-x) - multi-modal classification, VGG-16 and LSTM.
- 2020: [Classification for Crisis-Related Tweets Leveraging Word Embeddings and Data Augmentation](https://trec.nist.gov/pubs/trec28/papers/CS-UCD.IS.pdf) - data augmentation, word embeddings.
- 2019: [Label Embedding using Hierarchical Structure of Labels for Twitter Classification](https://www.aclweb.org/anthology/D19-1660/) - label embedding, hierarchical multi-label classification.
- 2018: [Deep Neural Networks versus Naive Bayes Classifiers for Identifying Informative Tweets during Disasters](https://www.cs.uic.edu/~cornelia/papers/iscram18_deep.pdf) - RNN, CNN, and traditional ML.
- 2018: [Convolutional neural network for earthquake detection and location](https://advances.sciencemag.org/content/4/2/e1700578), CNN.
- 2017: [Robust Classification of Crisis-Related Data on Social Networks Using Convolutional Neural Networks](https://mimran.me/papers/robust_classification_of_crisis_data_on_social_media_using_cnn_icwsm2017.pdf) - CNN, classification.

#### Other methods
- 2011: [Classifying Text Messages for the Haiti Earthquake](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.370.6804&rep=rep1&type=pdf)

#### Survey
- 2017: [Fifteen years of social media in emergencies: A retrospective review and future directions for crisis Informatics](https://onlinelibrary.wiley.com/doi/full/10.1111/1468-5973.12196)
- 2016: [An Overview of Sentiment Analysis in Social Media and Its Applications in Disaster Relief](https://link.springer.com/chapter/10.1007/978-3-319-30319-2_13)
- 2015: [Processing Social Media Messages in Mass Emergency: A Survey](https://dl.acm.org/doi/abs/10.1145/2771588?casa_token=b-r6_iKyK2EAAAAA:F76AORZth50Br_ZqwcMyPMAxCBOLm1GYFN9hzMIF5xth89KAR4VaNgzDPs5vox-MjD_3IxqOQxqOQg)

<a name="conferences"></a>
#### Conferences and Journals
- [AAAI: The AAAI Conference on Artificial Intelligence](https://aaai.org/Conferences/AAAI-20/)
- [SIGIR: The International ACM SIGIR Conference on Research and Development in Information Retrieval](https://sigir.org/sigir2020/)
- [ACL: The Annual Meeting of the Association for
Computational Linguistics](https://acl2020.org/)
- [CIKM: The International Conference on Information and Knowledge Managemen](https://www.cikm2020.org/)
- [WWW: The International World Wide Web Conference](https://www2020.thewebconf.org/)
- [WSDM: The ACM International Conference on Web Search and Data Mining](http://www.wsdm-conference.org/2021/)
- [EMNLP: The Conference on Empirical Methods in Natural Language Processing](https://2020.emnlp.org/)
- [IJCAI: International Joint Conferences on Artificial Intelligence Organization](https://www.ijcai.org/)
- [ECIR: The annual European Conference on Information Retrieval](https://ecir2020.org/)
- [ISCRAM: The Information Systems for Crisis Response and Management](https://iscram.org/)
- [COLING: International Conference on Computational Linguistics](https://coling2020.org/)
- [NLP-IR: International Conference on Natural Language Processing and Information Retrieval](http://www.nlpir.net/)
- [LREC: The Conference on Language Resources and Evaluation](https://lrec2020.lrec-conf.org/en/)
- [ICWSM: International AAAI Conference on Web and Social Media](https://www.icwsm.org/2020/index.html)
- [ASONAM: The IEEE/ACM International Conference on Advances in Social Networks Analysis and Mining](http://asonam.cpsc.ucalgary.ca/2020/)
- [ACM Computing Surveys](https://dl.acm.org/journal/csur)
- [IEEE Computational Intelligence Magazine](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=10207)
- [Journal of Contingencies and Crisis Management](https://onlinelibrary.wiley.com/journal/14685973)

<a name="misc"></a>
### Misc.

- [CrisisNLP](https://crisisnlp.qcri.org/) - contains a decent number of resources for research on crisis informatics topics.
- [CrisisLex](https://crisislex.org/) - a repository of crisis-related social media data and tools including collections of crisis data and a lexicon of crisis terms

#### Contribution
The items included here so far are by no means completed but used as a starting point for the community's effort to make this list better and comprehensive. Hence, this repository welcomes the contribution from the community. If you find any items missed here, just pull requests to add them or email me at [wangcongcongcc@gmail.com](#).