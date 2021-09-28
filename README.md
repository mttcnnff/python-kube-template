## Dev Env Setup

### Dev Env Dependencies

#### Minikube
1. Install Minikube, instructions found here: https://minikube.sigs.k8s.io/docs/start/
2. Start minikube with the driver of your choice (I've found Hyperkit less resource intensive than Docker):
```
$ minikube start --driver=hyperkit
```
3. Check the status of minikube:
```
$ minikube status
minikube
type: Control Plane
host: Running
kubelet: Running
apiserver: Running
kubeconfig: Configured
```

#### Tilt
1. Install Tilt, instructions found here: https://docs.tilt.dev/install.html
2. Verify the Tilt installation:
```
$ tilt version
v0.22.9, built 2021-09-17
```

#### Poetry (Optional)
_Poetry isn't a hard requirement as everything runs inside minikube, however it can be helpful to have all Python deps installed for things like syntax highlighting in an IDE, running DB migrations, etc._
1. Install Poetry, instructions found here: https://python-poetry.org/docs/master/#installation
2. Run `poetry shell` to create a virtualenv
3. Run `poetry install` from the repo's root directory

## Local Development

### Running the Dev Env
Run `tilt up` from the repo's root directory:
```
$ tilt up
Tilt started on http://localhost:10350/
v0.22.9, built 2021-09-17

(space) to open the browser
(s) to stream logs (--stream=true)
(t) to open legacy terminal mode (--legacy=true)
(ctrl-c) to exit
```

### Database Migrations
This project uses alembic for DB migrations, find more info about it here: https://alembic.sqlalchemy.org/en/latest/
1. Make sure you
2. Run `poetry shell` to activate the virtualenv for the project
3. Run `APP_ENV=<local|qa|prod> alembic upgrade head`
_Note: When running locally, you'll need to include DB_HOST as well: `APP_ENV=<local|qa|prod> DB_HOST=localhost alembic upgrade head`_

### PGAdmin (Optional)
When testing DB changes locally it might be helpful to use a UI to view tables, data, and run queries. PGAdmin is a nice tool to have for this.
1. Uncomment the following lines from the project's `Tilefile`:
```
k8s_yaml('k8s/local/pgadmin.yaml')
k8s_resource('spend-api-db-admin', port_forwards='5433:80')
```
2. Wait for the db-admin pod to come up:
```
$ kubectl get pods
NAME                                  READY   STATUS    RESTARTS   AGE
spend-api-c75d7cdd5-gtfvv             1/1     Running   0          8m5s
spend-api-db-5fd9d7785c-d8852         1/1     Running   0          48m
spend-api-db-admin-59d94b9b84-stgss   1/1     Running   0          49s  👈👈👈
```
4. Navigate to `http://localhost:5433/` and sign in with user:`admin@admin.com` and password:`password`
<img src="https://user-images.githubusercontent.com/17532157/135005262-19100036-f2ed-4ae5-b9fa-f4d5ea072f9a.png" width="750">
