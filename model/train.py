import sys
sys.path.insert(0, '../utils')
import reader

from config import config
config=config()


from model import LangModel

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--backward', dest='backward', action='store_true', help='train the backward model (default is forward)')
parser.add_argument('-e', '--epoch', type=int, default=config.max_epoch, help="maximum number of epochs to run; default = {}".format(config.max_epoch))
parser.add_argument('-b', '--batch', type=int, default=config.batch_size, help="batch size; default = {}".format(config.batch_size))
args = parser.parse_args()

from utils import *
import numpy as np
import tensorflow as tf

# Define model and restore checkpoint if created

model = LangModel(config.backward_save_path if args.backward else config.forward_save_path)
model.restore()

# Train chosen model

print('Training {} language model'.format('backward' if args.backward else 'forward'))
train_data, train_sequence_length, test_data, test_sequence_length = reader.read_data(config.data_path, config.num_steps, is_backward=True)
model.compile()
model.run(train_data, test_data, args.epoch, args.batch)