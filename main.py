from classification import *
import os

import pandas as pd

if __name__ == "__main__":
    # df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\Data\\Ecoli_urine_G_avg_1100.csv")
    # df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\Data\\old\\Ecoli-Ecoli.csv")
    # df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\Data\\old\\Ecoli-Ecoli.csv")
    # df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\LargeDataset\\ecoli_raman.csv")
    # df = pd.read_csv("/Users/harelhe/Desktop/GitRepo/SCE-BS1/raman/texo_raman.csv")

    df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\LargeDataset\\Ecoli_urine_G_groups_1800.csv")
    # df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\LargeDataset\\blood_bac_vir.csv")
    # df = df.replace(["R", "I", "S"], [1, 1, 0])
    df = df.replace(['Neg', 'NEg', 'POs', 'Pos', 'R', 'I', 'S'], [0, 0, 1, 1, 1, 1, 0])
    # df = df[df['analysis'].isin(['Bacterial', 'Viral'])]
    # df = df.replace(['Bacterial', 'Viral'], [0, 1])
    # df = df.replace(['Neg', 'NEg', 'POs', 'Pos', 'R', 'I', 'S', 's', 'r', 'ecoli', 'kleb'],
    #                 [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1])
    # df['index'] = df['serial']
    # df = df.groupby(['index']).mean()
    # df['serial'] = df.index
    # df = df.reset_index()
    # df['index'] = range(df.index.shape[0])
    # # df = pd.read_csv("C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\Data\\KlbPn_urine_G.csv")
    # Classification.GLOBAL_MODEL_SETTING = ("random_state", 0)
    # # ClassificationPreprocessing.SAVE = False
    # Classification.BOOTSTRAP = False
    # ClassificationPreprocessing.ADD_TO_REPORT = ""
    # Classification.grid_search_k_folds(multi_proses=4)
    # Classification.limit_cores(1)
    number_of_features = 110
    # os.chdir(f"C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\EcoliDNN\\Results\\loo_svm_cipro_1100_urine_George\\")
    #     # os.chdir(f"C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\EcoliDNN\\Results\\10kfold_cipro_1400_urine_George\\")
    # os.chdir(f"C:\\Users\\harelhe\\Desktop\\GitRepo\\SCE-BS1\\CLB_CNN\\Results\\2_anti_loo_RF_urine_George\\")
    # path = "/Users/harelhe/Desktop/GitRepo/SCE-BS1/EcoliDNN/Results/xgb_10kfold_cipro_1400_urine_George/"
    # path = "/Users/harelhe/Desktop/GitRepo/SCE-BS1/bar_vir/results/"
    path = "/Users/harelhe/Desktop/GitRepo/SCE-BS1/EcoliDNN/Results/ESBL/RF_1800_urine_George_10fold_pca_avg/"
    # path = "/Users/harelhe/Desktop/GitRepo/SCE-BS1/raman/texo/"
    try:
        os.mkdir(path)
    except OSError:
        print("Creation of the directory %s failed" % path)
    else:
        print("Successfully created the directory %s " % path)


    # antibiotics = ['texonomy'#'seftazidime'
    #     # 'amoxicillin_clavul_A',
    #     # 'ampicillin',
    #     # 'ceftazidime',
    #     # 'cefuroxime_axetil',
    #     # 'ceftriaxone',
    #     # 'cefuroxime',
    #     # 'cephalexin',
    #     # 'ciprofloxacin',
    #     # 'ESBL test'
    #     # 'sulfamethoxa_trimeth'
    # ]
    antibiotics = [#'ESBL test',    'amikacin',
                   # 'amoxicillin_clavul_A',    'ampicillin',
                   #  'ceftazidime',
                   #  'ceftriaxone',
                   #  'cefuroxime',    'cefuroxime_axetil',    'cephalexin',
                   #  'ciprofloxacin',
                   # # 'ertapenem',
                   # # 'fosfomycin',
                   #  'gentamicin',
                    'ESBL test',
                   #  # 'meropenem',
                   #  'nitrofurantion',    'piperacill_tazobactam',    'sulfamethoxa_trimeth'
                   ]
    # antibiotics = ['analysis']
    # antibutics = ["amoxicillin_clavul_A"]
    # fethers = df.loc[:, "1801.264":"898.703"]
    # fethers = df.loc[:, "898.7034445":"1801.263898"]

    df_orig = df.copy()
    for i_anti in antibiotics:
        print(i_anti)
        df = df_orig.copy()
        # dfTmp = df[i_anti].replace(['Neg', 'NEg', 'POs', 'Pos', 'R', 'I', 'S'], [0, 0, 1, 1, 1, 1, 0]).values
        # df[i_anti] = dfTmp
        df = df[df[i_anti].notna()]
        # df = df.reset_index()
        # df = df.drop('level_0', axis=1)
        # group_str = 'index'
        # wl_start = "1801.263898"
        # wl_end = "898.7034445"
        # rawX = df.loc[:, wl_start:wl_end]
        # rawX_der = sgf(rawX, window_length=13, polyorder=3, deriv=2, mode="nearest")
        # rawY = df[i_anti].values
        # groups = df[group_str].values
        # group_indx = np.array(groups_to_index(groups))

        # pooled_strat_kfold(rawX_der, rawY, path, i_anti, 10, 0, 8)
        pooled_strat_pca_nested_kfold_groups(df.copy(), path, i_anti, 10, 0, 10, 0)

        # fethers_tamp = pd.concat([features, df.loc[:, i_anti]], axis=1)
        # fethers_tamp = fethers_tamp.dropna()
        # target = fethers_tamp.pop(i_anti)
        # target = target.replace(["R", "I", "S"], [1, 1, 0])
        # model = Classification(fethers_tamp, target, "random")
        # model = Classification(fethers_tamp, target, "xgboost")
        # model = Classification(fethers_tamp, target, "svm")
        # model.sacrifice_rate_setter(0.15)
        # model.preprocessing(["sgf"])
        # model.feature_selection(number_of_features=number_of_features)
        # C = 250, kernel = 'rbf', gamma = 0.0001, probability = True
        # model.model_modifying(("C", 250), ('kernel', 'rbf'),
        #                       ("gamma", [0.000001, 0.000005, 0.00001, 0.00004, 0.0001, 0.0005, 0.001, 0.1, 1]), ('probability', True))
        # model.model_modifying(("objective", 'binary:logistic'),('colsample_bytree', 0.5),
        #                       ("gamma", 0.1), ('learning_rate', 0.1), ('max_depth', 7), ('reg_lambda', 0), ('scale_pos_weight', 1))
        # model.model_modifying(('criterion', ['gini']), ("min_samples_split", 2),
        #                       ("oob_score", True), ('n_estimators', [500]), ('max_depth', [10]))
        # # model.K_folds_stratified(number_of_folds=10)
        # # model.K_folds(number_of_folds=10)
        #
        # model.leave_one_out()
        # model.save_classification_report(antibutic)
        # model.show_roc(antibutic)
        # model.save_classification_probability(antibutic)
