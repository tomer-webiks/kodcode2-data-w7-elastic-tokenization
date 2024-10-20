POST /financial_records/_doc/1
{
  "transaction": "Paid $100 for service",
  "amount": "$100"
}

GET /financial_records/_search

POST /financial_records/_doc/2
{
  "transaction": "Paid €50 for service",
  "amount": "€50"
}

GET /financial_records/_analyze
{
    "field": "transaction",
    "text": "I just paid a lot of money, about $100"
}

GET /financial_records/_validate/query?explain=true
{
    "query": {
        "match": {
            "transaction": "paid"
        }
    }
}

GET /financial_records/_explain/1
{
    "query": {
        "match": {
            "transaction": "paid"
        }
    }
}