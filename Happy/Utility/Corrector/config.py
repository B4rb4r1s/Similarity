import re
import os
import logging

MAX_INPUT = 256


SUMMARY_TABLE = 'elibrary_dataset_summary'
SUMMARY_MODELS_DIRECTORY = './DocumentAnalysisSystem/Models/Summary/'
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--FRED-T5-large-spell',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--RuM2M100-1.2B',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-fredt5-distilled-95m',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-fredt5-large',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-m2m100-1.2B'
SUMMARY_MODELS = [f'{SUMMARY_MODELS_DIRECTORY}{model_dir}' for model_dir in os.listdir(SUMMARY_MODELS_DIRECTORY)]


SPELL_CORRECTION_TABLE = 'elibrary_dataset_spell'
SPELL_MODELS_DIRECTORY = './DocumentAnalysisSystem/Models/SpellCheck/'
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--FRED-T5-large-spell',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--RuM2M100-1.2B',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-fredt5-distilled-95m',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-fredt5-large',
# './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-m2m100-1.2B'
# SPELL_CORRECTION_MODELS = [f'{SPELL_MODELS_DIRECTORY}{model_dir}' for model_dir in os.listdir(SPELL_MODELS_DIRECTORY)]
SPELL_CORRECTION_MODELS = [
    './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--FRED-T5-large-spell',
    './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--RuM2M100-1.2B',
    './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-fredt5-distilled-95m',
    './DocumentAnalysisSystem/Models/SpellCheck/ai-forever--sage-m2m100-1.2B',
    './DocumentAnalysisSystem/Models/SpellCheck/UrukHan--t5-russian-spell'
    ]

WHITESPACE_HANDLER = lambda k: re.sub(r' {2,}', ' ', re.sub('\n+', '\n', re.sub(r'(?<!\n)\n(?!\n)', '', re.sub('-\n', '', k.strip()))))
PROCESSING_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
