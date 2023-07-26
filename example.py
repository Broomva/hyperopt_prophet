#%%
import pandas as pd

from hyperopt_prophet import training

# %%

data = pd.read_csv('sample_data/data.csv')
# %%

results = training.prophet_hyperopt_training(data)
# %%
