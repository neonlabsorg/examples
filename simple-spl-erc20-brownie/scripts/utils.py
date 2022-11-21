import time
import requests


class Faucet:
    def __init__(self, faucet_url: str) -> None:
        self._url = faucet_url
        self._session = requests.Session()

    def request_neon(self, account: str, amount: int = 1000) -> None:
        response = self._session.post(
            self._url, json={"amount": amount, "wallet": account}
        )
        assert response.ok, f"Faucet returned error: {response.text}"
        time.sleep(3)
        return response
