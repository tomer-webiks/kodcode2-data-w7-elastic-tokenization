PUT /product_index
{
  "settings": {
    "analysis": {
      "char_filter": {
        "html_strip": {
          "type": "html_strip"
        },
        "product_name_cleaner": {
          "type": "pattern_replace",
          "pattern": "[^A-Za-z0-9 ]",
          "replacement": ""
        }
      },
      "tokenizer": {
        "edge_ngram_tokenizer": {
          "type": "edge_ngram",
          "min_gram": 3,
          "max_gram": 10,
          "token_chars": ["letter", "digit"]
        }
      },
      "filter": {
        "lowercase": {
          "type": "lowercase"
        }
      },
      "analyzer": {
        "product_analyzer": {
          "type": "custom",
          "char_filter": ["html_strip", "product_name_cleaner"],
          "tokenizer": "edge_ngram_tokenizer",
          "filter": ["lowercase"]
        }
      }
    }
  }
}


POST /product_index/_doc/1
{
  "product_name": "<h1>Apple iPhone 13</h1>",
  "description": "Latest Apple smartphone with 128GB storage.",
  "price": 799.99
}

POST /product_index/_doc/2
{
  "product_name": "<h2>Samsung Galaxy S21</h2>",
  "description": "Samsung flagship smartphone with 256GB storage.",
  "price": 999.99
}

POST /product_index/_doc/3
{
  "product_name": "<p>Google Pixel 6</p>",
  "description": "Newest Google phone with AI camera features.",
  "price": 699.99
}



GET /product_index/_search
{
  "query": {
    "match": {
      "product_name": {
        "query": "gala",
        "analyzer": "product_analyzer"
      }
    }
  }
}


POST /product_index/_analyze
{
  "analyzer": "product_analyzer",
  "text": "<h1>Samsung Galaxy</h1>"
}