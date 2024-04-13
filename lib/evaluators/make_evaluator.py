import imp
import importlib.util
import os
from lib.datasets.dataset_catalog import DatasetCatalog


def _evaluator_factory(cfg):
    module = cfg.evaluator_module
    path = cfg.evaluator_path
    print("module", module )
    print("path", path )
    evaluator = imp.load_source(module, path).Evaluator()
    print("evaluator", evaluator)
    return evaluator


def make_evaluator(cfg):
    if cfg.skip_eval:
        return None
    else:
        return _evaluator_factory(cfg)
