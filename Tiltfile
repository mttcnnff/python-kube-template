# -*- mode: Python -*

k8s_yaml('k8s/kubernetes.yaml')
k8s_resource('spend-api', port_forwards=8000)

# Records the current time, then kicks off a server update.
# Normally, you would let Tilt do deploys automatically, but this
# shows you how to set up a custom workflow that measures it.
#local_resource(
#    'deploy',
#    'python now.py > start-time.txt',
#)

# Add a live_update rule to our docker_build
congrats = "🎉 Congrats, you ran a live_update! 🎉"
docker_build('spend-api:latest', '.', build_args={},
    live_update=[
        sync('.', '/app'),
        run('cd /app && poetry install',
            trigger=['./poetry.lock', 'pyproject.toml']),

        # if all that changed was start-time.txt, make sure the server
        # reloads so that it will reflect the new startup time
        # run('touch /app/app.py', trigger='./start-time.txt'),

        # add a congrats message!
        #run('sed -i "s/Hello cats!/{}/g" /app/templates/index.html'.
        #   format(congrats)),
])