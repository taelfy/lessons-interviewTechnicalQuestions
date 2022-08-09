import os
port = int(os.getenv('PORT', default=8080))

bind=f"0.0.0.0:{port}"

workers=2

threads=4

timeout=120

worker_class="gthread"

preload_app=False