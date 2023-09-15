# PART: Pretrained Authorship Representation Transformer
Focussing on Blog data first. Please download from kaggle "Blog authorship corpus"

## Instructions
* download required libraries
* download data and put it inside 'data/nlp/blog_corpus'
* run gather data notebook
* next run the clean data notebook
* split the data
* u can validate if you want using validation notebook [Data must have pretokenized and decoded text]
* run the bash files


### Currently only testing: 
``` python3 run_experiment.py --devices 1 --model max --blogs --batch_size 10 --vbatch_size 10 --scheduler enable
    python3 run_experiment.py --devices 1 --model mean --blogs --batch_size 10 --vbatch_size 10 --scheduler enab    ```