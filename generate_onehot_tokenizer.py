import json

tokenizer = {
    "version": "1.0",
    "truncation": None,
    "padding": None,
    "added_tokens": [],
    "normalizer": {
        "type": "Sequence",
        "normalizers": [
            {
                "type": "BertNormalizer",
                "clean_text": False,
                "handle_chinese_chars": False,
                "strip_accents": None,
                "lowercase": False
            },
            {
                "type": "Lowercase"
            }
        ]
    },
    "pre_tokenizer": {
        "type": "BertPreTokenizer"
    },
    "post_processor": None,
    "decoder": {
        "type": "BPEDecoder",
        "suffix": "</w>"
    },
    "model": {
        "type": "BPE",
        "dropout": None,
        "unk_token": "<unk>",
        "continuing_subword_prefix": None,
        "end_of_word_suffix": "</w>",
        "fuse_unk": False,
        "byte_fallback": False,
        "ignore_merges": False,
        "vocab": {
            "<unk>": 0
        },
        "merges": []
    }
}

tokens = ["<unk>", "<|startoftext|>", "<|endoftext|>", "<word_one>", "<word_two>"]
for i in range(len(tokens)):
    tokenizer['added_tokens'].append({
      "id": i,
      "content": tokens[i],
      "single_word": False,
      "lstrip": False,
      "rstrip": False,
      "normalized": False,
      "special": True
    })
output = open('./tokenizer/tokenizer.json', 'wt')
output.write(json.dumps(tokenizer))
output.close()
