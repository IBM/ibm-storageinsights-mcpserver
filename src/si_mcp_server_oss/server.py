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

from typing import Optional, List

from mcp import types
from mcp.server.fastmcp import FastMCP

from logger import setup_logger
from constants import (
    IO_RATE_METRIC_TYPES,
    DATA_RATE_METRIC_TYPES,
    TRANSFER_SIZE_METRIC_TYPES,
    RESPONSE_TIME_METRIC_TYPES,
    CPU_UTILIZATION_METRICS,
    CAPACITY_METRICS,
    DURATION,
    SeverityType,
    ComponentType,
)
from utils import (
    resolve_tenant_id,
    call_ibm_storageinsights_api,
)
from settings import (
    SI_BASE_URL,
    SI_TENANT_ID,
)

# Set up Configured logger
logger = setup_logger("si-mcp-logger")

# Instantiate the server from FastMCP
server = FastMCP("si-mcp-server")
logger.info("Started mcp server")


@server.tool()
async def fetch_tenant_alerts(
    tenant_id_input: Optional[str] = SI_TENANT_ID,
    duration: Optional[str] = DURATION,
    severity: Optional[List[SeverityType]] = None,
) -> types.CallToolResult:
    """
    Get alerts for tenant.

    Args:
        tenant_id_input: Storage Insights Tenant id
        duration: Alerts requested for a particular duration (e.g., "20m", "5h", "1d").
        severity: Alerts requested for a list of severities to filter by (The severity types are : critical, warning, info, critical_acknowledged, warning_acknowledged, info_acknowledged).
    """
    try:
        logger.debug("Tool invoked: fetch_tenant_alerts")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {}
        if duration:
            params["duration"] = duration
        if severity:
            params["severity"] = [s.value for s in severity]
        rest_url = f"{SI_BASE_URL}/tenants/{tenant_id}/alerts"
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_tenant_alerts. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_tenant_notifications(
    tenant_id_input: Optional[str] = SI_TENANT_ID,
    duration: Optional[str] = DURATION,
    severity: Optional[SeverityType] = None,
) -> types.CallToolResult:
    """
    Get notification for tenant.

    Args:
         tenant_id_input: Storage Insights Tenant id
         duration: Notifications requested for a particular duration (e.g., "5h", "1d").
         severity: Notifications requested for a particular severity (The severity types are : critical, warning, info, critical_acknowledged, warning_acknowledged, info_acknowledged).
    """
    try:
        logger.debug("Tool invoked: fetch_tenant_notifications")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {}
        if duration:
            params["duration"] = duration
        if severity:
            params["severity"] = severity.value
        rest_url = f"{SI_BASE_URL}/tenants/{tenant_id}/notifications"
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_tenant_notifications. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_storage_systems(
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get all storage systems for tenant.

    Args:
        tenant_id_input: Storage Insights Tenant id
    """
    try:
        logger.debug("Tool invoked: fetch_storage_systems")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        rest_url = f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems"
        result = await call_ibm_storageinsights_api(
            url=rest_url, logger=logger, tenant_id=tenant_id, api_key=api_key
        )
        logger.debug(
            f"Received data for tool call: fetch_storage_systems. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_notifications(
    system_id: str,
    duration: Optional[str] = DURATION,
    severity: Optional[SeverityType] = None,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get notifications of system under the tenant.

    Args:
         tenant_id_input: Storage Insights Tenant id
         system_id: Storage System id
         duration: Notifications requested for a particular duration (e.g., "5h", "1d").
         severity: Notifications requested for a particular severity (The severity types are : critical, warning, info, critical_acknowledged, warning_acknowledged, info_acknowledged).
    """
    try:
        logger.debug("Tool invoked: fetch_system_notifications")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {}
        if duration:
            params["duration"] = duration
        if severity:
            params["severity"] = severity.value
        rest_url = f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/notifications"
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_notifications. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_details(
    system_id: str, tenant_id_input: Optional[str] = SI_TENANT_ID
) -> types.CallToolResult:
    """
    Get storage system details for given system under a tenant.

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
    """
    try:
        logger.debug("Tool invoked: fetch_system_details")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        rest_url = f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}"
        result = await call_ibm_storageinsights_api(
            url=rest_url, logger=logger, tenant_id=tenant_id, api_key=api_key
        )
        logger.debug(
            f"Received data for tool call: fetch_system_details. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_io_rate(
    system_id: str,
    metric_types: Optional[List[str]] = IO_RATE_METRIC_TYPES,
    duration: Optional[str] = DURATION,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get io rate for a system present on the tenant

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        metric_types : performance metric type
        duration : duration for the data fetch (ex. 20m, 1h, 1d)
    """
    try:
        logger.debug("Tool invoked: fetch_system_io_rate")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {
            "types": metric_types,
            "duration": duration,
        }
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/metrics"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_io_rate. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_data_rate(
    system_id: str,
    metric_types: Optional[List[str]] = DATA_RATE_METRIC_TYPES,
    duration: Optional[str] = DURATION,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get data rate for a system present on the tenant

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        metric_types : performance metric type
        duration : duration for the data fetch (ex. 20m, 1h, 1d)
    """
    try:
        logger.debug("Tool invoked: fetch_system_data_rate")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {
            "types": metric_types,
            "duration": duration,
        }
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/metrics"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_data_rate. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_response_time(
    system_id: str,
    metric_types: Optional[List[str]] = RESPONSE_TIME_METRIC_TYPES,
    duration: Optional[str] = DURATION,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get response time for a system present on the tenant

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        metric_types : performance metric type
        duration : duration for the data fetch (ex. 20m, 1h, 1d)
    """
    try:
        logger.debug("Tool invoked: fetch_system_response_time")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {
            "types": metric_types,
            "duration": duration,
        }
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/metrics"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_response_time. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_transfer_size(
    system_id: str,
    metric_types: Optional[List[str]] = TRANSFER_SIZE_METRIC_TYPES,
    duration: Optional[str] = DURATION,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get transfer size for a system present on the tenant

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        metric_types : performance metric type
        duration : duration for the data fetch (ex. 20m, 1h, 1d)
    """
    try:
        logger.debug("Tool invoked: fetch_system_transfer_size")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {
            "types": metric_types,
            "duration": duration,
        }
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/metrics"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_transfer_size. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_cpu_utilization(
    system_id: str,
    metric_types: Optional[List[str]] = CPU_UTILIZATION_METRICS,
    duration: Optional[str] = DURATION,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get cpu utilization metrics for a system present on the tenant

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        metric_types : performance metric type
        duration : duration for the data fetch (ex. 20m, 1h, 1d)
    """
    try:
        logger.debug("Tool invoked: fetch_system_cpu_utilization")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {
            "types": metric_types,
            "duration": duration,
        }
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/metrics"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_cpu_utilization. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_capacity(
    system_id: str,
    metric_types: Optional[List[str]] = CAPACITY_METRICS,
    duration: Optional[str] = DURATION,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get capacity metrics for a system present on the tenant

    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        metric_types : performance metric type
        duration : duration for the data fetch (ex. 20m, 1h, 1d)
    """
    try:
        logger.debug("Tool invoked: fetch_system_capacity")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {
            "types": metric_types,
            "duration": duration,
        }
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/metrics"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_capacity. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_components(
    system_id: str,
    comp_type: ComponentType,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get storage systems components (volumes, pools, enclosures, drives, fc-ports, ip-ports, host-connections, io-groups, managed-disks) for system under tenant.
    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
        comp_type: component_type and could contain only one of the following values - volumes, pools, enclosures, drives, fc-ports, ip-ports, host-connections, io-groups, managed-disks
    """
    try:
        logger.debug("Tool invoked: fetch_system_components")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        rest_url = f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/{comp_type.value}"
        result = await call_ibm_storageinsights_api(
            url=rest_url, logger=logger, tenant_id=tenant_id, api_key=api_key
        )
        logger.debug(
            f"Received data for tool call: fetch_system_components. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.tool()
async def fetch_system_alerts(
    system_id: str,
    duration: Optional[str] = DURATION,
    severity: Optional[List[SeverityType]] = None,
    tenant_id_input: Optional[str] = SI_TENANT_ID,
) -> types.CallToolResult:
    """
    Get alerts for system under tenant.
    Args:
        tenant_id_input: Storage Insights Tenant id
        system_id: Storage System id
    """
    try:
        logger.debug("Tool invoked: fetch_system_alerts")
        tenant_id, api_key = resolve_tenant_id(tenant_id=tenant_id_input, logger=logger)
        params = {}
        if duration:
            params["duration"] = duration
        if severity:
            params["severity"] = [s.value for s in severity]
        rest_url = (
            f"{SI_BASE_URL}/tenants/{tenant_id}/storage-systems/{system_id}/alerts"
        )
        result = await call_ibm_storageinsights_api(
            url=rest_url,
            logger=logger,
            params=params,
            tenant_id=tenant_id,
            api_key=api_key,
        )
        logger.debug(
            f"Received data for tool call: fetch_system_alerts. Returning result to MCP Client: {result}"
        )
        return types.CallToolResult(
            content=[
                types.TextContent(type="text", text=f"Operation successful: {result}")
            ]
        )
    except Exception as error:
        return types.CallToolResult(
            isError=True,
            content=[types.TextContent(type="text", text=f"Error: {str(error)}")],
        )


@server.prompt()
async def morning_cup_of_coffee() -> types.Prompt:
    """
    Run 3 tools and combine the output of the 3 tool calls to generate morning cup of coffee
    """
    return types.Prompt(
        name="morning-cup-coffee",
        description="Fetch storage system details, alert details and notification details in sequence with the same input. Filter the result to show only systems in error status, critical alerts and notifications.Show the results in proper markdown tables",
        arguments=[
            types.PromptArgument(
                name="tenant_id",
                description="Tenant ID to be passed to all tools",
                required=True,
            )
        ],
    )


if __name__ == "__main__":
    server.run(transport="stdio")
