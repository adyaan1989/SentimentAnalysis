from pathlib import Path


#DataIngestion
@dataclass(frozen=True)
class DataIngetionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
