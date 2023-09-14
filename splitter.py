# splitter.py

from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("roberta-large")
import pandas as pd

CHUNK_SIZE = 64

def split_data(row):
    eid, values = row
    input_ids = tokenizer(values.text).input_ids
    chunked = [input_ids[chunk: chunk + CHUNK_SIZE] for chunk in range(0, len(input_ids), CHUNK_SIZE)]
    decoded_chunked = tokenizer.batch_decode(chunked)
    return pd.DataFrame({'id': [eid]*len(chunked),
                         'pretokenized_text': chunked,
                         'decoded_text': decoded_chunked})
