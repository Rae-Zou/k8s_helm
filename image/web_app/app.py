from flask import Flask, render_template, request
import docker

app = Flask(__name__)

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

        # Return container logs
        for line in container.logs(stream=True):
            print(line.decode('utf-8').strip())
        return container.logs().decode('utf-8')
    
    except docker.errors.ImageNotFound:
        return f"Image {image_name} not found."
    except docker.errors.APIError as e:
        return f"Error occurred: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_name = request.form['image_name']
        logs = run_container(image_name)
        return render_template('result.html', logs=logs)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
