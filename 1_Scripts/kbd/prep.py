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
    
    count = 0

    new_lemmas = []
    table = {}
    with open(out_train_file, "w") as outp:
        for in_file in augment_files:
            with open(in_file, "r") as fp:
                for line in fp.readlines():
                    lemma, form, tags = line.strip().split("\t")
                    addition = form.removeprefix(lemma)
                    new_lemmas.append(lemma)
                    table[tags] = addition
                    outp.write(f"{lemma}\t{form}\t{tags}\n")
                    count += 1

    l = len(new_lemmas)
    print(f"    {l} New lemmas!!")
    t = len(table.keys())
    print(f"    {t} New Tags!!")

    i = 0
    with open(out_train_file, "w") as outp:

        
        with open(in_train_file, "r") as fp1: # Copy The Original First!
            for line in fp1.readlines():
                lemma, form, tags = line.strip().split("\t")
                outp.write(f"{lemma}\t{form}\t{tags}\n")
                count += 1

        for tag, addition in table.items():
            for lem in new_lemmas:
                outp.write(f"{lem}\t{lem+addition}\t{tag}\n")
                i += 1
                count += 1

    assert i == l*t, "Multiplication Error?!!"
    print(f"    {l * t} Total Augment Entries!!")

    print(f"    Total Entries: {count}")
    print()

def cross_pollinate(in_train_file, augment_files, out_train_file):
    # Lemmas from new files
    # Tags from old and new files
    a = 0
    count = 0

    print("CROSS POLLINATION!!")

    new_lemmas = []
    table = {}
    with open(out_train_file, "w") as outp:
        for in_file in augment_files:
            with open(in_file, "r") as fp:
                for line in fp.readlines():
                    lemma, form, tags = line.strip().split("\t")
                    addition = form.removeprefix(lemma)
                    new_lemmas.append(lemma)
                    table[tags] = addition
                    outp.write(f"{lemma}\t{form}\t{tags}\n")
                    count += 1

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
    with open(out_train_file, "w") as outp:



        with open(in_train_file, "r") as fp1: # Copy The Original First!
            for line in fp1.readlines():
                lemma, form, tags = line.strip().split("\t")
                outp.write(f"{lemma}\t{form}\t{tags}\n")
                count += 1

        for tag, addition in table.items():
            for lem in new_lemmas:
                outp.write(f"{lem}\t{lem+addition}\t{tag}\n")
                i += 1
                count += 1

    assert i == l*t, "Multiplication Error?!!"
    print(f"    {l * t} Total Augment Entries!!")
    
    print(f"    Total Entries: {count}")
    print()

def main():
    in_train_file = "../../dataset/kbd.train.tsv"
    augment_files = ["../../3_Augment_Data/kabardian-dev.tsv", \
                     "../../3_Augment_Data/kabardian-train-low.tsv"]


    simple_addition(in_train_file, augment_files, out_train_file="../../dataset/kbd.train_2_simple_addition.tsv")
    self_pollinate(in_train_file, augment_files, out_train_file="../../dataset/kbd.train_3_self_pollinate.tsv")
    cross_pollinate(in_train_file, augment_files, out_train_file="../../dataset/kbd.train_4_cross_pollinate.tsv")


if __name__ == "__main__":
    main()


# Simple addition works!! (just append dev and train-low files!! Higher quality - 88.66 - Only 200 more entries)
# So this (Self-pollination) doesn't work! (Drives the acc down to 6.6!! Close to the neural baseline!! Maybe because only 17 and 15 new tags for almost 3200 new entries!!)
# Cross-Pollination (Does even Worse!! Drives it down to 43.66 - 4800 more entries (24 tags x 200 lemmas))

# Results
    # Baseline: 88.33%
    # Simple Addition: 88.67% [Best!!]
    # Self-Pollination: 67.7% 
    # Cross-Pollination: 43.67% 