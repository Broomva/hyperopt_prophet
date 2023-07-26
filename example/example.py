# %%
import pandas as pd

from hyperopt_prophet.training import ProphetHyperOptTrainer, ProphetTrainingParams
from hyperopt_prophet.utils import get_plotly_forecast
import logging
logger = logging.getLogger('cmdstanpy')
logger.setLevel(logging.WARNING)
logging.basicConfig(level=logging.WARNING)


# %%

data = pd.read_csv("sample_data.csv")
# %%

model = ProphetHyperOptTrainer(
    training_data=data, training_params=ProphetTrainingParams(_env_file="training.env")
)
# %%
prophet_model, model_json, result, avg_metrics, prediction = model.fit()
# %%
fig = get_plotly_forecast(prophet_model, prediction)
fig.show()
