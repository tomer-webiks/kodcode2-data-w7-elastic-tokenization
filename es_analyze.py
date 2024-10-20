def analyze(es, char_filter, tokenizer, filter=[], text=""):
    response = es.indices.analyze(
        body={
            "char_filter": char_filter,
            "tokenizer": tokenizer,
            "filter": filter,
            "text": text
        }
    )

    # Extract tokens
    tokens = [token['token'] for token in response['tokens']]
    return tokens

