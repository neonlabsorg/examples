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
        response.raise_for_status()
        time.sleep(3)
