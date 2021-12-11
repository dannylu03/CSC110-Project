from dataclasses import dataclass

@dataclass
class DataLoad: 
    file: str

    def load_file(self) -> DataFrame:
        raise NotImplementedError


