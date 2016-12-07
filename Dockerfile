############################################################
# Dockerfile to run a Django-based web application
# Based on an django Image
############################################################

# Set the base image to use to Ubuntu
FROM ubuntu:14.04

# Set the file maintainer (your name - the file's author)
MAINTAINER Harvey Kim <vaporize93@gmail.com>

# Set env variables used in this Dockerfile (add a unique prefix, such as DOCKYARD)
# Local directory with project source
ENV DOCKYARD_SRC=.
# Directory in container for all project files
ENV DOCKYARD_SRVHOME=/srv
# Directory in container for project source files
ENV DOCKYARD_SRVPROJ=/srv/dbp

# Timezone
ENV TZ=Asia/Seoul
RUN echo $TZ | tee /etc/timezone
RUN dpkg-reconfigure --frontend noninteractive tzdata

# Set apt repository mirror to korea
RUN sed -i 's/archive.ubuntu.com/ftp.kaist.ac.kr/g' /etc/apt/sources.list

# Update the default application repository sources list
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip nginx libjpeg8-dev libmysqlclient-dev

# Create application subdirectories
WORKDIR $DOCKYARD_SRVHOME
RUN mkdir logs

# Copy application source code to SRCDIR
COPY $DOCKYARD_SRC $DOCKYARD_SRVPROJ
VOLUME ["$DOCKYARD_SRVPROJ/skhualumni/media/", "$DOCKYARD_SRVHOME/logs/"]

# Install Python dependencies
RUN pip3 install -r $DOCKYARD_SRVPROJ/requirements.txt

# Port to expose
EXPOSE 80

# Copy entrypoint script into the image
WORKDIR $DOCKYARD_SRVPROJ
COPY dbp-entry.sh /
WORKDIR $DOCKYARD_SRVPROJ/skhualumni
ENTRYPOINT ["/dbp-entry.sh"]

