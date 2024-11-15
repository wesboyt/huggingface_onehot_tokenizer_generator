# huggingface_onehot_tokenizer_generator
Simple script which allows users to define their own language without the rigamorale of bad utilities provided by hf.

Notes:

- Change the eos token in the tokenizer config if your language has more than one sentence per context window, I use mine to model discrete games so 1 sentence == 1 game.
- I would add a loop to generate_onehot_tokenizer after the tokens array is initialized where you build your language dictionary. Using '<' and '>' allows discretation of words that might share prefixes. HF's implementation is very fickle I reccomend using the same style as the example.
- The tokenizer folder can be linked to any CLM training loop where you train a model from scratch: "python clm.py --model_type llama --tokenizer_name tokenizer --config_name config.json --train_file train.txt --block_size 128 --per_device_train_batch_size 32"