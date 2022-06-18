from pathlib import Path


def gen_model_conf(filename=None):
    fout = Path(filename) if filename else Path('tmp/model.yml')
    fout.write_bytes(b'model generate!')
    return True