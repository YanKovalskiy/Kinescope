import pytest
from playwright.sync_api import Playwright

from environment import Environment


@pytest.fixture(scope="session")
def api_request(playwright: Playwright):
    request_context = playwright.request.new_context()
    yield request_context
    request_context.dispose()


@pytest.fixture()
def token():
    return Environment.get_environment_variable('TOKEN')


@pytest.fixture()
def email():
    return Environment.get_environment_variable('EMAIL')


@pytest.fixture()
def password():
    return Environment.get_environment_variable('PASSWORD')


@pytest.fixture()
def parent_id(api_request, token):
    headers = {
        'Authorization': f'Bearer {token}'
    }
    request = api_request.get(url='https://api.kinescope.io/v1/projects?catalog_type=vod&per_page=100&page=1',
                          headers=headers)
    return request.json()['data'][0]['id']
