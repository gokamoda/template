import shutil
from pathlib import Path

import hydra
from modules import init_logging, init_hydra_run
from omegaconf import DictConfig

LOG_PATH = "latest.log"
logger = init_logging(__name__, log_path=LOG_PATH)


@hydra.main(version_base="1.2", config_path="../config", config_name="main")
def main(cfg: DictConfig) -> None:
    """_summary_

    Parameters
    ----------
    cfg : DictConfig
        _description_
    """

    output_dir = init_hydra_run(cfg)
    # CODE HERE
    

    shutil.copy(LOG_PATH, f"{save_latest_dir}/main.log")
    shutil.copytree(save_latest_dir, output_dir.joinpath("latest"))
    logger.info("log file copied to logs/%s/latest/main.log", output_dir)


if __name__ == "__main__":
    main()
