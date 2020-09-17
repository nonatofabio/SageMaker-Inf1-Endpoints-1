#!/bin/bash

pip install neuron-cc[tensorflow]==1.0.18001.0+0.5312e6a21 torch-neuron==1.5.1.1.0.1532.0 -U --extra-index-url=https://pip.repos.neuron.amazonaws.com
pip install transformers -U
pip show neuron-cc
pip show torch-neuron
pip show transformers
