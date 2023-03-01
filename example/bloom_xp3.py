# from multiprocessing import Pool, cpu_count
import datasets
# from promptsource.utils import load_dataset

all_datasets = [
    # ("duorc", "SelfRC"),
    # ("xquad", "xquad.ar"),
    # ("duorc", "ParaphraseRC"),
    # ("xquad", "xquad.zh"),
    # ("cosmos_qa", None),
    # ("xquad", "xquad.vi"),
    # ("dream", None),
    # ("xquad", "xquad.en"),
    # ("quail", None),
    # ("xquad", "xquad.es"),
    # ("xquad", "xquad.hi"),
    ("wiki_hop", "original"),
    ("gigaword", None),
    ("multi_news", None),
    # ("xsum", None),
    ("khalidalt/tydiqa-primary", "swahili"),
    ("khalidalt/tydiqa-primary", "telugu"),
    # ("great_code", None),
]
_all_datasets = [
    # C3
    # CMRC2018
    # DRCD
    # MLQA
    # CSL
    # TNEWS
    # XLSum
    # WiC
    # XL-WiC
    # BiSECT
    # APPS
    # CodeContests
    # JupyterCodePairs
    # XLCoST
    # CodeComplex
    # Docstring Corpus
    # Flores
    ('glue', 'mrpc'),
    ('glue', 'qqp'),
    ('paws', 'labeled_final'),
    ('ai2_arc', 'ARC-Challenge'),
    ('ai2_arc', 'ARC-Easy'),
    ('kilt_tasks', 'hotpotqa'),
    ('trivia_qa', 'unfiltered'),
    ('web_questions', None),
    ('wiki_qa', None),
    ('adversarial_qa', 'dbidaf'),
    ('adversarial_qa', 'dbert'),
    ('adversarial_qa', 'droberta'),
    ('duorc', 'SelfRC'),
    ('duorc', 'ParaphraseRC'),
    ('ropes', None),
    ('squad_v2', None),
    ('super_glue', 'record'),
    ('quoref', None),
    ('cos_e', 'v1.11'),
    ('cosmos_qa', None),
    ('dream', None),
    ('openbookqa', 'main'),
    ('qasc', None),
    ('quail', None),
    ('quarel', None),
    ('quartz', None),
    ('race', 'high'),
    ('race', 'middle'),
    ('sciq', None),
    ('social_i_qa', None),
    ('super_glue', 'boolq'),
    ('super_glue', 'multirc'),
    ('wiki_hop', 'original'),
    ('wiqa', None),
    ('piqa', None),
    ('amazon_polarity', None),
    ('app_reviews', None),
    ('imdb', None),
    ('rotten_tomatoes', None),
    ('yelp_review_full', None),
    ('common_gen', None),
    ('wiki_bio', None),
    ('cnn_dailymail', '3.0.0'),
    ('gigaword', None),
    ('multi_news', None),
    ('samsum', None),
    ('xsum', None),
    ('ag_news', None),
    ('dbpedia_14', None),
    ('trec', None),
    # Multilingual
    ('GEM/wiki_lingua', 'ar'),
    ('GEM/wiki_lingua', 'en'),
    ('GEM/wiki_lingua', 'es'),
    ('GEM/wiki_lingua', 'fr'),
    ('GEM/wiki_lingua', 'hi'),
    ('GEM/wiki_lingua', 'id'),
    ('GEM/wiki_lingua', 'pt'),
    ('GEM/wiki_lingua', 'vi'),
    ('GEM/wiki_lingua', 'zh'),
    ('Helsinki-NLP/tatoeba_mt', 'ara-eng'),
    ('Helsinki-NLP/tatoeba_mt', 'ara-fra'),
    ('Helsinki-NLP/tatoeba_mt', 'ara-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'ben-eng'),
    ('Helsinki-NLP/tatoeba_mt', 'cat-eng'),
    ('Helsinki-NLP/tatoeba_mt', 'cat-fra'),
    ('Helsinki-NLP/tatoeba_mt', 'cat-por'),
    ('Helsinki-NLP/tatoeba_mt', 'cat-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-cmn_Hans'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-cmn_Hant'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-eus'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-fra'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-hin'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-ind'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-mal'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-mar'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-por'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-run'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-swa'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-tam'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-tel'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-urd'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-vie'),
    ('Helsinki-NLP/tatoeba_mt', 'eng-zho'),
    ('Helsinki-NLP/tatoeba_mt', 'eus-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-cmn_Hans'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-cmn_Hant'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-ind'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-por'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-run'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-vie'),
    ('Helsinki-NLP/tatoeba_mt', 'fra-zho'),
    ('Helsinki-NLP/tatoeba_mt', 'hin-urd'),
    ('Helsinki-NLP/tatoeba_mt', 'hin-zho'),
    ('Helsinki-NLP/tatoeba_mt', 'por-cmn_Hans'),
    ('Helsinki-NLP/tatoeba_mt', 'por-cmn_Hant'),
    ('Helsinki-NLP/tatoeba_mt', 'por-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'por-zho'),
    ('Helsinki-NLP/tatoeba_mt', 'run-spa'),
    ('Helsinki-NLP/tatoeba_mt', 'spa-cmn_Hans'),
    ('Helsinki-NLP/tatoeba_mt', 'spa-cmn_Hant'),
    ('Helsinki-NLP/tatoeba_mt', 'spa-vie'),
    ('Helsinki-NLP/tatoeba_mt', 'spa-zho'),
    ('Helsinki-NLP/tatoeba_mt', 'vie-cmn_Hans'),
    ('Helsinki-NLP/tatoeba_mt', 'vie-zho'),
    ('xquad', 'xquad.ar'),
    ('xquad', 'xquad.zh'),
    ('xquad', 'xquad.vi'),
    ('xquad', 'xquad.en'),
    ('xquad', 'xquad.es'),
    ('xquad', 'xquad.hi'),
    ('paws-x', 'en'),
    ('paws-x', 'es'),
    ('paws-x', 'fr'),
    ('paws-x', 'zh'),
    ('khalidalt/tydiqa-primary', 'arabic'),
    ('khalidalt/tydiqa-primary', 'bengali'),
    ('khalidalt/tydiqa-primary', 'english'),
    ('khalidalt/tydiqa-primary', 'indonesian'),
    ('khalidalt/tydiqa-primary', 'swahili'),
    ('khalidalt/tydiqa-primary', 'telugu'),
    ('khalidalt/tydiqa-goldp', 'arabic'),
    ('khalidalt/tydiqa-goldp', 'bengali'),
    ('khalidalt/tydiqa-goldp', 'english'),
    ('khalidalt/tydiqa-goldp', 'indonesian'),
    ('khalidalt/tydiqa-goldp', 'swahili'),
    ('khalidalt/tydiqa-goldp', 'telugu'),
    ('Muennighoff/mbpp', 'sanitized'),
    ("openai_humaneval", None),
    ("great_code", None),
    ("neural_code_search", "evaluation_dataset"),
    # flores200
]

print(all_datasets)


def download(names):
    d_name, conf_name = names
    try:
        if d_name == "Helsinki-NLP/tatoeba_mt":
            # Fixes a bug when loading a ds where only test split exists
            ds = datasets.load_dataset(
                d_name,
                conf_name,
                download_config=datasets.DownloadConfig(num_proc=1),
                ignore_verifications=True,
                revision="842eb26634a9775f504bb2f3f43cd4cc5f9314d8")
        else:
            ds = datasets.load_dataset(
                d_name,
                conf_name,
                download_config=datasets.DownloadConfig(num_proc=4,
                                                        # resume_download=True,
                                                        ),
            )
    except Exception as e:
        print(f"--- ERROR Dataset ({d_name}, {conf_name})\n")
        print(e)
        print(f"({d_name}, {conf_name})", file=open("todo.txt", "a"))
        return
    print(f"--- DONE Dataset ({d_name}, {conf_name})\n")
    print(f"({d_name}, {conf_name})", file=open("done.txt", "a"))


def download_sp(idx):
    if idx == 1:
        _all_datasets = all_datasets[-50:]
    else:
        _all_datasets = all_datasets[:50]
    for d in _all_datasets:
        download(d)
    print("ALL DONE {idx}")


if __name__ == "__main__":
    # download_mp()
    download_sp(idx=0)
