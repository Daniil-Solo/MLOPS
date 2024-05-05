"""Script for training model."""

import pickle

import click
import dvc.api
import pandas as pd
from scipy import sparse
from sklearn.linear_model import LogisticRegression


@click.command()  # type: ignore
@click.argument("input_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("features_file", type=click.Path(readable=True))  # type: ignore
@click.argument("output_model_file", type=click.Path(writable=True))  # type: ignore
def cli(input_dataset_file: str, features_file: str, output_model_file: str) -> None:
    """Run model training.

    :param input_dataset_file:
    :param features_file:
    :param output_model_file:
    :return:
    """
    # loading parameters
    params = dvc.api.params_show()
    random_state = params["random_state"]
    model_params = params["logistic_regression"]
    # loading data
    df = pd.read_csv(input_dataset_file)
    target = df["target"]
    del df
    data = sparse.load_npz(features_file)
    # model training
    clf = LogisticRegression(random_state=random_state, **model_params)
    clf.fit(data, target)
    # model saving
    with open(output_model_file, "wb") as f:
        pickle.dump(clf, f)


if __name__ == "__main__":
    cli()
