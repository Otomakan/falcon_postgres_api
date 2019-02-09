function virtual_env_setup {
    VIRTUALENV_NAME=env

    if [ ! -d ${VIRTUALENV_NAME} ]; then
      virtualenv env -p python3
    fi

    source ${VIRTUALENV_NAME}/bin/activate
    # pip install --upgrade pip
    # pip install --upgrade wheel
    # pip install -r requirements.txt
    # pip install -r requirements-dev.txt
    # Create routes and models automatically
    deactivate
    source ${VIRTUALENV_NAME}/bin/activate
    PYTHONPATH=$PYTHONPATH:. alembic upgrade head
    echo "Running '$1' inside virtual environment…"
    $1
}
