from sklearn.model_selection import StratifiedKFold, KFold
from .metrics import Metrics_Type

def create_cv(n_splits:int=5, shuffle:bool=True):
    return StratifiedKFold(n_splits=n_splits, shuffle=shuffle)

def do_training_with_cv(model, cv, df_train, df_train_target, metrics_type) -> float:
    score = 0.0 # 초기값 
    for i, (train_index, valid_index) in enumerate(cv.split(df_train, df_train_target)):
        # 학습용 데이터 -> features, targets
        tr_features, tr_targets = df_train.iloc[train_index], df_train_target.iloc[train_index]
        # 평가용 데이터 -> features, targests
        te_features, te_targets = df_train.iloc[valid_index], df_train_target.iloc[valid_index]
        # 모델 학습
        model.fit(tr_features, tr_targets)
        # 평가
        predictions = model.predict_proba(te_features)[:, 1]
        score += metrics_type.value[1](te_targets, predictions)

    return score / cv.n_splits
