
### Guide to use [TweetsRetrieval](https://crisisnlp.qcri.org/)

The `TweetsRetrieval-1.2-jar-with-dependencies.jar` is a Java-based tool to download full tweets content using tweet ids which can download up to 72K tweets per hour. That is very fast!

Ref: `TweetsRetrieval-1.2-jar-with-dependencies.jar` in this folder is downloaded from [RESOURCE # 8](https://crisisnlp.qcri.org/)

## Steps
##### 1. Put Twitter Keys in the `twitter.properties`
** Go to [Twitter Developer Site](https://developer.twitter.com/en) to apply if you have not got these in hand.
```
consumer.key=<YOURS>
consumer.secret=<YOURS>
access.token=<YOURS>
access.token.secret=<YOURS>
```

##### 2. Prepare a list of tweets ids in `sample_tweet_ids.txt` organized line by line like:
```
1248552109240283136
1239381272583118849
...
```

##### 3. Run the following command to obtain the full content of tweets. 
** You may need to have Java environment ready before run this command
```
java -classpath TweetsRetrieval-1.2-jar-with-dependencies.jar qa.qcri.tweetsretrieval.TweetsRetrievalTool sample_tweet_ids.txt sample_output.txt
```

##### 4. Aha, just enjoy the show for a while, then you will find the tweets in `sample_output.txt`