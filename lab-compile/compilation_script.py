#!/usr/bin/env python

import torch
import torch_neuron
import transformers
from transformers import BertTokenizer
from transformers import BertModel
import math
from transformers import AutoTokenizer, AutoModelForSequenceClassification

sentence1="If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."
sentence2="The greatest glory in living lies not in never falling, but in rising every time we fall."
sentence3="If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success. If you set your goals ridiculously high and it's a failure, you will fail above everyone else's success."

tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

encoded_sentence = tokenizer.encode_plus(sentence1, sentence3, max_length=128, pad_to_max_length=True, return_tensors="pt")

example_inputs = encoded_sentence['input_ids'], encoded_sentence['attention_mask'], encoded_sentence['token_type_ids']
model_neuron = torch.neuron.trace(model, example_inputs, compiler_args=['-O2'], verbose=1, compiler_workdir='./compile')

#model_neuron.save('test.pt')
