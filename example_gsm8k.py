from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets.gsm8k.gsm8k_0shot_v2_gen_a58960 import \
        gsm8k_datasets
    from opencompass.configs.models.mymodel.default import \
        models as mymodel

datasets = gsm8k_datasets
models = mymodel
