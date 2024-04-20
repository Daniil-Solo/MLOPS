"""Script for training model."""

import pickle

import click
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression

LINEAR_REGRESSION = "linear-regression"
RANDOM_FOREST = "random-forest"
models = [LINEAR_REGRESSION, RANDOM_FOREST]


@click.command()  # type: ignore
@click.argument("dataset_file", type=click.Path())  # type: ignore
@click.argument("model_file", type=click.Path(writable=True))  # type: ignore
@click.option("--model", type=click.Choice(models), default=LINEAR_REGRESSION)  # type: ignore
@click.option("--random_state", type=click.INT, default=0)  # type: ignore
def cli(dataset_file: str, model_file: str, model: str, random_state: int) -> None:
    """Run model training.

    :param dataset_file: in dataset filepath
    :param model_file: out model filepath
    :param model: type of model
    :param random_state:
    :return: nothing
    """
    df = pd.read_csv(dataset_file)
    target = df["target"].values
    data = df.drop(["target"], axis=1).values
    if model == LINEAR_REGRESSION:
        reg = LinearRegression()
    elif model == RANDOM_FOREST:
        reg = RandomForestRegressor(random_state=random_state)
    else:
        print(f"Wrong model! Available models are: {', '.join(models)}")
        return
    reg.fit(data, target)
    with open(model_file, "wb") as f:
        pickle.dump(reg, f)
    print(model, "fitted on", dataset_file, "and saved as", model_file)


if __name__ == "__main__":
    cli()
