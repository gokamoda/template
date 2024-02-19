import shutil
import hydra
from pathlib import Path
from omegaconf import DictConfig, OmegaConf

from modules import init_logging

LOG_PATH = "latest.log"
logger = init_logging(__name__, log_path=LOG_PATH)

@hydra.main(version_base="1.2", config_path="../config", config_name="main")
def main(cfg: DictConfig) -> None:
    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write("")
    logger.info(OmegaConf.to_yaml(cfg))

    hydra_cfg = hydra.core.hydra_config.HydraConfig.get()
    output_dir_str = hydra_cfg.runtime.output_dir
    output_dir = Path(output_dir_str)
    logger.info(output_dir)

    shutil.copy(LOG_PATH, f"{output_dir}/main.log")
    logger.info(f"log file copied to logs/{output_dir}/main.log")



if __name__ == "__main__":
    main()