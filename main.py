import warnings
warnings.filterwarnings('ignore')
import logging
logging.basicConfig(level=logging.INFO)

import argparse

###############################
# 코드 정의 영역 
###############################
from service.data_setup import do_load_dataset
from service.preprocessing.data_preprocessing import do_preprocessing

def main(args):
    # 데이터 로드 
    df_train, df_test, df_train_target = do_load_dataset(
        train_path=args.path_train, test_path=args.path_test, 
        target_name=args.target_name)
    
    # 데이터 전처리 
    df_train, df_test = do_preprocessing(df_train=df_train,
                        df_test=df_test,
                        drop_cols=args.drop_cols,
                        transform_cols=args.transform_cols,
                        encoding_cols=args.encoding_cols)
    
    


if __name__ == "__main__":
    ###############################
    # 코드 실행 영역 
    ###############################
    args = argparse.ArgumentParser()
    args.add_argument("--path_train", default="./data/train.csv", type=str)
    args.add_argument("--path_test", default="./data/test.csv", type=str)
    args.add_argument("--path_submission", default="./data/submission.csv", type=str)
    args.add_argument("--target_name", default="survived", type=str)
    # EDA 분석 결과 
    args.add_argument("--drop_cols", default=['passengerid', 'name', 'ticket'], type=list)
    args.add_argument("--transform_cols", default=['age', 'fare'], type=list)
    args.add_argument("--encoding_cols", default=['pclass', 'gender', 'cabin', 'embarked'], type=list)

    main(args.parse_args()) 

