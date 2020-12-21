_Note: this repository was created solely for the purpose of submitting. The commits made to this repository does not accurately represent the individual contributions made by each member._

# Search Based Test Input Generation for Chatbot Testing

#### KAIST 2020 Fall CS454 Team 9
- Jeongeon Park 20160811
- Suro Lee 20160830
- Seungho Kim 20170798
- Chanhee Lee 20170828

## Introduction

In this project, we propose a search-based approach that automatically generates chatbot test input of high quality. Our approach uses the Metropolis-Hasting algorithm, where we improve on an existing paper by N. Miao et al. (2019) to generate input data in the form of questions. Through our comparison with human-generated test input in terms of both the generated test input and the chatbot output when putting in the generated test input, we show that the model-generated test input using our approach is more diverse and relevant to the topic keyword than the human-generated test input.

## Requirements

-   python 3.8
    -   TensorFlow `== 2.3.1` (other versions are not tested)
    -   numpy
    -   pickle
    -   spaCy
        -   run `python -m spacy download en_core_web_lg` to download the required model

## Train Language Model

To use a pre-trained language model, [download](https://drive.google.com/drive/folders/1MRMNEXKjaM_9tI1gdONJaNSO5Xl5k7ZB?usp=sharing) the `forward` and `backward` folders into `model`.

### Usage

`python model/train.py [-h] [--backward]`

### Optional Arguments

`-h, --help`

> shows the help message and exits

`--backward`

> include this argument to train the backward model (instead of the forward model)

`-e, --epoch (type: int, default: 100)`

> sets the maximum number of epochs to run

`-b, --batch (type: int, default: 32)`

> sets the batch size

## Generate Questions

Optional: insert your own keywords from which the questions are generated into `data/input/keywords.txt`.

### Usage

`python model/questions_gen.py`

Generated questions and the steps taken are written into `data/output/output.txt`.

## Evaluation

#### Usage

`python evaluate/diversity.py [-h] [-a A] [-b B]`

#### Optional Arguments

`-h, --help`

> shows the help message and exits

`-a A`

> index of the first message to evaluate (defaults to 0)

`-b B`

> index of the last message to evaluate (defaults to the last index)
