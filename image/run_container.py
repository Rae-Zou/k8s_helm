import docker

def run_container(image_name):
    client = docker.from_env()

    try:
        container = client.containers.run(
            image=image_name,
            detach=True,  # Detach the container so it runs in the background
            auto_remove=True,  # Automatically remove the container when it exits
            ports={'8080/tcp': 8080}  # Example port mapping (host_port:container_port)
        )
        print(f"Container {container.id} is running.")

        # Print container logs
        print("Container logs:")
        for line in container.logs(stream=True):
            print(line.decode('utf-8').strip())

    except docker.errors.ImageNotFound:
        print(f"Image {image_name} not found.")
    except docker.errors.APIError as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    image_name = "my-python-script"  # Replace with your Docker image name
    run_container(image_name)
