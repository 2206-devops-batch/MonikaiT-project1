FROM jenkins/jenkins:lts

RUN /usr/local/bin/install-plugins.sh ssh-slave
RUN /usr/local/bin/install-plugins.sh kubernetes

USER root
RUN apt-get update && apt-get install git -y
USER jenkins
