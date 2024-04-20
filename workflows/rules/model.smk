configfile: "./workflows/config.yaml"

rule train_model:
    input: "student-mat-{dataset_size}.csv"
    output: "{dataset_size}_{model}.pkl"
    threads: 1
    resources: cpu=1
    params :
        random_state = config["random_state"]
    shell: "python ./workflows/scripts/train_model.py {input[0]} {output[0]} --model {wildcards.model} --random_state {params.random_state}"