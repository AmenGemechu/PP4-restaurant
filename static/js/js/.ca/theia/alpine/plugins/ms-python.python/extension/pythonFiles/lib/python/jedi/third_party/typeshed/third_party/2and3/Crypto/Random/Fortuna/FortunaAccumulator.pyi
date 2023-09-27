from typing import Any

__revision__: str

class FortunaPool:
    digest_size: Any
    def __init__(self) -> None: ...
    def append(self, data): ...
    def digest(self): ...
    def hexdigest(self): ...
    length: int
    def reset(self): ...

def which_pools(r): ...

class FortunaAccumulator:
    min_pool_size: int
    reseed_interval: float
    reseed_count: int
    generator: Any
    last_reseed: Any
    pools: Any
    def __init__(self) -> None: ...
    def random_data(self, bytes): ...
    def add_random_event(self, source_number, pool_number, data): ...