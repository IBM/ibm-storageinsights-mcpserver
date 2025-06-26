# Copyright 2025. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
import os
from logging.handlers import RotatingFileHandler
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()


def setup_logger(name: str) -> logging.Logger:
    """
    Sets up logger to be used by every method in the application.
    Args:
        name: name of the logger (__name__)
    Returns:
        Configured logger object
    """
    logger = logging.getLogger(name)
    if logger.hasHandlers():
        return logger

    # Defaults
    default_log_level_str = "INFO"
    default_log_filename = "si_mcp_server.log"
    default_log_file_path = Path(default_log_filename)

    # Fetch log level and path from .env
    log_level_str = os.getenv("LOG_LEVEL", default_log_level_str).strip().upper()
    log_dir_raw = os.getenv("LOG_FILE_PATH", "").strip()

    # Convert to logging constant
    log_level = getattr(logging, log_level_str, logging.INFO)
    logger.setLevel(log_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s"
    )

    # Resolve log file path
    try:
        if log_dir_raw:
            log_dir = Path(log_dir_raw)
            log_dir.mkdir(parents=True, exist_ok=True)
            log_file_path = log_dir / default_log_filename
        else:
            log_file_path = default_log_file_path
    except Exception as e:
        # Falling back to default if invalid log dir
        log_file_path = default_log_file_path

    try:
        file_handler = RotatingFileHandler(
            log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5
        )
    except PermissionError as e:
        file_handler = RotatingFileHandler(
            default_log_file_path, maxBytes=10 * 1024 * 1024, backupCount=5
        )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(log_level)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(log_level)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger