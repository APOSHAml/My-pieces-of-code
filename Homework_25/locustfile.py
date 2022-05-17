from locust import HttpUser, task
import random

class QuickStartUser(HttpUser):
    token = ""

    def on_start(self):
        response = self.token = self.client.post(
            "/authorize", json={"name": "vasia"
                                }
        )
        self.token = response.json()['token']

    @task
    def get_post(self):
        self.client.get(
            f'/meme/{random.randint(1,100)}',
            headers={
                'Authorization': self.token
                        }
        )