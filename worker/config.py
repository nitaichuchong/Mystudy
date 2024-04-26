broker_url = 'redis://127.0.0.1:6379/0'
broker_pool_limit = 100  # Broker 连接池子， 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['json', 'pickle']

task_serializer = 'pickle'
result_expires = 3600  # 任务过期时间

result_backend = 'redis://127.0.0.1:6379/0'
result_serializer = 'pickle'
result_cache_max = 1000  # 任务结果最大缓存数量

worker_redirect_stdouts_level = 'INFO'
