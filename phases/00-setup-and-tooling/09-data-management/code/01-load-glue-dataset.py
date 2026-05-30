from datasets import load_dataset

dataset = load_dataset("nyu-mll/glue", "mrpc")

for i, example in enumerate(dataset["train"]):
    print(example)
    if i >= 4:
        break