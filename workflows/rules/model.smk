configfile: "./workflows/config.yaml"

rule train_model:
    input: "student-mat-{dataset_size}.csv"
    output: "{dataset_size}_{model}.pkl"
    threads: int(os.environ["NUMBER_OF_PROCESSORS"]) // 2
    shell: "python ./workflows/scripts/train_model.py {input[0]} {output[0]} --model {wildcards.model}"