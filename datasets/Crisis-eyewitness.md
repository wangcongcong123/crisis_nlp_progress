## Crisis-eyewitness

### Keywords
raw-tweets, multi-class or binary classification.

### Links
[paper](https://reader.elsevier.com/reader/sd/pii/S0306457319303590?token=F160A6D847FC35A20C43436D67AF60E8B481D9E980E7BB5132494CF1B3EC631BACA1D40214DCF485C76B76E3997DE07E), [download link](https://crisisnlp.qcri.org/data/eyewitness_tweets_annotations_14k_public.zip)

### Examples

```json
{
"text":"I was wondering why the room was shaking when I was trying to sleep ... I found out it was an earthquake. I bring disasters with me"
"label":"direct-eyewitness"
}

{
"text":"F*cking hell...my wife and kids are in Tokyo and they're in the middle of an earthquake Jesus Murphy just how crap can one day get?"
"label":"indirect-eyewitness"
}

{
"text":"It was 90 degrees at noon and now we have a thunder storm and flash flood warning.... welcome to SoCal"
"label":"vulnerable-direct witness"
}
...
```

### Citation
```
@article{zahra2020automatic,
  title={Automatic identification of eyewitness messages on twitter during disasters},
  author={Zahra, Kiran and Imran, Muhammad and Ostermann, Frank O},
  journal={Information processing \& management},
  volume={57},
  number={1},
  pages={102107},
  year={2020},
  publisher={Elsevier}
}

```