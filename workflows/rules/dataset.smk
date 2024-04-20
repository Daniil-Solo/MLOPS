configfile: "./workflows/config.yaml"

rule prepare_dataset:
    input: "student-mat.csv"
    output: "student-mat-{dataset_size}.csv"
    threads: 1
    resources: cpu=1
    shell: "python ./workflows/scripts/prepare_dataset.py {input[0]} {output[0]} --size {wildcards.dataset_size}"

rule download_kaggle_dataset:
    output: "student-mat.csv"
    shell: "kaggle datasets download uciml/student-alcohol-consumption -f student-mat.csv"