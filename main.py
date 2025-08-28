import warnings
warnings.filterwarnings('ignore')

import logging
logging.basicConfig(level=logging.INFO)

from common.dataset import load_dataset
from common.preprocessing.eda import do_eda
from common.preprocessing.cleaning import do_cleaning
from common.preprocessing.encoding import do_encoding

def modeling():
    logging.info("##################################")
    logging.info("Start Load Dataset")
    # 1. train dataset, test dataset 
    df_train = load_dataset("./data/train.csv")
    df_test = load_dataset("./data/test.csv")
    # 2. eda
    do_eda(df_train=df_train)
    # 3. cleaning
    do_cleaning(df_train, df_test)

    # 4. encoding
    enc_cols = ['gender', 'embarked']
    tr_enc, te_enc = do_encoding(df_train[enc_cols], df_test[enc_cols])

    # 5. create model

    # 6. prediction

    # 7. submission


if __name__ == "__main__":
    modeling()

