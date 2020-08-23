## TREC-IS

This dataset include subsets from its multiple editions of the [IS-track](http://dcs.gla.ac.uk/~richardm/TREC_IS/) since 2018, as of 2020a, the subsets include, 2018, 2019a, 2019b and 2020a-task1-2 and 2020a-covid. The dataset is likely to be accumulated as it has more editions in the future.

### Keywords
tweets-ids, multi-label-classification, multi-task learning, ranking.

### Links
[details](http://dcs.gla.ac.uk/~richardm/TREC_IS/), [download link](http://dcs.gla.ac.uk/~richardm/TREC_IS/2019/2019_Instructions.html)

### Count per label
** This subject to change depending on the retrieval date of raw tweets. There are a subset of this dataset specifically designed for covid-related tweets. The following does not take that into account.
```json
4 prioirty levels (single-label annotations)
{
"High":3823
"Medium":5933
"Low":30254
"Critical":449
}

25 information types (multi-label annotations)
{
"Report-Official":1607
"Report-News":11061
"Report-Factoid":8021
"CallToAction-Volunteer":168
"Report-Location":9491
"Other-Advice":2018
"Report-EmergingThreats":2676
"Other-Discussion":3019
"CallToAction-MovePeople":300
"Report-NewSubEvent":853
"Report-ThirdPartyObservation":6969
"Report-ServiceAvailable":1379
"Report-FirstPartyObservation":4435
"Request-SearchAndRescue":242
"Other-Irrelevant":10689
"Report-Weather":3562
"Other-Sentiment":8870
"Other-ContextualInformation":2184
"Report-Hashtags":10459
"Request-GoodsServices":153
"CallToAction-Donations":858
"Report-MultimediaShare":10647
"Request-InformationWanted":289
"Report-CleanUp":186
"Report-OriginalEvent":2999
}

```

### Examples
** Here just gives some attributes of each example, there should be more attributes like user or date metadata related to the tweets.

```json
{
"event_id":"guatemalaEarthquake2012"
"post_id":"266804609954234369"
"text":"RT @adamlevine: Guys, let's help raise funds for the @RedCross for those in need in the #Guatemala #earthquake http://t.co/6u9oY7sh"
"categories":"CallToAction-Donations,Report-ServiceAvailable,Report-News"
"priority":"Medium"
"timestamp":"6 Sep 2018 18:03:17 GMT"
}

{
"event_id":"albertaWildfires2019"
"post_id":"1132650970775793665"
"text":"Our @JWongGlobalNews is reporting live on the #HighLevel firefight again this morning. Today: winds are expected to shift. From Julia's reports: w/ fire just a few km away those winds could push it even closer to town. We'll update conditions with her @GlobalEdmonton"
"categories":"Report-ThirdPartyObservation,Report-Weather,Report-Location,Report-EmergingThreats,Report-Hashtags,Report-News"
"priority":"Medium"
"timestamp":"7 Jun 2019 15:46:33 GMT"
}
...
```

### Citation
```
@article{mccreadie2019trec,
  title={Trec incident streams: Finding actionable information on social media},
  author={McCreadie, Richard and Buntain, Cody and Soboroff, Ian},
  year={2019}
}

@article{mccreadie2020incident,
  title={Incident Streams 2019: Actionable Insights and How to Find Them},
  author={McCreadie, Richard and Buntain, Cody and Soboroff, Ian},
  year={2020}
}
```

