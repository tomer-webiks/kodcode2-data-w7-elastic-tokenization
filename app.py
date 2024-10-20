# create_connection.py
from elasticsearch import Elasticsearch
from es_analyze import analyze

es = Elasticsearch("http://elastic:XEQHTlSw@localhost:9200")  # use your cluster address


# -- 1 -- HTML Strip

# WITHOUT
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        text="<p>Hello <b>World</b>! This is <a href='<http://example.com>'>Elasticsearch</a>.</p>"
    )
)

# WITH
print(
    analyze(es,
        char_filter=["html_strip"],
        tokenizer="standard",
        text="<p>Hello <b>World</b>! This is <a href='<http://example.com>'>Elasticsearch</a>.</p>"
    )
)

# CHAR FILTERS
# -- 2 -- Pattern Replace Char Filter -- PHONE NUMBERS

# WITHOUT
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        text="(123) 456-7890"
    )
)

# WITH
print(
    analyze(es,
        char_filter=[
            {
                "type": "pattern_replace",
                "pattern": "[^0-9]",  # Regex to match non-digit characters
                "replacement": ""     # Replace them with nothing (remove them)
            }
        ],
        tokenizer="standard",
        text="(123) 456-7890"
    )
)


# TOKENIZERS
# -- 3 -- Lowercase -- LOWERCASE

# WITHOUT
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        text="The 2 QUICK Brown-Foxes, jumps_over the lazy-dog's bone."
    )
)

# WITH
print(
    analyze(es,
        char_filter=[],
        tokenizer="lowercase",
        text="The 2 QUICK Brown-Foxes, jumps_over the lazy-dog's bone."
    )
)

# -- 4 -- N-GRAM

# WITHOUT
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        text="Hello Sachin"
    )
)

# WITH
print(
    analyze(es,
        char_filter=[],
        tokenizer={
            "type": "ngram",
            "min_gram": 3,
            "max_gram": 4
        },
        text="Hello Sachin"
    )
)


# TOKEN FILTERS
# -- 5 -- APOSTROPHE

# WITHOUT
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        text="The 2 QUICK Brown-Foxes, jumps_over the lazy-dog's bone."
    )
)

# WITH
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        filter=["apostrophe"],
        text="The 2 QUICK Brown-Foxes, jumps_over the lazy-dog's bone."
    )
)


# -- 6 -- SYNONYM_GRPAH

# WITHOUT
print(
    analyze(es,
        char_filter=[],
        tokenizer="standard",
        text="The 2 QUICK Brown-Foxes, jumps_over the lazy-dog's bone."
    )
)

# WITH
print(
    analyze(es,
        char_filter=[],
        tokenizer="lowercase",
        filter=[
            "lowercase",
            {
              "type": "synonym_graph",
              "synonyms": ["NYC, New York City", "LA, Los Angeles"]
            }
         ],
        text="The 2 QUICK Brown-Foxes, jumps_over the lazy-dog's bone."
    )
)