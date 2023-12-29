import logging

import docker


def trigger_evaluation_script_inside_worker():
    # logging.DEBUG("entered trigger function")
    # Create a Docker client
    client = docker.from_env()

    # Specify the name or ID of the running container
    container_name_or_id = "evalxai-worker-1"

    # logging.DEBUG("created docker client")

    # Get the container object
    container = client.containers.get(container_name_or_id)

    # logging.DEBUG("successfully got the worker container")

    # Execute a command in the container
    print("In Trigger function")
    command = "python evaluate.py"
    result = container.exec_run(command)

    # logging.DEBUG(result.output.decode("utf-8"))

    # Print the output of the command
    print(result.output.decode("utf-8"))
