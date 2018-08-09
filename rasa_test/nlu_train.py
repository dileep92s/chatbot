# -*- coding: utf-8 -*-

from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

def train_nlu(data, configs, model_dir):
	training_data = load_data(data)
	trainer = Trainer(config.load(configs))
	trainer.train(training_data)
	trainer.persist(model_dir, fixed_model_name = 'nlu')
	
def run_nlu():
	interpreter = Interpreter.load('./models/default/nlu')
	print(interpreter.parse(u"what is wss"))
	
if __name__ == '__main__':
	train_nlu('./data/testData.json', 'config.json', './models')
	run_nlu()