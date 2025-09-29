import re

MODELS_PATH = './Models'

SIMILARITY_MODELS = [
    './Models/cointegrated--rubert-tiny2',
    './Models/sergeyzh--LaBSE-ru-sts',
    './Models/uaritm--multilingual_en_uk_pl_ru',
    './Models/DeepPavlov--rubert-base-cased-sentence',
]

PROCESSING_HANDLER = lambda k: re.sub(r' {2,}', ' ', re.sub('\n+', '\n', re.sub(r'(?<!\n)\n(?!\n)', ' ', re.sub('-\n', '', k.strip()))))