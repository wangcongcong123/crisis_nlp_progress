## Covid-category

### Keywords
tweets-ids, binary-classification, Amazon-Turk-Annotation

### Links
[details](https://github.com/digitalepidemiologylab/covid-twitter-bert/tree/master/datasets/covid_category), [download link](https://raw.githubusercontent.com/digitalepidemiologylab/covid-twitter-bert/master/datasets/covid_category/covid_category.csv)

### Count per label
** This subject to change depending on the retrieval date of raw tweets.
```json
{
"category_personal":1458
"category_news":3116
}
```

### Examples
** Here just gives some attributes of each example, there should be more attributes like user or date metadata related to the tweets.

```json
{
"id":1223462053030985700
"text":"Thank you @CebuPacificAir for cancelling all flights between PH and mainland China from Feb 2 to March 29, 2020 . I… https://t.co/vGnzk0H8d2"
"label":"category_personal"
}

{
"id":1230417893998751700
"text":"Samsung says Galaxy factories in Vietnam running 'at full capacity' #vietnam https://t.co/9MuUxVtM9z"
"label":"category_news"
}
...
```

### Citation
```
@article{muller2020covid,
  title={COVID-Twitter-BERT: A Natural Language Processing Model to Analyse COVID-19 Content on Twitter},
  author={M{\"u}ller, Martin and Salath{\'e}, Marcel and Kummervold, Per E},
  journal={arXiv preprint arXiv:2005.07503},
  year={2020}
}
```

