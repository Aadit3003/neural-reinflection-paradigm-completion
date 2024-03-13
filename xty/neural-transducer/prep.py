filename = "../dataset/xty.test.tsv"
out_file = "../dataset/xty.PREP.tsv"
import pandas as pd
import sys

def prep_input_test_file(in_file, out_file):
    with open(out_file, "w") as outp:
        with open(in_file, "r") as fp:
            for line in fp.readlines():
                lemma, tags = line.strip().split("\t")
                placeholder = "PLACEHOLDER"
                outp.write(f"{lemma}\t{placeholder}\t{tags}\n")
    print("INPUT FILE PREPPED!")

def prep_submission_pred_file(raw_pred_file, out_file):
    df = pd.read_csv(raw_pred_file, sep='\t', header=0)
    df["prediction"] = [''.join(a.split(' ')) for a in df["prediction"]]
    df["target"] = [''.join(b.split(' ')) for b in df["target"]]
    with open(out_file, "w+") as outp:
        for prediction in df["prediction"]:
            outp.write(f"{prediction}\n")
    # print("SUBMISSION FILE WRITTEN!")




def main():
    # lang = 
    lang = "xty"
    # prep_input_test_file(in_file=f"../dataset/{lang}.test.tsv", \
    #                      out_file=f"../dataset/{lang}.PREP.tsv")

    prep_submission_pred_file(raw_pred_file = f"./checkpoints/sig22/tagtransformer/{lang}.decode.test.tsv", \
                              out_file = f"../../../2_Final_Submission/{lang}.txt")
    # print("DONE!")

if __name__ == "__main__":
    main()