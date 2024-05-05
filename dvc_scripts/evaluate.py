"""Script for evaluating model."""

import json
import pickle

import click
import pandas as pd
from scipy import sparse
from sklearn.metrics import accuracy_score, precision_score, recall_score


@click.command()  # type: ignore
@click.argument("input_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("features_file", type=click.Path(readable=True))  # type: ignore
@click.argument("model_file", type=click.Path(readable=True))  # type: ignore
@click.argument("metrics_file", type=click.Path(writable=True))  # type: ignore
def cli(input_dataset_file: str, features_file: str, model_file: str, metrics_file: str) -> None:
    """Run evaluating model.

    :param input_dataset_file:
    :param features_file:
    :param model_file:
    :param metrics_file:
    :return:
    """
    # loading data
    df = pd.read_csv(input_dataset_file)
    target = df["target"]
    del df
    data = sparse.load_npz(features_file)
    # loading model
    with open(model_file, "rb") as f:
        clf = pickle.load(f)
    # evaluating
    predictions = clf.predict(data)
    accuracy = accuracy_score(target, predictions)
    precision = precision_score(target, predictions)
    recall = recall_score(target, predictions)
    metrics = {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
    }
    with open(metrics_file, "w", encoding="utf-8") as f:
        json.dump(metrics, f)


if __name__ == "__main__":
    cli()
