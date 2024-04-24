"""Script for training model."""

import pickle
from pathlib import Path

import click
import pandas as pd
from hydra import compose, initialize
from hydra.utils import instantiate
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
@click.argument("dataset_file", type=click.Path())  # type: ignore
@click.argument("model_file", type=click.Path(writable=True))  # type: ignore
@click.option(  # type: ignore
    "--model",
    type=click.Choice(["linear-regression", "random-forest"]),
    default="linear-regression",
)
def cli(dataset_file: str, model_file: str, model: str) -> None:
    """Run model training.

    :param dataset_file: in dataset filepath
    :param model_file: out model filepath
    :param model: type of model
    :return: nothing
    """
    df = pd.read_csv(dataset_file)
    target = df["target"].values
    data = df.drop(["target"], axis=1).values
    cfg = compose_config(overrides=[f"model='{model}'"])
    reg_model = instantiate(cfg["model"])
    if "n_jobs" in reg_model.get_params():
        reg_model.set_params(n_jobs=int(cfg["cpu_count"]) // 2)
    reg_model.fit(data, target)
    with open(model_file, "wb") as f:
        pickle.dump(reg_model, f)


if __name__ == "__main__":
    cli()
