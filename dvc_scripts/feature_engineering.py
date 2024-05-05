"""Script for features generation."""

import click
import dvc.api
import pandas as pd
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer


@click.command()  # type: ignore
@click.argument("train_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("test_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("train_features_file", type=click.Path(writable=True))  # type: ignore
@click.argument("test_features_file", type=click.Path(writable=True))  # type: ignore
def cli(
    train_dataset_file: str,
    test_dataset_file: str,
    train_features_file: str,
    test_features_file: str,
) -> None:
    """Run features generation.

    :param train_dataset_file:
    :param test_dataset_file:
    :param train_features_file:
    :param test_features_file:
    :return:
    """
    # loading parameters
    params = dvc.api.params_show()
    tf_idf_params = params["tf_idf"]
    # train dataframe
    train_df = pd.read_csv(train_dataset_file)
    train_df["text"] = train_df["text"].fillna("")
    # vectorization train dataframe
    tfidf_vectorizer = TfidfVectorizer(**tf_idf_params)
    tfidf_vectorizer.fit(train_df["text"])
    # saving train data
    train_data = tfidf_vectorizer.transform(train_df["text"])
    sparse.save_npz(train_features_file, train_data)
    del train_df
    del train_data
    # test dataframe
    test_df = pd.read_csv(test_dataset_file)
    test_df["text"] = test_df["text"].fillna("")
    # vectorization test dataframe
    test_data = tfidf_vectorizer.transform(test_df["text"])
    # saving test data
    sparse.save_npz(test_features_file, test_data)


if __name__ == "__main__":
    cli()
