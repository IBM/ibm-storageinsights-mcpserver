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

### 2. `fetch_tenant_notifications`

   - **Description**: Retrieve a list of notifications for a tenant.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of notifications present for the tenant.

### 3. `fetch_storage_systems`

   - **Description**: Get all storage systems added to the tenant for monitoring tenant.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of storage systems present on the tenant.

### 4. `fetch_system_notifications`

   - **Description**: Get notifications of system under the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of notifications for a system represented by unique system id.

### 5. `fetch_system_details`

   - **Description**: Get details for given system present on the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: Details of a system represented by unique system id.

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

### 13. `fetch_system_alerts`

   - **Description**: Get alerts of system under the tenant.
   - **Inputs**:
     - `system_id` *(string)*: Unique system id for the system.
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: List of alerts for a system represented by unique system id.

## 💬 Prompts

### 1. `morning_cup_of_coffee`
   
   - **Description**: Fetch storage system details, alert details and notification details in sequence with the same input. Filter the result to show only systems in error status, critical alerts and notifications.
   - **Inputs**:
     - `tenant_id_input` *(optional string)*: Storage Insights Tenant id.
   - **Returns**: Prompt to execute required tools and output the result

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
