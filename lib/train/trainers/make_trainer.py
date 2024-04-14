from .trainer import Trainer
import imp


def _wrapper_factory(cfg, network, train_loader=None):
    temp = iter(train_loader)
    temp_batch = next(temp)
    print("check dataloader point 3")
    module = cfg.loss_module
    path = cfg.loss_path
    network_wrapper = imp.load_source(module, path).NetworkWrapper(network, train_loader)
    return network_wrapper


def make_trainer(cfg, network, train_loader=None):
    network = _wrapper_factory(cfg, network, train_loader)
    return Trainer(network)
