# %%
import pandas as pd

from hyperopt_prophet.training import ProphetHyperOptTrainer, ProphetTrainingParams
from hyperopt_prophet.utils import get_plotly_forecast

# %%

df = pd.read_csv("sample_data.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
# Set 'timestamp' as the index of the DataFrame
df.set_index("timestamp", inplace=True)

# Apply linear interpolation to the remaining columns with missing values
for column in ["gas_prod", "water_prod", "tubing_pressure", "casing_pressure"]:
    for well in ["WL01"]:
        df.loc[df["well_name"] == well, column] = df.loc[
            df["well_name"] == well, column
        ].interpolate(method="time")

df.reset_index(inplace=True)
# %%
model_params = ProphetTrainingParams(
    **{
        "target_col": "gas_prod",
        "id_col": "well_name",
        "time_col": "timestamp",
        "horizon": 365,
        "unit": "day",
        "experiment_id": "1234",
        "max_eval": "5",
        "num_folds": "2",
        "loss_metric": "rmse",
        "base_model_name": "hyperopt_prophet",
        "is_parallel": False,
        "regressors": ["water_prod", "tubing_pressure", "casing_pressure"],
    }
)
model = ProphetHyperOptTrainer(
    training_data=df, training_params=model_params
)
# %%
prophet_model, model_json, result, avg_metrics, prediction = model.fit()

# %%
fig = get_plotly_forecast(prophet_model.model(), prediction)
fig.show()

# %%
