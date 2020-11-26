import json
import os
import glob
import re
from wordcloud import WordCloud, STOPWORDS
import numpy as np
import pandas as pd
import logging
import matplotlib.pyplot as plt

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

def read_jsonl(filepath):
    examples = []
    with open(filepath, "r",encoding="utf-8") as f:
        for line in f:
            example = json.loads(line.strip())
            examples.append(example)
    return examples


def write_jsonl(examples,filepath):
    if not os.path.isdir("out"):
        os.makedirs("out",exist_ok=True)
    with open("out/"+filepath, "w+") as f:
        for example in examples:
            f.write(json.dumps(example) + "\n")
    return True


def get_attr_list(examples, attr_name):
    attr_list = []
    for example in examples:
        if isinstance(example[attr_name], list):
            attr_list.extend(example[attr_name])
        if ", " in example[attr_name]:
            attr_list.extend(example[attr_name].split(", "))
        if "," in example[attr_name]:
            attr_list.extend(example[attr_name].split(","))
        else:
            attr_list.append(example[attr_name])
    return attr_list


def get_text_name(example):
    if "content" in example:
        return "content"
    elif "context" in example:
        return "context"
    elif "full_text" in example:
        return "full_text"
    else:
        return "text"


def get_wordcloud(examples):
    cleand_tokens = []
    for example in examples:
        text_name = get_text_name(example)
        for token in example[text_name].split():
            if re.match('^[a-zA-Z0-9_]+$', token) and not token.lower().startswith(
                    "rt") and not token.lower().startswith("http") and len(token) > 3:
                cleand_tokens.append(token.lower())
    cleaned_text = " ".join(cleand_tokens)
    wc = WordCloud(stopwords=STOPWORDS, margin=1, max_words=2000, background_color='white').generate(cleaned_text)
    return wc

def get_data2path(scan_scope="data"):
    data2path = {}
    for folder_name in os.listdir(scan_scope):
        if os.path.isdir(os.path.join(scan_scope, folder_name)):
            data2path[folder_name] = os.path.join(scan_scope, folder_name)
    return data2path


def get_subsets_mappings(path):
    subdata2path = {}
    subnames = glob.glob(os.path.join(path, "*.json"))
    for each_sub in subnames:
        subdata2path[each_sub.split(os.sep)[-1].split(".")[0]] = each_sub
    return subdata2path


def has_id(example):
    return "post_id" in example or "id" in example


def get_id(example):
    return example["post_id"] if "post_id" in example else example["id"]

def filter_by_attr_options(examples, attr_options, attr_name):
    return_examples = []
    for example in examples:
        # if any(example[attr_name] in option for option in attr_options):
        #     return_examples.append(example)
        if set(example[attr_name].split(",")).intersection(set(attr_options)):
            return_examples.append(example)


    return return_examples


def get_len_stats(examples, tokenizer=lambda a: a.split()):
    fieldname=get_text_name(examples[0])
    docs = [example[fieldname] for example in examples]
    doclen2count = {}
    for doc in docs:
        len_doc = len(tokenizer(doc))
        if len_doc in doclen2count:
            doclen2count[len_doc] += 1
        else:
            doclen2count[len_doc] = 1
    len_list = []
    for doclen, count in doclen2count.items():
        len_list.extend([doclen] * count)
    return np.std(len_list), np.average(len_list), doclen2count, len_list


def plot_data_dist(examples, savefig=None, show_boxplot=True, dataname=""):
    std, avg, doclen2count, len_list = get_len_stats(examples) # by default using space splitter
    if show_boxplot:
        plt.subplot(121)
    else:
        plt.subplot(111)

    plt.title(f"{dataname} (std. {std:.2f}, size {len(len_list)})", fontsize=10)
    plt.xlabel("Number of words (sample length)")
    plt.ylabel("Number of samples")
    plt.bar([e for e in doclen2count], [doclen2count[e] for e in doclen2count])

    if show_boxplot:
        plt.subplot(122)
        # plt.boxplot(len_list)
        plt.title(f"{dataname} (min. {min(len_list)}, avg. {avg:.2f}, max. {max(len_list)})", fontsize=10)
        df = pd.DataFrame([len_list], index=[''])
        df.T.boxplot(vert=False)

    if savefig is not None:
        logger.info(f"saved data dist fig to {savefig}")
        plt.savefig(savefig, bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    examples = read_jsonl("data/eyewitness_tweets/hurricanes_eyewitness_annotations_2004.json")
    # filtered=get_attr_list(examples,"label")
    # print(filtered)
    # import matplotlib.pyplot as plt
    plot_data_dist(examples)