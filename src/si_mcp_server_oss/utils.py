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

import json
import logging
import os
import time
from typing import Optional, Any

import httpx


from settings import (
    SI_BASE_URL,
    SI_TENANT_ID,
    SI_API_KEY,
    CONFIG_FILE_PATH,
)

# Load the default and additional tenant-api mappings in case if multi-tenant view is required
additional_tenant_api_mapping = json.loads(os.getenv("ADDITIONAL_TENANT_API_MAPPING"))

with open(CONFIG_FILE_PATH) as file:
    config = json.load(file)


def get_metric_names(group_name: str):
    """
    Get list of metric names from config.json
    Args:
        group_name (string): name of metric group

    Returns:
        List of metrics in the given metric group
    """
    group = config.get(group_name, [])
    return [metric["name"] for metric in group]


# Initialize the caches for re-using the short-lived token (when not expired) for SI API invocation
token_cache = {}


async def fetch_token(
    si_tenant_id: str, si_api_key: str, logger: logging.Logger
) -> str | None:
    """
    Search of an existing token or request a new token from Storage Insights
    Args:
        si_tenant_id (string): Storage insights tenant ID
        si_api_key (string): Storage insights api key
        logger (logging.looger): Logger

    Returns:
        Returns a short-lived token
    """
    if si_tenant_id in token_cache and token_cache[si_tenant_id].get("expiration") > (
        time.time() * 1000
    ):
        logger.info(f"Re-using existing token for tenant {si_tenant_id}")
        token = token_cache[si_tenant_id].get("token")
    else:
        logger.info(f"Creating new token for tenant {si_tenant_id}")
        token = None
        url = f"{SI_BASE_URL}/tenants/{si_tenant_id}/token"
        headers = {
            "x-api-key": f"{si_api_key}",
            "Content-Type": "application/json",
            "x-integration": "si-mcp",
            "x-integration-version": "v1",
        }
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(url, headers=headers, timeout=30.0)
                response.raise_for_status()
                data = response.json()
                token = data.get("result")["token"]
                expiration = data.get("result")["expiration"]
                if si_tenant_id not in token_cache:
                    token_cache[si_tenant_id] = dict()
                token_cache[si_tenant_id]["token"] = token
                token_cache[si_tenant_id]["expiration"] = expiration
                logger.info(f"Fetched new token for tenant {si_tenant_id}")
            except Exception as e:
                logger.error(f"Token fetch failed for tenant {si_tenant_id}: {e}")
                raise e
    return token


def resolve_tenant_id(tenant_id: str, logger: logging.Logger) -> tuple[str, str] | None:
    """
    Validate the tenant id passed from the agent/client. If it is among additional tenants, fetch the API KEY.
    If not present in the tenant api mapping, None should be returned
    Args:
        tenant_id (string): Storage insights tenant ID
        logger (logging.logger): Logger

    Returns:
        Return tenant ID and api key
    """
    if tenant_id == SI_TENANT_ID:
        si_tenant_id = tenant_id
        si_api_key = SI_API_KEY
        logger.debug(f"Reconciled to default TENANT_ID {si_tenant_id}")
    elif tenant_id in additional_tenant_api_mapping:
        si_tenant_id = tenant_id
        si_api_key = additional_tenant_api_mapping.get(si_tenant_id, None)
        logger.debug(f"Reconciled to alternate TENANT_ID {si_tenant_id}")
    else:
        si_tenant_id = None
        si_api_key = None
        logger.error("Unlisted TENANT_ID")
        raise ValueError(f"Un-supported tenant ID: {tenant_id}")
    return si_tenant_id, si_api_key


async def call_ibm_storageinsights_api(
    url: str,
    logger: logging.Logger,
    params: Optional[dict] = None,
    tenant_id: Optional[str] = None,
    api_key: Optional[str] = None,
) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling."""
    logger.info(f"Fetch the token for SI API invocation for tenant id {tenant_id}")
    token = await fetch_token(tenant_id, api_key, logger)
    headers = {
        "x-api-token": f"{token}",
        "Content-Type": "application/json",
        "x-integration": "si-mcp",
        "x-integration-version": "v1",
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(
                url, params=params, headers=headers, timeout=100.0
            )
            response.raise_for_status()
            if response.content:
                result = response.json()
            else:
                result = None
            logger.debug("Received API response")
        except Exception as e:
            logger.error(f"Encountered error in API call. Error: {e}")
            raise e
    return result
