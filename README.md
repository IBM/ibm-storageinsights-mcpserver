# IBM Storage Insights MCP Server

> **DISCLAIMER**: This is a community-maintained project and is not officially affiliated with, endorsed by, or supported by IBM. This MCP server utilizes the [IBM Storage Insights](https://www.ibm.com/products/storage-insights) External APIs.

This open-sourced Model Context Protocol (MCP) server will help [IBM Storage Insights](https://www.ibm.com/products/storage-insights)  to integrate in the Agentic-AI ecosystem. It will help users to bring their AI-Agents for seamless observability and diagnosis of their Storage Assets registered with [IBM Storage Insights](https://www.ibm.com/products/storage-insights) .

## 🚀 Features

- **Observability Tools**: Leverage key [IBM Storage Insights](https://www.ibm.com/products/storage-insights) monitoring capabilities via an MCP interface.
- **Extensible Design**: Easily integrate additional Storage Insights APIs for future expansions.
- **Pythonic**: Allowing ease of use and extension for AI developers

## 🛠️ Tools
Listed below are the tools which are presently exposed thought the MCP server:
### 1. `fetch_tenant_alerts`

   - **Description**: Retrieve a list of alerts for a tenant.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of alerts present for the tenant.
   - **Examples**:
     ```
     # Example 1: Fetch alerts using default tenant ID from .env
     "Get all alerts for my tenant"
     
     # Example 2: Fetch alerts for a specific tenant
     "Show me alerts for tenant ID 01f13d45-27fd-1e2d-1234-66e2fdea0987"
     
     # Example 3: Check critical alerts
     "What are the current alerts on my storage systems?"
     ```

### 2. `fetch_tenant_notifications`

   - **Description**: Retrieve a list of notifications for a tenant.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of notifications present for the tenant.
   - **Examples**:
     ```
     # Example 1: Get all notifications using default tenant
     "Show me all notifications for my tenant"
     
     # Example 2: Fetch notifications for specific tenant
     "Get notifications for tenant 01f13d45-27fd-1e2d-1234-66e2fdea0987"
     
     # Example 3: Check recent notifications
     "What notifications do I have on my storage infrastructure?"
     ```

### 3. `fetch_storage_systems`

   - **Description**: Get all storage systems added to the tenant for monitoring tenant.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of storage systems present on the tenant.
   - **Examples**:
     ```
     # Example 1: List all storage systems
     "Show me all storage systems in my tenant"
     
     # Example 2: Get storage systems for specific tenant
     "List storage systems for tenant 01f13d45-27fd-1e2d-1234-66e2fdea0987"
     
     # Example 3: Check available systems
     "What storage systems are being monitored?"
     ```

### 4. `fetch_system_notifications`

   - **Description**: Get notifications of system under the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of notifications for a system represented by unique system id.
   - **Examples**:
     ```
     # Example 1: Get notifications for a specific system
     "Show notifications for system 5249e140-3d44-11f1-8e40-a94d2a0672fd"
     
     # Example 2: Check system-specific notifications
     "What notifications exist for storage system 5249e140-3d44-11f1-8e40-a94d2a0672fd?"
     
     # Example 3: Get notifications for system in specific tenant
     "Get notifications for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in tenant 01f13d45-27fd-1e2d-1234-66e2fdea0987"
     ```

### 5. `fetch_system_details`

   - **Description**: Get details for given system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: Details of a system represented by unique system id.
   - **Examples**:
     ```
     # Example 1: Get complete details of a system
     "Show me details for storage system 5249e140-3d44-11f1-8e40-a94d2a0672fd"
     
     # Example 2: Check system configuration
     "What are the details of system 5249e140-3d44-11f1-8e40-a94d2a0672fd?"
     
     # Example 3: Get system info for specific tenant
     "Get details for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in tenant 01f13d45-27fd-1e2d-1234-66e2fdea0987"
     ```

### 6. `fetch_system_io_rate`

   - **Description**: Get io rate for a system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
     - `metric_types` *(optional list of strings)*: performance metric types
     - `duration` *(optional string)*: duration for the data fetch (e.g. `20m`, `1h`, `1d`)
   - **Returns**: Requested IO Rate for the given system represented by unique system id.
   - **Supported IO rate metrics**
     - `volume_overall_read_io_rate`
     - `volume_overall_write_io_rate`
     - `volume_overall_total_io_rate`
   - **Examples**:
     ```
     # Example 1: Get IO rate for last hour
     "Show me IO rate for system 5249e140-3d44-11f1-8e40-a94d2a0672fd for the last 1 hour"
     
     # Example 2: Get read and write IO rates for last day
     "Get read and write IO rates for system 5249e140-3d44-11f1-8e40-a94d2a0672fd over the last day"
     
     # Example 3: Check total IO rate for last 20 minutes
     "What is the total IO rate for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in the last 20 minutes?"
     ```

### 7. `fetch_system_data_rate`

   - **Description**: Get data rate for a system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
     - `metric_types` *(optional list of strings)*: performance metric types
     - `duration` *(optional string)*: duration for the data fetch (e.g. `20m`, `1h`, `1d`)
   - **Returns**: Requested Data Rate for the given system represented by unique system id.
   - **Supported IO rate metrics**
     - `volume_read_data_rate`
     - `volume_write_data_rate`
     - `volume_total_data_rate`
   - **Examples**:
     ```
     # Example 1: Get data rate for last hour
     "Show me data rate for system 5249e140-3d44-11f1-8e40-a94d2a0672fd for the past hour"
     
     # Example 2: Get read data rate for last day
     "What is the read data rate for system 5249e140-3d44-11f1-8e40-a94d2a0672fd over the last 24 hours?"
     
     # Example 3: Check total data throughput
     "Get total data rate for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in the last 30 minutes"
     ```
    
### 8. `fetch_system_response_time`

   - **Description**: Get response time for a system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
     - `metric_types` *(optional list of strings)*: performance metric types
     - `duration` *(optional string)*: duration for the data fetch (e.g. `20m`, `1h`, `1d`)
   - **Returns**: Requested Response time for the given system represented by unique system id.
   - **Supported IO rate metrics**
     - `volume_read_response_time`
     - `volume_write_response_time`
     - `volume_total_response_time`
   - **Examples**:
     ```
     # Example 1: Get response time for last hour
     "Show me response time for system 5249e140-3d44-11f1-8e40-a94d2a0672fd for the last hour"
     
     # Example 2: Check read response time
     "What is the read response time for system 5249e140-3d44-11f1-8e40-a94d2a0672fd over the last day?"
     
     # Example 3: Get total response time metrics
     "Get total response time for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in the last 20 minutes"
     ```

### 9. `fetch_system_transfer_size`

   - **Description**: Get transfer size for a system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
     - `metric_types` *(optional list of strings)*: performance metric types
     - `duration` *(optional string)*: duration for the data fetch (e.g. `20m`, `1h`, `1d`)
   - **Returns**: Requested transfer size for the given system represented by unique system id.
   - **Supported IO rate metrics**
     - `volume_read_transfer_size`
     - `volume_write_transfer_size`
     - `volume_total_transfer_size`
   - **Examples**:
     ```
     # Example 1: Get transfer size for last hour
     "Show me transfer size for system 5249e140-3d44-11f1-8e40-a94d2a0672fd for the last hour"
     
     # Example 2: Check write transfer size
     "What is the write transfer size for system 5249e140-3d44-11f1-8e40-a94d2a0672fd over the last day?"
     
     # Example 3: Get total transfer size metrics
     "Get total transfer size for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in the last 30 minutes"
     ```

### 10. `fetch_system_cpu_utilization`

   - **Description**: Get cpu utilization for a system present on the tenant.
   - **Inputs**:
      - `system_id` *(string)*: Unique system id for the system.
      - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
      - `metric_types` *(optional list of strings)*: performance metric types
      - `duration` *(optional string)*: duration for the data fetch (e.g. `20m`, `1h`, `1d`)
   - **Returns**: Requested cpu utilization for the given system represented by unique system id.
   - **Supported IO rate metrics**
      - `cpu_utilization`
   - **Examples**:
     ```
     # Example 1: Get CPU utilization for last hour
     "Show me CPU utilization for system 5249e140-3d44-11f1-8e40-a94d2a0672fd for the last hour"
     
     # Example 2: Check CPU usage over last day
     "What is the CPU utilization for system 5249e140-3d44-11f1-8e40-a94d2a0672fd over the last 24 hours?"
     
     # Example 3: Monitor CPU performance
     "Get CPU utilization for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in the last 20 minutes"
     ```

### 11. `fetch_system_capacity`

   - **Description**: Get capacity for a system present on the tenant.
   - **Inputs**:
      - `system_id` *(string)*: Unique system id for the system.
      - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
      - `metric_types` *(optional list of strings)*: performance metric types
      - `duration` *(optional string)*: duration for the data fetch (e.g. `20m`, `1h`, `1d`)
   - **Returns**: Requested capacity for the given system represented by unique system id.
   - **Supported IO rate metrics**
      - `used_capacity`
      - `available_capacity`
   - **Examples**:
     ```
     # Example 1: Get capacity metrics for last hour
     "Show me capacity metrics for system 5249e140-3d44-11f1-8e40-a94d2a0672fd for the last hour"
     
     # Example 2: Check available capacity
     "What is the available capacity for system 5249e140-3d44-11f1-8e40-a94d2a0672fd?"
     
     # Example 3: Monitor used capacity over time
     "Get used capacity for system 5249e140-3d44-11f1-8e40-a94d2a0672fd over the last day"
     ```
       
### 12. `fetch_system_components`

   - **Description**: Get component for a system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `comp_type` *(string)*: name of the component to fetch.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: Requested capacity for the given system represented by unique system id.
   - **Supported components**
     - `volumes`
     - `pools`
     - `enclosures`
     - `drives`
     - `fc-ports`
     - `ip-ports`
     - `host-connections`
     - `io-groups`
     - `managed-disks`
   - **Examples**:
     ```
     # Example 1: Get volumes for a system
     "Show me all volumes for system 5249e140-3d44-11f1-8e40-a94d2a0672fd"
     
     # Example 2: List storage pools
     "What pools are configured on system 5249e140-3d44-11f1-8e40-a94d2a0672fd?"
     
     # Example 3: Check FC ports
     "Get fc-ports for system 5249e140-3d44-11f1-8e40-a94d2a0672fd"
     ```

### 13. `fetch_system_alerts`

   - **Description**: Get alerts of system under the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of alerts for a system represented by unique system id.
   - **Examples**:
     ```
     # Example 1: Get alerts for a specific system
     "Show me alerts for system 5249e140-3d44-11f1-8e40-a94d2a0672fd"
     
     # Example 2: Check system alerts
     "What alerts are active on system 5249e140-3d44-11f1-8e40-a94d2a0672fd?"
     
     # Example 3: Get alerts for system in specific tenant
     "Get alerts for system 5249e140-3d44-11f1-8e40-a94d2a0672fd in tenant tenant123"
     ```

## 💬 Prompts

### 1. `morning_cup_of_coffee`
   
   - **Description**: Fetch storage system details, alert details and notification details in sequence with the same input. Filter the result to show only systems in error status, critical alerts and notifications.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: Prompt to execute required tools and output the result
   - **Examples**:
     ```
     # Example 1: Get morning summary with default tenant
     "Run morning cup of coffee for my tenant"
     
     # Example 2: Get daily health check
     "Give me the morning cup of coffee report"
     
     # Example 3: Get summary for specific tenant
     "Run morning cup of coffee for tenant 01f13d45-27fd-1e2d-1234-66e2fdea0987"
     ```

## 🧪 Setup

### Set up your environment
   - Install uv : Refer [Installing UV](https://docs.astral.sh/uv/getting-started/installation/) section to install uv.
### Storage Insights Credentials

Tools in this MCP Server invokes [IBM Storage Insights](https://www.ibm.com/products/storage-insights) APIs and hence needs Storage Insights tenant ID and API key for a working setup. Refer [Generating a REST API key](https://www.ibm.com/docs/en/storage-insights?topic=configuring-user-access-management) to generate REST API key for your tenant ID. 

Add below values to `src/si_mcp_server_oss/.env` file:

```env
DEFAULT_SI_TENANT_ID =  <Your Storage Insights tenant ID>
DEFAULT_SI_API_KEY = <Your Storage Insights External Rest API key>
ADDITIONAL_TENANT_API_MAPPING = <Additional tenant id and API key mapping if you want the server to support multiple tenants (optional)>
LOG_FILE_PATH = <Directory path to store mcp server logs (optional)>
LOG_LEVEL = <Log level fo the configured logger (optional)>
CONFIG_FILE_PATH = <Path to the config file (optional)>
```

## 🖥️ Usage with Claude Desktop

Add the following configuration to your `claude_desktop_config.json`:

**MacOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "si_mcp_server": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/si-mcp-server-oss/src/si_mcp_server_oss",
        "run",
        "server.py"
      ]
    }
  }
}
```

## 🐞 Testing and Debugging

1. We recommend using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) for testing and debugging. You can run the inspector with:

   ```bash
   npx @modelcontextprotocol/inspector uv --directory /ABSOLUTE/PATH/TO/PARENT/FOLDER/si-mcp-server-oss/src/si_mcp_server_oss run server.py
   ```
   The inspector will provide a URL you can open in your browser to see logs and send requests manually.

2. Optionally, change `LOG_LEVEL` in .env file and set it to `DEBUG` to collect debug logs from the server.

## Running MCP server with Streamable HTTP Transport

This MCP servers is configured to communicate over standard input/output (transport=stdio), but can be re-configured for Streamable HTTP. To setup streamable HTTP please refer [Authentication](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#authentication) and [Streamable HTTP](https://github.com/modelcontextprotocol/python-sdk?tab=readme-ov-file#streamable-http-transport)


## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or a pull request if you have any suggestions, bug reports, or improvements to propose.

## 📄 License

This project is licensed under the [Apache License, Version 2.0](./LICENSE).
