import pandas as pd

def load_dataset(path:str) -> pd.DataFrame:
    # 타이타닉 데이터셋 로드하는 코드 작성
    return pd.read_csv(path)

