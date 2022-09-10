import argparse


class Trainer:
    def __init__(self, text):
        self.txt = text
        self.txt2 = ""
        self.dct = dict()

    def clean(self):
        for i in self.txt:
            if i.isalpha() or i == " ":
                self.txt2 += i.lower()

    def fit(self):
        arr = self.txt2.split(" ")
        for i in range(len(arr)):
            if self.dct[arr[i]] is None:
                self.dct[arr[i]] = list()
            self.dct[arr[i]].add(arr[i+1])


parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", type=str, dest="inputf")
parser.add_argument("--model", type=str)
args = parser.parse_args()
f = open(args.inputf, "r")
tr = Trainer(f.read())
tr.fit()
