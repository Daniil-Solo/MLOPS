configfile: "./workflows/config.yaml"

rule feature_engineering:
    input: "student-mat.csv"
    output: "student-mat-prepared.csv"
    threads: config["data_operations_n_threads"]
    shell: "python ./workflows/scripts/feature_engineering.py {input[0]} {output[0]}"

rule select_features_from_dataset:
    input: "student-mat-prepared.csv"
    output: "student-mat-{dataset_size}.csv"
    threads: config["data_operations_n_threads"]
    shell: "python ./workflows/scripts/select_features_from_dataset.py {input[0]} {output[0]} --size {wildcards.dataset_size}"

rule download_kaggle_dataset:
    output: "student-mat.csv"
    threads: config["data_operations_n_threads"]
    shell: "kaggle datasets download uciml/student-alcohol-consumption -f student-mat.csv"