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

from enum import Enum
from utils import get_metric_names


class SeverityType(Enum):
    CRITICAL = "critical"
    WARNING = "warning"
    INFORMATIONAL = "info"
    CRITICAL_ACKNOWLEDGED = "critical_acknowledged"
    WARNING_ACKNOWLEDGED = "warning_acknowledged"
    INFORMATIONAL_ACKNOWLEDGED = "info_acknowledged"


class ComponentType(Enum):
    VOLUMES = "volumes"
    POOLS = "pools"
    ENCLOSURES = "enclosures"
    DRIVES = "drives"
    FC_PORTS = "fc-ports"
    IP_PORTS = "ip-ports"
    HOST_CONNECTIONS = "host-connections"
    IO_GROUPS = "io-groups"
    MANAGED_DISKS = "managed-disks"
    VOLUME_MAPPINGS = "volume-mappings"


DURATION = "12h"

IO_RATE_METRIC_TYPES = get_metric_names("io_metrics")
DATA_RATE_METRIC_TYPES = get_metric_names("data_rate_metrics")
TRANSFER_SIZE_METRIC_TYPES = get_metric_names("transfer_size_metrics")
RESPONSE_TIME_METRIC_TYPES = get_metric_names("response_time_metrics")
CPU_UTILIZATION_METRICS = get_metric_names("cpu_utilization_metrics")
CAPACITY_METRICS = get_metric_names("capacity_metrics")
CACHE_EFFICIENCY_METRICS = get_metric_names("cache_efficiency_metrics")
DISK_LATENCY_METRICS = get_metric_names("disk_latency_metrics")
