"""Script for preparing dataset."""

import re
from functools import lru_cache

import click
import nltk
import pandas as pd
from nltk.stem.snowball import EnglishStemmer

nltk.download("punkt")
stemmer = EnglishStemmer()


@lru_cache(maxsize=10240, typed=True)
def stem_with_cache(w: str) -> str:
    """Run stemming with using cache.

    :param w:
    :return:
    """
    return str(stemmer.stem(w))


@click.command()  # type: ignore
@click.argument("input_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("output_dataset_file", type=click.Path(writable=True))  # type: ignore
def cli(input_dataset_file: str, output_dataset_file: str) -> None:
    """Run dataset preparing.

    :param input_dataset_file: in dataset filepath
    :param output_dataset_file: out dataset filepath
    :return: nothing
    """
    df = pd.read_csv(input_dataset_file, names=["class", "title", "text"])
    # Missing values
    df = df[~(df["title"].isnull() & df["text"].isnull())]
    df["title"] = df["title"].apply(lambda x: "" if pd.isna(x) else x)
    # Text processing - concatenating
    df["all_text"] = df["title"] + ", " + df["text"]
    del df["title"]
    del df["text"]
    # Text processing - lowering
    df["lowered_text"] = df["all_text"].apply(lambda x: x.lower())
    del df["all_text"]
    # Text processing - cleaning
    df["cleaned_text"] = df["lowered_text"].apply(lambda x: " ".join(re.findall("[-a-z]{2,}", x)))
    del df["lowered_text"]
    # Text processing - stemming
    df["text"] = df["cleaned_text"].apply(
        lambda x: " ".join(stem_with_cache(w) for w in x.split(" "))
    )
    del df["cleaned_text"]
    # Transform class to target
    df["target"] = df["class"].apply(lambda x: 0 if x == 1 else 1)
    del df["class"]
    # Saving
    df.to_csv(output_dataset_file, index=False)
    print("prepared dataset saved as", output_dataset_file)


if __name__ == "__main__":
    cli()
