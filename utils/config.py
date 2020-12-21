class config(object):
    def __init__(self):
        # path to data for training language model
        self.data_path='../data/question_data/questions.txt'

        # path to dictionary
        self.dict_path='../data/question_data/dict.pkl'

        # path to keywords used to generate questions from
        self.use_data_path='../data/input/keywords.txt'

        # path to questions generated
        self.use_output_path='../data/output/output.txt'
        
        self.dict_size=30000
        self.vocab_size=self.dict_size+4
        
        self.forward_save_path='../model/forward'
        self.backward_save_path='../model/backward'

        self.shuffle=False
        
        self.batch_size=32
        self.num_steps=50
        self.hidden_size=300
        
        self.max_epoch=100
        
        self.GPU='0'
        self.sample_time=3
        
        self.search_size=100
      
        #self.sample_prior=[1,1,1,1]
        self.action_prob=[0.3,0.3,0.3,0.1]
        self.keyboard_input=False
        self.just_acc_rate=0.0
        self.key_num=4
        self.max_length=10
