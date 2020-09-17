#!/bin/bash
echo "Tar-ing..."
tar -czvf model.tar.gz neuron_compiled_bert_model.pt
echo "Uploading to S3"
aws s3 cp model.tar.gz s3://inf1-compiled-bert-model/
