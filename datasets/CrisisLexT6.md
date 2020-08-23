## CrisisLexT6

### Keywords
raw-tweets, binary-classification, crisis tweets identification and recognition.

### Links
[details](https://github.com/sajao/CrisisLex), [download link](https://github.com/sajao/CrisisLex/tree/master/data/CrisisLexT6)

### Count per label
** This subject to change depending on the retrieval date of raw tweets. There are around 10000 examples for each crisis (6 in total).

```json
{
"off-topic":27620
"on-topic":32462
}
```

### Examples
** Here just gives some attributes of each example, there should be more attributes like user or date metadata related to the tweets.

```json
{
"id":263044104500420609
"label":"on-topic"
"text":"Sandy be soooo mad that she be shattering our doors and shiet #HurricaneSandy"
}

{
"id":262596552399396864
"label":"off-topic"
"text":"I've got enough candles to supply a Mexican family"
}
...
```

### Citation
```
@inproceedings{olteanu2014crisislex,
  title={Crisislex: A lexicon for collecting and filtering microblogged communications in crises},
  author={Olteanu, Alexandra and Castillo, Carlos and Diaz, Fernando and Vieweg, Sarah},
  booktitle={Proceedings of the 8th International AAAI Conference on Weblogs and Social Media (ICWSM'14)},
  number={CONF},
  year={2014}
}
```

