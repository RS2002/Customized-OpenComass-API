from opencompass.models import MyModelAPI

api_meta_template = dict(round=[
    dict(role='HUMAN', api_role='HUMAN'),
    dict(role='BOT', api_role='BOT', generate=True),
], )

models = [
    dict(
        abbr='XXX',
        type=MyModelAPI,
        path='XXX',
        key="XXX",
        meta_template=api_meta_template,
        query_per_second=1,
        max_out_len=16384,
        max_seq_len=16384,
        batch_size=16),
]
