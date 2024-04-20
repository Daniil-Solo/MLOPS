"""Script for preparing dataset."""

import click
import pandas as pd

SMALL_SIZE = "small"
NORMAL_SIZE = "normal"
sizes = [SMALL_SIZE, NORMAL_SIZE]


@click.command()  # type: ignore
@click.argument("input_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("output_dataset_file", type=click.Path(writable=True))  # type: ignore
@click.option("--size", type=click.Choice(sizes), default=SMALL_SIZE)  # type: ignore
def cli(input_dataset_file: str, output_dataset_file: str, size: str) -> None:
    """Run dataset preparing.

    :param input_dataset_file: in dataset filepath
    :param output_dataset_file: out dataset filepath
    :param size: size of out feature set
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
    df["target"] = df["G3"]
    SMALL_SIZE_COLUMNS = [
        "isGP",
        "isMale",
        "repChoice",
        "traveltime",
        "studytime",
        "failures",
        "wantsHSE",
        "target",
    ]
    NORMAL_SIZE_COLUMNS = [
        "isGP",
        "isMale",
        "le3FamSize",
        "Medu",
        "Fedu",
        "repChoice",
        "traveltime",
        "studytime",
        "failures",
        "wantsHSE",
        "hasInternet",
        "hasRomantic",
        "freetime",
        "goout",
        "Dalc",
        "Walc",
        "health",
        "absences",
        "target",
    ]
    if size == SMALL_SIZE:
        new_df = df[SMALL_SIZE_COLUMNS]
    elif size == NORMAL_SIZE:
        new_df = df[NORMAL_SIZE_COLUMNS]
    else:
        print(f"Wrong size! Available sizes are: {', '.join(sizes)}")
        return
    new_df.to_csv(output_dataset_file, index=False)
    print("prepared dataset saced as", output_dataset_file, "with size", size)


if __name__ == "__main__":
    cli()
