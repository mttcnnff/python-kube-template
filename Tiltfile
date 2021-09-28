# -*- mode: Python -*

k8s_yaml('k8s/local/kubernetes.yaml')
k8s_resource('spend-api', port_forwards=8000)

k8s_yaml('k8s/local/postgres.yaml')
k8s_resource('spend-api-db', port_forwards=5432)

#k8s_yaml('k8s/local/pgadmin.yaml')
#k8s_resource('spend-api-db-admin', port_forwards='5433:80')

docker_prune_settings(disable=False, num_builds=1, keep_recent=2 )
docker_build('spend-api:latest', '.', build_args={},
    live_update=[
        sync('.', '/app'),
        run('cd /app && poetry install',
            trigger=['./poetry.lock', 'pyproject.toml']),
])