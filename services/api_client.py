import requests


class APIClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def __init__(self):
        self._auth_token = None

    def get_auth_token(self):
        """Получить токен авторизации"""
        if not self._auth_token:
            auth_data = {"username": "admin", "password": "password123"}
            response = requests.post(f"{self.BASE_URL}/auth", json=auth_data)
            if response.status_code == 200:
                self._auth_token = response.json().get("token")
        return self._auth_token

    def get_auth_cookies(self):
        """Получить cookies с токеном для авторизации"""
        token = self.get_auth_token()
        return {"token": token} if token else None

    def post(self, endpoint, data=None, headers=None, cookies=None):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=data, headers=headers, cookies=cookies)

    def get(self, endpoint, params=None, headers=None):
        return requests.get(f"{self.BASE_URL}{endpoint}", params=params, headers=headers)

    def put(self, endpoint, data=None, headers=None, cookies=None):
        if cookies is None:
            cookies = self.get_auth_cookies()
        return requests.put(f"{self.BASE_URL}{endpoint}", json=data, headers=headers, cookies=cookies)

    def patch(self, endpoint, data=None, headers=None, cookies=None):
        if cookies is None:
            cookies = self.get_auth_cookies()
        return requests.patch(f"{self.BASE_URL}{endpoint}", json=data, headers=headers, cookies=cookies)

    def delete(self, endpoint, headers=None, cookies=None):
        if cookies is None:
            cookies = self.get_auth_cookies()
        return requests.delete(f"{self.BASE_URL}{endpoint}", headers=headers, cookies=cookies)
