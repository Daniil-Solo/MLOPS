configfile: "./workflows/config.yaml"
include: "./workflows/rules/model.smk"
include: "./workflows/rules/dataset.smk"

rule all:
    input:
        expand("{dataset_size}_{model}.pkl", model=config["models"], dataset_size=config["dataset_sizes"])
