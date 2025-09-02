import enum
from lightgbm import LGBMClassifier

class Model_Type(enum.Enum):
    lightgbm = (enum.auto(), LGBMClassifier)


def create_model(model_name:Model_Type, hp:dict):
    # 검증코드
    if model_name not in Model_Type.__members__: # [lightgbm]
        raise Exception(f"지원하지 않는 모델입니다. >> {model_name}")
    
    # 비지니스코드
    # Model_Type[model_name].value[1]
    # -> LGBMClassifier
    # -> LGBMClassifier(**hp)
    model = Model_Type[model_name].value[1](**hp, verbose=-1)

    # 리턴 
    return model 


