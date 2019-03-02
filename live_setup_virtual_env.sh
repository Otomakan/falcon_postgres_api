function virtual_env_setup {
    VIRTUALENV_NAME="falconAPI"
    virtualenv -p python3.6 ${VIRTUALENV_NAME}

    source ${VIRTUALENV_NAME}/bin/activate
    echo "upgrading"
    python3.6 -m pip install --upgrade pip

    python3.6 -m pip install --upgrade wheel
    echo "To requirements"
    python3.6 -m pip install -r requirements.txt
    python3.6 -m pip install -r requirements-dev.txt
    echo "deactivate"
    deactivate
    source ${VIRTUALENV_NAME}/bin/activate
    PYTHONPATH=$PYTHONPATH:. alembic upgrade head
    echo "Running '$1' inside virtual environment…"
    $1
}