# -*- mode: Python -*

k8s_yaml('k8s/kubernetes.yaml')
k8s_resource('spend-api', port_forwards=8000)

# Add a live_update rule to our docker_build
congrats = "🎉 Congrats, you ran a live_update! 🎉"
docker_build('spend-api:latest', '.', build_args={},
    live_update=[
        sync('.', '/app'),
        run('cd /app && poetry install',
            trigger=['./poetry.lock', 'pyproject.toml']),
])