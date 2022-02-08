# havent understood v well, see:
# https://fastapi.tiangolo.com/advanced/async-tests/

# TODO BUT NOT URGENTO annotate the parameter 'app'

import pytest
from httpx import AsyncClient
from typing import Dict

from fastapi_tut.core.config import settings

@pytest.mark.anyio
async def test_get_access_token(client: AsyncClient) -> None:
	login_data = {
		"username": settings.FIRST_SUPERUSER_EMAIL,
		"password": settings.FIRST_SUPERUSER_PASSWORD,
	}
	r = await client.post(
		"/login/access-token", data=login_data)
	tokens = r.json()
	assert r.status_code == 200
	assert "access_token" in tokens
	assert tokens["access_token"]

@pytest.mark.anyio
async def test_use_access_token(
	client: AsyncClient, superuser_token_headers: Dict[str, str]
) -> None:
	r = await client.post(
		"/login/test-token", headers=await superuser_token_headers
	)
	result = r.json()
	assert r.status_code == 200
	assert "email" in result
