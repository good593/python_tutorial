import logging
import pandas as pd 

def do_cleaning(df_train:pd.DataFrame, df_test:pd.DataFrame
                , drop_cols:list = ['name', 'ticket', 'cabin']):
    logging.info("##################################")
    logging.info("Start do_cleaning")
    # 1. row 기준으로 중복된 데이터 제거 
    df_train.drop_duplicates(inplace=True)
    df_test.drop_duplicates(inplace=True)

    # 2. 필요없는 컬럼 제거 
    df_train.drop(drop_cols, axis=1, inplace=True)
    df_test.drop(drop_cols, axis=1, inplace=True)

    # 3. 결측치에 적용할 데이터 추출 from train 
    # 결측치에 추출한 데이터 적용 
    age_median = df_train['age'].median()
    df_train['age'].fillna(age_median, inplace=True)
    df_test['age'].fillna(age_median, inplace=True)

    fare_median = df_train['fare'].median()
    df_train['fare'].fillna(fare_median, inplace=True)
    df_test['fare'].fillna(fare_median, inplace=True)

    embarked_mode = df_train['embarked'].mode().values[0]
    df_train['embarked'].fillna(embarked_mode, inplace=True)
    df_test['embarked'].fillna(embarked_mode, inplace=True)

    assert df_train.isnull().sum().sum() == 0, '학습용 데이터에 결측치가 있습니다.'
    assert df_test.isnull().sum().sum() == 0, '평가용 데이터에 결측치가 있습니다.'
