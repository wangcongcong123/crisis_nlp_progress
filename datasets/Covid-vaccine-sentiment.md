## Covid-vaccine-sentiment

### Keywords
tweets-ids, multi-class-classification

### Links
[details](https://github.com/digitalepidemiologylab/crowdbreaks-paper), [download link](https://github.com/digitalepidemiologylab/crowdbreaks-paper/blob/master/data/vaccine_sentiment_data.csv)

### Count per label
** This subject to change depending on the retrieval date of raw tweets.
```json
{
"0":9236
"1":7598
"-1":2001
}
```

### Examples
** Here just gives some attributes of each example, there should be more attributes like user or date metadata related to the tweets.

```json
{
"id":384866774690582500
"text":"#bono "As we know corruption is killing more kids than TB, AIDS, &amp; malaria put together. There is a vaccine and it’s called transparency.""
"label":"1"
}

{
"id":468606190230835200
"text":"“@UberFacts: On average, people who complain live longer -- Releasing this tension increases immunity and boosts their health.” @GANSIEL"
"label":"0"
}

{
"id":384872905500557300
"text":"@TannersDad @wolfblitzer @andersoncooper @drsanjaygupta http://t.co/nx86CdfQZN. If vaccines don't cause autism , why this package insert?"
"label":"-1"
}
...
```

### Citation
```
@article{muller2019crowdbreaks,
  title={Crowdbreaks: Tracking health trends using public social media data and crowdsourcing},
  author={M{\"u}ller, Martin M and Salath{\'e}, Marcel},
  journal={Frontiers in public health},
  volume={7},
  year={2019},
  publisher={Frontiers Media SA}
}
```

