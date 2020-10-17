from utils import *
import streamlit as st
import matplotlib.pyplot as plt
from collections import Counter
# streamlit run app.py
import logging
st.set_option('deprecation.showPyplotGlobalUse', False)
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s -   %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)


def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)


def display_attr_wordcloud(examples):
    wc = get_wordcloud(examples)
    plt.axis("off")
    plt.figure()
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()


def display_attr_distribution(attr_list, attr_name):
    x_labels, y = [], []
    counter = Counter(attr_list)
    for key, value in counter.most_common():
        x_labels.append(key)
        y.append(value)
    x = range(len(x_labels))
    st.markdown(f"<small>Number of {attr_name} in this graph: {len(x_labels)}</small>", unsafe_allow_html=True)
    st.write({i: counter[i] for i in set(attr_list)})
    plt.figure()
    plt.bar(x, y, color='green', align='center')
    plt.title(f'{attr_name} Count')
    plt.xticks(x, x_labels, rotation=90)
    plt.legend()
    for index, value in enumerate(y):
        plt.text(x[index] - .25, value, str(value), fontsize=8)
    plt.tight_layout(h_pad=1.0)
    st.pyplot()


def display_filters(attrs4filter, examples, data_select="", subset_select=""):
    for attr_name in attrs4filter:
        if attr_name in examples[0]:
            if st.checkbox(f"Filter by {attr_name}?"):
                attr_list = get_attr_list(examples, attr_name)
                if st.checkbox(f"Show distribution by {attr_name}"):
                    display_attr_distribution(attr_list, attr_name)

                attr_list_unique = list(set(attr_list))
                attr_options = st.multiselect(f"Query {attr_name}, size={len(attr_list_unique)}", attr_list_unique,
                                              attr_list_unique[0:1])

                attr_selected_examples = filter_by_attr_options(examples, attr_options, attr_name)

                if st.checkbox(f"Show word cloud of examples ({attr_name}={attr_options})?"):
                    display_attr_wordcloud(attr_selected_examples)
                if st.checkbox(f"Show data length of examples ({attr_name}={attr_options})?"):
                    plot_data_dist(attr_selected_examples)
                    st.pyplot()
                # if st.button(f"save selected examples ({attr_name}={attr_options})"):
                #     if write_jsonl(attr_selected_examples,
                #                    f"data_select={data_select}-subset_select={subset_select}-{attr_name}={attr_options}.json"):
                #         st.info(
                #             f"examples saved to: out/data_select={data_select}-subset_select={subset_select}-{attr_name}={attr_options}.json")

                offset = st.number_input(f"Display examples (offset,size={len(attr_selected_examples)})?", value=0,
                                         step=min(1, len(attr_selected_examples) - 1), min_value=0,
                                         max_value=len(attr_selected_examples) - 1)

                for example in attr_selected_examples[offset:offset + min(1, len(attr_selected_examples) - 1)]:
                    if has_id(example):
                        st.markdown(f"[Tweet Link](https://twitter.com/merica/status/{get_id(example)})")
                    st.write(example)


def display_main_panel(examples, data_select="", subset_select=""):
    st.markdown("## Explore")
    if has_id(examples[0]):
        search_id = st.text_input("search by id")
        # print(search_id)
        if search_id.isdigit():
            id2examples = {get_id(example): example for example in examples}

            if search_id in id2examples:
                st.markdown(f"[Tweet Link](https://twitter.com/merica/status/{search_id})")
                st.write(id2examples[search_id])

    offset = st.number_input(f"Display (offset,size={len(examples)})?", value=0,
                             step=min(1, len(examples) - 1 if len(examples) != 0 else 0), min_value=0,
                             max_value=len(examples) - 1 if len(examples) != 0 else 0)

    for example in examples[offset:offset + min(1, len(examples) - 1 if len(examples) != 0 else 0)]:
        if has_id(example):
            st.markdown(f"[Tweet Link](https://twitter.com/merica/status/{get_id(example)})")
        st.write(example)

    if st.checkbox(f"Show data length distribution of all examples?"):
        plot_data_dist(examples)
        st.pyplot()
    if st.checkbox(f"Show world cloud of all examples?"):
        display_attr_wordcloud(examples)

    # if st.button(f"save all examples of selected sets"):
    #     if write_jsonl(examples, f"data_select={data_select}-subset_select={subset_select}-all.json"):
    #         st.info(f"examples saved to: out/data_select={data_select}-subset_select={subset_select}-all.json")


if __name__ == '__main__':
    st.beta_set_page_config(page_title="Crisis Data Explorer", page_icon=":shark:")
    data2path = get_data2path()
    st.title('Inspect Crisis Dataset')

    st.sidebar.title("Dataset from")
    st.sidebar.markdown(
        "[![](https://img.shields.io/github/stars/wangcongcong123/crisis_nlp_progress)](https://github.com/wangcongcong123/crisis_nlp_progress)",
        unsafe_allow_html=True)
    datasets = tuple(data2path.keys())
    data_select = st.sidebar.selectbox("Select a dataset", datasets, index=datasets.index(
        "trecis_short") if "trecis_short" in datasets else 0)  # default
    subdata2path = get_subsets_mappings(data2path[data_select])
    st.sidebar.title("Select subsets")
    data_subsets = list(subdata2path.keys())

    if os.path.isfile(os.path.join(data2path[data_select], "readme.md")):
        st.sidebar.markdown(open(os.path.join(data2path[data_select], "readme.md"), "r").read())

    attrs4filter = []
    if os.path.isfile(os.path.join(data2path[data_select], "attrs4filter.txt")):
        attrs4filter = open(os.path.join(data2path[data_select], "attrs4filter.txt"), "r").read().strip().split(",")

    options = st.sidebar.multiselect("Select one or more subsets to inspect", data_subsets, data_subsets[0:1])
    data_subsets_select = ",".join(options)
    examples = []

    for option in options:
        subset_examples = read_jsonl(subdata2path[option])
        examples.extend(subset_examples)
    if len(examples) == 0:
        st.warning("This dataset is not available yet")
    else:
        st.sidebar.markdown(
            f"You selected data subset(s): **{','.join(options)}**, that contains `{len(examples)}` examples in total",
            unsafe_allow_html=True)

        display_filters(attrs4filter, examples, data_select=data_select, subset_select=options)
        display_main_panel(examples, data_select=data_select, subset_select=options)

    # local_css("style.css")
    # remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    # icon("search")
    # selected = st.text_input("", "Search...")
    # button_clicked = st.button("OK")
    # streamlit run app.py
