"""Script for sampling features from dataset."""

from pathlib import Path

import click
import pandas as pd
from hydra import compose, initialize
from omegaconf import DictConfig


def compose_config(
    overrides: list[str] | None = None,
) -> DictConfig:
    """Build config with overriding params.

    :param overrides: params with override values
    :return: config
    """
    with initialize(version_base=None, config_path=str(Path("../../config"))):
        hydra_config = compose(config_name="config", overrides=overrides)
        return hydra_config


@click.command()  # type: ignore
@click.argument("input_dataset_file", type=click.Path(readable=True))  # type: ignore
@click.argument("output_dataset_file", type=click.Path(writable=True))  # type: ignore
@click.option("--size", type=click.Choice(["small", "normal"]), default="normal")  # type: ignore
def cli(input_dataset_file: str, output_dataset_file: str, size: str) -> None:
    """Run dataset preparing.

    :param input_dataset_file: in dataset filepath
    :param output_dataset_file: out dataset filepath
    :param size: size of out feature set
    :return: nothing
    """
    df = pd.read_csv(input_dataset_file)
    cfg = compose_config(overrides=[f"dataset='{size}'"])
    df["target"] = df[cfg.dataset.target]
    new_df = df[cfg.dataset.columns + ["target"]]
    new_df.to_csv(output_dataset_file, index=False)


if __name__ == "__main__":
    cli()
