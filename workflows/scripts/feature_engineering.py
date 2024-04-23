"""Script for preparing dataset."""

import click
import pandas as pd


@click.command()  # type: ignore
@click.argument("input_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("output_dataset_file", type=click.Path(writable=True))  # type: ignore
def cli(input_dataset_file: str, output_dataset_file: str) -> None:
    """Run dataset preparing.

    :param input_dataset_file: in dataset filepath
    :param output_dataset_file: out dataset filepath
    :return: nothing
    """
    df = pd.read_csv(input_dataset_file)
    df["isGP"] = df["school"].apply(lambda x: x == "GP").astype("int32")
    df["isMale"] = df["sex"].apply(lambda x: x == "M").astype("int32")
    df["le3FamSize"] = df["famsize"].apply(lambda x: x == "LE3").astype("int32")
    df["repChoice"] = df["reason"].apply(lambda x: x == "reputation").astype("int32")
    df["wantsHSE"] = df["higher"].apply(lambda x: x == "yes").astype("int32")
    df["hasInternet"] = df["internet"].apply(lambda x: x == "yes").astype("int32")
    df["hasRomantic"] = df["romantic"].apply(lambda x: x == "yes").astype("int32")
    df = df.drop(
        labels=["school", "sex", "famsize", "reason", "higher", "internet", "romantic"],
        axis=1,
    )
    df.to_csv(output_dataset_file, index=False)
    print("prepared dataset saved as", output_dataset_file)


if __name__ == "__main__":
    cli()
