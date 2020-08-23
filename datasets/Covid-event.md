## Covid-event

### Keywords
tweets-ids, classification, sequence-tagging, question-answering.

### Links
[details](https://github.com/viczong/extract_COVID19_events_from_Twitter),
[paper](https://arxiv.org/abs/2006.02567), [label details](https://docs.google.com/document/d/1OWFTXOZpoXNrDULq6PFXvIGarSZwpU-uLQRuV4wrJwI/edit#heading=h.xdwa0w128gtb)

### Count per event
** This subject to change depending on the retrieval date of raw tweets.
```json
{
"can_not_test":1128
"negative":1142
"death":1231
"cure_and_prevention":1246
"positive":2402
}
```

### Examples
** Here just gives some attributes of each example, there should be more attributes like user or date metadata related to the tweets.

```json
{
"id":"1242297314640789505"
"event_type":"can_not_test"
"slot_type":"part2-when.Response"
"context":"And they still can’t get tested to be sure. And they can’t be admitted to the hospital without a positive test, or a real life threatening emergency. I’m the first to graduate out of my sisters, my mom and her sister, my grandma... and so on. And I might not get to walk."
"question":"When is the can’t-be-tested situation reported?"
"choices":"not specified, the hospital without a positive test, they, can’t, the hospital, a positive test, a real life, emergency, the first, my sisters, my mom, her sister, my grandma, I"
"answer":"not specified"
}

{
"id":"1240098086652952577"
"event_type":"can_not_test"
"slot_type":"part2-symptoms.Response"
"context":"The number of dead has risen by 7 in the past 3 hours. Unemployed is exactly to grow to 20%. This is an epic emergency! And my friend has been unbelievably sick for a week and can’t get tested. #coronavirus #COVID19 #pandemic"
"question":"Is the untested person currently experiencing any COVID-19 related symptoms?"
"choices":"yes, no, not specified"
"answer":"yes"
}

{
"id":"1238928718447308800"
"event_type":"can_not_test"
"slot_type":"part2-name.Response"
"context":"@sheltgarner @chrislhayes Seattle here. . .Our schools are closed and our kids want to go to the mall. Grocery store shelves are barren as people are preparing. But it just seems so surreal that we're all still out and about spreading it further. (BTW: we still can't get tested)"
"question":"Who can not get a test?"
"choices":"author of the tweet, not specified, Seattle, Our schools, our kids, the mall. Grocery store shelves, people, we're all, we, can't"
"answer":"author of the tweet"
}
...
```

### Citation
```
@misc{zong2020extracting,
    title={Extracting COVID-19 Events from Twitter},
    author={Shi Zong and Ashutosh Baheti and Wei Xu and Alan Ritter},
    year={2020},
    eprint={2006.02567},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
}
```