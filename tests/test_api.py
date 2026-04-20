import asyncio

from main import root


def test_root_endpoint_metadata():
    payload = asyncio.run(root())

    assert payload["name"] == "fifa-world-cup-chatbot-api"
    assert payload["docs"] == "/docs"
    assert payload["health"] == "/health"
