import os
import sys
sys.path.insert(0, '../utils')

import tensorflow as tf
import numpy as np

from config import config
config=config()

class LangModel():
    def __init__(self, ckpt_path):
        self.ckpt_path = ckpt_path
        self.model = tf.keras.Sequential([
            # B: batch size
            # M: max sentence length
            # H: hidden size
            # V: vocab size
            tf.keras.layers.Masking(mask_value=config.dict_size+3),  # B, M
            tf.keras.layers.Embedding(config.vocab_size, config.hidden_size),  # B, M, H
            tf.keras.layers.LSTM(config.hidden_size, unit_forget_bias=False, return_sequences=True),  # B, M, H
            tf.keras.layers.LSTM(config.hidden_size, unit_forget_bias=False, return_sequences=True),  # B, M, H
            tf.keras.layers.TimeDistributed(tf.keras.layers.Dense(config.vocab_size))  # B, M, V
        ])
        self.softmax = tf.keras.layers.Softmax()
    
    def compile(self):
        def loss(labels, logits):
            return tf.keras.losses.sparse_categorical_crossentropy(labels, logits, from_logits=True)
        self.model.compile(optimizer='adam', loss=loss)

    def run(self, train_dataset, val_dataset, epochs, batch_size):
        checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.ckpt_path,
            monitor='val_loss',
            mode='min',
            save_best_only=True)

        early_callback = tf.keras.callbacks.EarlyStopping()

        self.model.fit(
            train_dataset, 
            epochs=epochs, 
            batch_size=batch_size,
            validation_data=val_dataset, 
            callbacks=[checkpoint_callback, early_callback]
        )

    def predict(self, input):
        if isinstance(input, list):
            input = np.array(input)
        logits = self.model.predict(input)
        probs = self.softmax(logits).numpy()

        return probs

    def restore(self):
        if not os.path.exists(self.ckpt_path):
            raise FileNotFoundError('File {} does not exist'.format(self.ckpt_path))
        self.model = tf.keras.models.load_model(self.ckpt_path, compile=False)