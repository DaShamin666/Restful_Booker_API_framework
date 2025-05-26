import requests

class APIClient:
    BASE_URL = "https://restful-booker.herokuapp.com"

    def post(self, endpoint, data=None, headers=None, cookies=None):
        return requests.post(f"{self.BASE_URL}{endpoint}", json=data, headers=headers, cookies=cookies)

    def get(self, endpoint, params=None, headers=None):
        return requests.get(f"{self.BASE_URL}{endpoint}", params=params, headers=headers)

    def put(self, endpoint, data=None, headers=None, cookies=None):
        return requests.put(f"{self.BASE_URL}{endpoint}", json=data, headers=headers, cookies=cookies)

    def patch(self, endpoint, data=None, headers=None, cookies=None):
        return requests.patch(f"{self.BASE_URL}{endpoint}", json=data, headers=headers, cookies=cookies)

    def delete(self, endpoint, headers=None, cookies=None):
        return requests.delete(f"{self.BASE_URL}{endpoint}", headers=headers, cookies=cookies) 