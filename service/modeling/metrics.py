import enum 
from sklearn.metrics import roc_auc_score, f1_score

class Metrics_Type(enum.Enum):
    roc_auc_score = (enum.auto(), roc_auc_score)
    f1_score = (enum.auto(), f1_score)

