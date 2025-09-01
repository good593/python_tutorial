import numpy as np
import pandas as pd

def __fillna(df_train:pd.DataFrame, df_test:pd.DataFrame):
    # df_train.isnull() -> 2차원 데이터(True/False)
    # df_train.isnull().sum() -> 1차원 데이터(컬럼별 결측치 합)
    # -> index(컬럼) / value(결측치 수)
    # df_train.isnull().sum()[df_train.isnull().sum() > 0]
    # -> 결측치가 존재하는 것만 조회 -> 1차원 데이터(index(=컬럼) / value(=결측치 수))
    train_none_cols = df_train.isnull().sum()[df_train.isnull().sum() > 0].index
    test_none_cols = df_test.isnull().sum()[df_test.isnull().sum() > 0].index
    # 전체 결측치 컬럼들
    none_cols = list(set(train_none_cols) | set(test_none_cols)) 
    for col in none_cols: # 결측치 컬럼 리스트 
        try:
            _value = df_train[col].mean() # 수치형 데이터 
        except:
            _value = df_test[col].mode()[0] # 범주형 데이터 
        finally:
            # 결측치에 통계값 넣기
            df_train[col].fillna(_value, inplace=True)
            df_test[col].fillna(_value, inplace=True)

    return df_train, df_test

def __dropcols(df_train:pd.DataFrame, df_test:pd.DataFrame, drop_cols:list):
    
    return df_train.drop(drop_cols, axis=1), df_test.drop(drop_cols, axis=1)

def __transform_cols(df_train:pd.DataFrame, df_test:pd.DataFrame, transform_cols:list):

    for col in transform_cols: # age, fare
        df_train[col] = df_train[col].map(lambda x: np.log1p(x))
        df_test[col] = df_test[col].map(lambda x: np.log1p(x))
    
    return df_train, df_test

def do_cleasing(df_train:pd.DataFrame, df_test:pd.DataFrame
                , drop_cols:list, transform_cols:list):
    # 1. row 중복 데이터 제거 
    df_train = df_train.drop_duplicates()

    # 2. 결측치를 치환(통계값 <- train)
    df_train, df_test = __fillna(df_train, df_test)

    # 3. 필요없는 컬럼 제거 
    df_train, df_test = __dropcols(df_train, df_test, drop_cols=drop_cols)

    # 4. 왜도/첨도 처리 
    df_train, df_test = __transform_cols(df_train, df_test, transform_cols=transform_cols)

    # 5. 검증 
    assert df_train.shape[1] == df_test.shape[1], "학습용(train)과 평가용(test) 컬럼수가 다름"
    return df_train, df_test
