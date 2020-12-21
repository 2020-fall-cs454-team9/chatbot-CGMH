_Note: this repository was created solely for the purpose of organizing and submitting our finalized project. The commits made to this repository do not accurately represent the individual contributions from each member._

# Search Based Test Input Generation for Chatbot Testing

#### KAIST 2020 Fall CS454 Team 9

-   20160811 Jeongeon Park
-   20160830 Suro Lee
-   20170798 Seungho Kim
-   20170828 Chanhee Lee

## Introduction

In this project, we propose a search-based approach that automatically generates chatbot test input of high quality. Our approach uses the Metropolis-Hastings algorithm, where we improve on an existing paper by N. Miao et al. (2019) to generate input data in the form of questions. Through our comparison with human-generated test input in terms of both the generated test input and the chatbot output when putting in the generated test input, we show that the model-generated test input using our approach is more diverse and relevant to the topic keyword than the human-generated test input.

## Requirements

-   python 3.8

-   Training and generation
    -   TensorFlow `== 2.3.1` (other versions are not tested)
    -   numpy
    -   pickle
-   Evaluation
    -   spaCy
        -   after installing, run `python -m spacy download en_core_web_lg` to download the required model
    -   gensim
    -   pandas
    -   nltk

## Train Language Model

To use a pre-trained language model, [download](https://drive.google.com/drive/folders/1MRMNEXKjaM_9tI1gdONJaNSO5Xl5k7ZB?usp=sharing) the `forward` and `backward` folders into `model`.

### Usage

    $ python model/train.py [-h] [--backward] [-e EPOCH] [-b BATCH]

### Optional Arguments

`-h, --help`

> shows the help message and exits

`--backward`

> include this argument to train the backward model (instead of the forward model)

`-e EPOCH, --epoch EPOCH`

> sets the maximum number of epochs to run (type: int, default: 100)

`-b BATCH, --batch BATCH`

> sets the batch size (type: int, default: 32)

## Generate Questions

Optional: insert your own keywords (from which the questions are generated) into `data/input/keywords.txt`.

### Usage

    $ python model/questions_gen.py

Generated questions are written into `data/output/output.txt`.

## Evaluation: Diversity

The file `evaluate/diversity.py` is used to evaluate both [1] the generated questions and [2] the chatbot's responses.

### Evaluate Generated Questions

1. Generate the questions file `data/output/output.txt`.

2. Use this file's relative path as the `file` argument.

### Evaluate Chatbot Responses

For evaluation, we used Pandorabots' [Kuki](https://www.messenger.com/t/chatbots.io) as our test chatbot.

1. Enter each question into the chat, and download the conversation as a `.json` file.

2. Parse the conversation using `evaluate/parseMessages.py` (for usage, add the `--help` argument for details.)

3. Use the parsed file's relative path as the `file` argument.

### Usage

    $ python evaluate/diversity.py [-h] [--output] [-a A] [-b B] file

### Positional Arguments

`file`

> relative path of the `.txt` file to be used for evaluation.

### Optional Arguments

`-h, --help`

> shows the help message and exits

`--output`

> add this argument to evaluate generated questions (instead of chatbot conversation)

`-a A`

_Only for chatbot responses_

> index of the first message to evaluate (type: int, default: 0)

`-b B`

_Only for chatbot responses_

> index of the last message to evaluate (type: int, default: last index)

## Evaluation: Topic Relevance

The file `evaluate/topic_relevance.py` is used to evaluate the generated questions.

### Evaluate Generated Questions

1. Generate the questions file `data/output/output.txt`.

2. Use the sentences generated in output.txt to put them in the arrays input_text1, 2, and 3.

### Usage
$ python evaluate/topic_relevance.py 

## Example

Train forward/backward language model

    $ python model/train.py

    $ python model/train.py --backward

Generate questions

    $ python model/questions_gen.py

Evaluate diversity of generated questions

    $ python evaluate/diversity.py --output ../data/output/output.txt

Parse and evaluate diversity of chatbot conversation

    $ python evaluate/parseMessages.py message_1.json data.txt

    $ python evaluate/diversity.py data.txt
