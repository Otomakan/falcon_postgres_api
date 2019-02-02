source ./setup_virtual_env.sh

function run_falcon_server {
     gunicorn my_app.router:app --reload
}

virtual_env_setup run_falcon_server
