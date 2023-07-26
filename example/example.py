# %%
import pandas as pd

from hyperopt_prophet.training import ProphetHyperOptTrainer, ProphetTrainingParams

# %%

data = pd.read_csv("sample_data.csv")
# %%

model = ProphetHyperOptTrainer(
    training_data=data, training_params=ProphetTrainingParams(_env_file="training.env")
)
# %%
model.fit()
# %%
