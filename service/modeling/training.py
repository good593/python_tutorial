
from .model import create_model
from .cross_validation import create_cv, do_training_with_cv
from .metrics import Metrics_Type

def do_training(df_train, df_train_target, args) -> bool:
    result = False 
    model = create_model(model_name=args.model_name, hp=args.hp) 
    score_by_cv = do_training_with_cv(
        model, create_cv(), df_train, df_train_target, 
        Metrics_Type.roc_auc_score)

    if score_by_cv >= 0.8:
        result = True 
    
    return result 


