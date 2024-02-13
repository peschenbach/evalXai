import logging
import io
import tarfile
import docker


def trigger_evaluation_script_inside_worker(file_contents: str, challenge_id: int):
    try:
        # logging.DEBUG("entered trigger function")
        # Create a Docker client
        client = docker.from_env()

        # Specify the name or ID of the running container
        container_name_or_id = "evalxai-worker-1"
        container = client.containers.get(container_name_or_id)

        # Specify the path and filename inside the container
        destination_path = "/worker"
        compressed_filename = "uploaded_file.tar"
        decompressed_filename = "uploaded_file.py"
        script_filename = "emd.py"
        file_path_in_container = f"{destination_path}/{compressed_filename}"

        file_contents_bytes = file_contents.encode('utf-8')

        # Create a tarball from the bytes
        tar_data = io.BytesIO()
        with tarfile.open(fileobj=tar_data, mode='w') as tar:
            tarinfo = tarfile.TarInfo(name=decompressed_filename)
            tarinfo.size = len(file_contents_bytes)
            tar.addfile(tarinfo, io.BytesIO(file_contents_bytes))

        # Copy the tarball into the container
        tar_data.seek(0)
        container.put_archive(destination_path, tar_data)

        # return "successfully saved the file"
    except Exception as e:
        return f"no file saved. error: {e}"

    # python_code = """
    # import requests
    # response = requests.get('http://backend:8000/api/prediction/')
    # print(response.text)
    # """
    # command_test = ["python", "-c", python_code]
    # container.exec_run(command_test)

    # decompress file (go back to python)
    command = f"tar -xf {file_path_in_container} -C {destination_path}"
    container.exec_run(command)

    # run the script
    command = f"python {destination_path}/{script_filename}"
    result = container.exec_run(command)

    # TODO: read the saved file and send it back in result to see its content
    return f"{result}"
    # logging.DEBUG(result.output.decode("utf-8"))

    # Print the output of the command
    # print(result.output.decode("utf-8"))
