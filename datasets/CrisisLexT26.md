## CrisisLexT26

### Keywords
raw-tweets, multi-class-classification, multi-task learning

### Links
[details](https://github.com/sajao/CrisisLex), [download link](https://github.com/sajao/CrisisLex/tree/master/data/CrisisLexT26)

### Count per label
** This subject to change depending on the retrieval date of raw tweets. There are around 1000 examples for each crisis. Since there are 26 crises in total for this dataset, the following statistics are just for `2012_Colorado_wildfires` that comprises 1200 tweets (the rest of crises have the same labeling structure)

```json
8 information types
{
"Other Useful Information":426
"Infrastructure and utilities":71
"Sympathy and support":172
"Not labeled":247
"Not applicable":10
"Donations and volunteering":78
"Affected individuals":151
"Caution and advice":45
}

4 informativeness types
{
"Not related":238
"Related and informative":685
"Related - but not informative":268
"Not applicable":9
}

8 information sources
{
"Government":74
"Media":453
"Not labeled":247
"Not applicable":6
"Business":10
"Eyewitness":66
"NGOs":48
"Outsiders":296
}
```

### Examples
** Here just gives some attributes of each example, there should be more attributes like user or date metadata related to the tweets.

```json
{
"id":211565974422425600
"Informativeness":"Related and informative"
"Information Type":"Caution and advice"
"text":"#Evacuation center Cache La Poudre Middle School 3515 West County Road 54G in Laporte. #Colorado #Wildfire"
"Information Source":"Government"
}

{
"id":211889384608374800
"Informativeness":"Related - but not informative"
"Information Type":"Donations and volunteering"
"text":"RT @HumaneSociety: .@winecountrydog it is still open to large animals just not people #highparkfire"
"Information Source":"NGOs"
}
...
```

### Citation
```
@inproceedings{olteanu2015expect,
  title={What to expect when the unexpected happens: Social media communications across crises},
  author={Olteanu, Alexandra and Vieweg, Sarah and Castillo, Carlos},
  booktitle={Proceedings of the 18th ACM conference on computer supported cooperative work \& social computing},
  pages={994--1009},
  year={2015}
}
```

