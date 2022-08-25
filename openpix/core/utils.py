from dataclasses import asdict, is_dataclass


def dataclass_to_json_dict(dt):
    if not is_dataclass(dt):
        raise ValueError("dt argument must be a dataclass")

    d = asdict(dt)
    return {k: v for k, v in d.items() if v is not None}