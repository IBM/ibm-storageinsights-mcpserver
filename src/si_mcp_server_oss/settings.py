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

import os
from dotenv import load_dotenv

load_dotenv()

SI_BASE_URL = os.getenv("SI_BASE_URL")
SI_TENANT_ID = os.getenv("DEFAULT_SI_TENANT_ID")
SI_API_KEY = os.getenv("DEFAULT_SI_API_KEY")
CONFIG_FILE_PATH = os.getenv("CONFIG_FILE_PATH")
