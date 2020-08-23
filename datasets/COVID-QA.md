## COVID-QA

### Keywords
raw-tweets, question-answering, [SQuAD](https://rajpurkar.github.io/SQuAD-explorer) -like structure.

### Links
[details](https://github.com/deepset-ai/COVID-QA),
[paper](https://openreview.net/forum?id=JENSKEEzsoU), [download link](https://github.com/deepset-ai/COVID-QA/blob/master/data/question-answering/COVID-QA.json)

### Examples

```json
{
  "version":"0.1",
  "categories":[
    {
      "name":"Incubation period",
      "sub_categories":[
        {
          "nq_name":"What is the incubation period of the virus?",
          "kq_name":"Incubation period of the virus",
          "answers":[
            {
              "id":"wuclekt6",
              "title":"Longitudinal analysis of laboratory findings during the process of recovery for patients with COVID-19",
              "exact_answer":"4 days (IQR, 2-7)"
            },            
            {
              "id":"e3t1f0rt",
              "title":"Epidemiological Characteristics of COVID-19; a Systemic Review and Meta-Analysis 1",
              "exact_answer":"5.84 (99% CI: 4.83, 6.85) days"
            },
...
```