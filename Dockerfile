
# Pull an official base image
FROM python:3.10.5-slim-bullseye

# Setting work directory
WORKDIR /MonikaiT-project1
# Install dependencies
COPY ./requirements.txt /MonikaiT-project1/requirements.txt
RUN pip install -r requirements.txt

# Copy src files
COPY . /MonikaiT-project1/ 

# Run Server
RUN export FLASK_APP=app.py
RUN export FLASK_ENV=development
RUN export FLASK_RUN_PORT=5000
RUN export FLASK_RUN_HOST=0.0.0.0

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
