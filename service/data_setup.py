import pandas as pd 

def load_dataset(path:str) -> pd.DataFrame:
    return pd.read_csv(path)

def split_features_targets(df:pd.DataFrame, target_name:str) -> tuple:
    df_targets = df[target_name]
    df_features = df.drop([target_name], axis=1)
    return df_features, df_targets

def do_load_dataset(train_path:str, test_path:str, target_name:str):
    df_train_full = load_dataset(path=train_path) 
    df_test = load_dataset(path=test_path) 

    df_train, df_train_target = split_features_targets(
        df=df_train_full, target_name=target_name)
    
    return df_train, df_test, df_train_target 
