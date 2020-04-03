from kombu import Queue, Exchange
broker_url = "redis://127.0.0.1/14"  # 中间者
result_backend = "redis://127.0.0.1/15"  # 可以配置也可以不配置,如果客户端不需要结果的话就无需配置
timezone = 'Asia/Shanghai'   # 时区
task_queues = (
    Queue('priority_high', exchange=Exchange('priority_high'), routing_key='priority_high'),
    Queue('priority_low', exchange=Exchange('priority_low'), routing_key='priority_low')
)