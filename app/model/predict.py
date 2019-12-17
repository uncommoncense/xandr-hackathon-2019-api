# Demonstrate how to load a model and predict with it:

# load a model
from fastai.text import load_learner


class PredictionModel(object):
    def __init__(self):
        dataset_size = "large"
        print(f"Processing {dataset_size} dataset.", flush=True)
        path=f"datasets/{dataset_size}"

        print("Loading the model", flush=True)
        self._learn = load_learner(path=path)
        print("Done loading the model", flush=True)

    def predict(self, text):
        print(f"{text}")
        probabilities = self._learn.predict(text)
        print(f"P(is_bullying)={probabilities[2][1]}")
        return float(probabilities[2][1])


if __name__ == '__main__':
    predictionModel = PredictionModel()
