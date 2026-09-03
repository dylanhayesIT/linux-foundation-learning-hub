from kubernetes.policy import validate_workload
from linux.health import health_score
from observability.metrics import aggregate
from aiops.scheduler import choose_node
from data.model import normalize
from platform.deployment import readiness

def test_policy(): assert "app:missing_resources" in validate_workload({"containers":[{"name":"app"}]})
def test_health(): assert 0 <= health_score(1,30,40) <= 100
def test_metrics(): assert aggregate([{"name":"cpu","value":20},{"name":"cpu","value":40}])["cpu"]==30
def test_scheduler(): assert choose_node([{"name":"a","cpu_free":8,"memory_free_gb":16,"accelerator":True}],4,8,True)=="a"
def test_data(): assert normalize([{"timestamp":"t","metric":"cpu","value":"2"}])[0]["value"]==2
def test_ready(): assert readiness(True,True,True,False,True)==80
