# Demonstrate how to load a model and predict with it:

# load a model
from fastai.basic_data import load_data
from fastai.text import AWD_LSTM, language_model_learner, load_learner

class PredictionModel(object):
    def __init__(self):
        # Make sure size matches file path name
        dataset_size="small-100"
        checkpoint_key="AWD_LSTM-clean-5_15"
        print(f"Processing {dataset_size} dataset.",flush=True)
        path=f"datasets/{dataset_size}"
        model_filename="models/bullying_model-AWD_LSTM-clean-5_15_1-exported"

        model_type=AWD_LSTM

        model_path=f"{path}/{model_filename}"

        print("Loading the model",flush=True)

        # Make sure file path is correct
        self.learn=load_learner(path="datasets/small-100")

    def predict(text):
        return learn.predict(text)

if __name__ == '__main__':
    predictionModel = PredictionModel()

#probabilities = learn.predict("Hey, how is it going?")

#print(f"P(is_bullying)={probabilities[2][1]}")
