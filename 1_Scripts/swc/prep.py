import pandas as pd
import sys

def simple_addition(in_train_file, augment_files, out_train_file):

    print("SIMPLE ADDITION!!")
    # Simply concatenate files!
    count = 0

    with open(out_train_file, "w") as outp:

        with open(in_train_file, "r") as fp1: # Copy The Original First!
            for line in fp1.readlines():
                lemma, form, tags = line.strip().split("\t")
                outp.write(f"{lemma}\t{form}\t{tags}\n")
                count += 1

        original = count
        print(f"    Original Entries: {original}")

        for in_file in augment_files:
            with open(in_file, "r") as fp:
                for line in fp.readlines():
                    lemma, form, tags = line.strip().split("\t")
                    outp.write(f"{lemma}\t{form}\t{tags}\n")
                    count += 1

    print(f"    Total Entries: {count}")
    print()

def self_pollinate(in_train_file, augment_files, out_train_file):
    # Both Lemmas and Tags from new files!
    a = 0

    print("SELF POLLINATION!!")
    

    new_lemmas = []
    table = {}
    for in_file in augment_files:
        with open(in_file, "r") as fp:
            for line in fp.readlines():
                lemma, form, tags = line.strip().split("\t")
                addition = form.removeprefix(lemma)
                new_lemmas.append(lemma)
                table[tags] = addition
                # outp.write(f"{lemma}\t{form}\t{tags}\n")
    l = len(new_lemmas)
    print(f"    {l} New lemmas!!")
    t = len(table.keys())
    print(f"    {t} New Tags!!")

    i = 0
    count = 0
    with open(out_train_file, "w") as outp:

        
        with open(in_train_file, "r") as fp1: # Copy The Original First!
            for line in fp1.readlines():
                lemma, form, tags = line.strip().split("\t")
                outp.write(f"{lemma}\t{form}\t{tags}\n")
                count += 1
            
        original = count

        for tag, addition in table.items():
            for lem in new_lemmas:
                outp.write(f"{lem}\t{lem+addition}\t{tag}\n")
                i += 1
                count += 1
                if count > 10 * original:
                    break

    # assert i == l*t, "Multiplication Error?!!"
    print(f"    {l * t} Total Augment Entries!!")

    print(f"    Total Entries: {count}")
    print()

def cross_pollinate(in_train_file, augment_files, out_train_file):
    # Lemmas from new files
    # Tags from old and new files
    a = 0

    print("CROSS POLLINATION!!")

    new_lemmas = []
    table = {}
    for in_file in augment_files:
        with open(in_file, "r") as fp:
            for line in fp.readlines():
                lemma, form, tags = line.strip().split("\t")
                addition = form.removeprefix(lemma)
                new_lemmas.append(lemma)
                table[tags] = addition
                # outp.write(f"{lemma}\t{form}\t{tags}\n")

    with open(in_train_file, "r") as tp:
        for line in tp.readlines():
            lemma, form, tags = line.strip().split("\t")
            addition = form.removeprefix(lemma)
                    # print(f"{lemma} + {addition} = {form}")
            table[tags] = addition
    
    l = len(new_lemmas)
    print(f"    {l} New lemmas!!")
    t = len(table.keys())
    print(f"    {t} New Tags!!")

    i = 0
    count = 0
    with open(out_train_file, "w") as outp:



        with open(in_train_file, "r") as fp1: # Copy The Original First!
            for line in fp1.readlines():
                lemma, form, tags = line.strip().split("\t")
                outp.write(f"{lemma}\t{form}\t{tags}\n")
                count += 1

        original = count
        # print(original)
        for tag, addition in table.items():
            for lem in new_lemmas:
                outp.write(f"{lem}\t{lem+addition}\t{tag}\n")
                i += 1
                count += 1
                if count > 10 * original:

                    break

    # assert i == l*t, "Multiplication Error?!!"
    print(f"    {l * t} Total Augment Entries!!")
    
    print(f"    Total Entries: {count}")
    print()


def main():
    in_train_file = "../../dataset/swc.train.tsv"
    augment_files = ["../../3_Augment_Data/swahili-dev.txt",\
                    "../../3_Augment_Data/swahili-test.txt",\
                    "../../3_Augment_Data/swahili-train-high.txt",\
                    "../../3_Augment_Data/swahili-train-low.txt"]


    simple_addition(in_train_file, augment_files, out_train_file="../../dataset/swc.train_2_simple_addition.tsv")
    self_pollinate(in_train_file, augment_files, out_train_file="../../dataset/swc.train_3_self_pollinate.tsv")
    cross_pollinate(in_train_file, augment_files, out_train_file="../../dataset/swc.train_4_cross_pollinate.tsv")


if __name__ == "__main__":
    main()
    # print("DONE!")


# Results
    # Baseline: 71.51%
    # Simple Addition: 95.89%
    # Self-Pollination: 73.5% [Had to cut-off]
    # Cross-Pollination: 73.5% [Had to cut-off]