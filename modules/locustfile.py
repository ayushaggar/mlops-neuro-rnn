import time
from locust import HttpUser, task
# import locust

class QuickstartUser(HttpUser):
    @task(1)
    def view_item(self):
        for i in range(100):
            self.client.get(f"/predict/Albert{i}", name="/item")
            time.sleep(1)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass