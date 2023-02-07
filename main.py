from classification import *
import os

import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("C:\\Users\\xxxx\\Desktop\\GitRepo\\Ecoli_urine_.csv")
    df = df.replace(['Neg', 'NEg', 'POs', 'Pos', 'R', 'I', 'S'], [0, 0, 1, 1, 1, 1, 0])
    path = "/Users/xxxx/Desktop//ESBL/"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


    antibiotics = [#'ESBL test',    'amikacin',

                    'ESBL test',
                   #  # 'meropenem',
                   #  'nitrofurantion',    'piperacill_tazobactam',    'sulfamethoxa_trimeth'
                   ]


    df_orig = df.copy()
    for i_anti in antibiotics:
        print(i_anti)
        df = df_orig.copy()

        df = df[df[i_anti].notna()]


        pooled_strat_pca_nested_kfold_groups(df.copy(), path, i_anti, 10, 0, 10, 0)
