import pandas as pd
from sklearn.model_selection import train_test_split

def load_dataset():
    X, y = load_full_dataset()
    return train_test_split(X, y, test_size=0.2, random_state=42)

def load_full_dataset():
    df = pd.read_csv("data/machine.data", header=None)

    df.columns = ["Vendor", "Model", "Cycle Time (ns)", "Min Mem (KB)", "Max Mem (KB)",
                  "Cache (KB)", "Min Channels", "Max Channels", "PRP", "ERP"]
    # remove column
    df = df.drop(columns=["Vendor", "Model", "ERP"])
    X = df.drop(columns=["PRP"])
    y = df["PRP"]

    return X, y

