# a_class.py
import ray

class Foo:
    @ray.remote
    def single_function(self):
        return None

    def combined_function(self):
        ray.init()
        results_id = [Foo.single_function.remote(self) for i in range(5)]
        results = ray.get(results_id)
        ray.shutdown()
        return None