#
#      Dockerfile, which includes all changes for DHBW image
#      * DHBW color Schema
#      * adapted Webpage and footers
#      * the configuration of invenio config 
# 
#      BASE image
#
#      we use the latest stable version v12.1.0 
#      * this image is used for web and worker pods   
# 
ARG INVENIO_VERSION=v12.1.0
# FROM registry.cern.ch/inveniosoftware/almalinux:latest
# FROM registry.cern.ch/inveniosoftware/demo-inveniordm:latest
# FROM ghcr.io/inveniosoftware/invenio-rdm:${INVENIO_VERSION}
# FROM registry.cern.ch/inveniosoftware/invenio-rdm:${INVENIO_VERSION}

#
#      for historic reason we keep the following lines in here
#      * we used the demo version for first tests
FROM ghcr.io/inveniosoftware/demo-inveniordm/demo-inveniordm:12.0.10

#      Install Python pip und Tools
# RUN yum install -y python3-pip

#      Install invenio-cli und dependencies
# RUN pip3 install invenio-cli

#
#      change working directory 
#
WORKDIR /opt/invenio

# 
#      Copy the DHBW UI Adjustments into the image 
# 
# 
#      1. the color schemas  
# 
COPY ./assets/less/site/globals /opt/invenio/src/assets/less/demo-inveniordm/globals/

#
#      2. the templates like frontpage, footer, ... 
# 
COPY ./templates/semantic-ui/invenio_app_rdm/frontpage.html /opt/invenio/src/templates/demo_inveniordm/demo_frontpage.html
COPY ./templates/semantic-ui/invenio_app_rdm/footer.html    /opt/invenio/src/templates/demo_inveniordm/footer.html

# 
#      3. the static data like images, ... 
# 
COPY ./static /opt/invenio/static
#
#      4. the invenio.cfg file 
# COPY ./configs/invenio.cfg /opt/invenio/invenio.cfg

#
#      Build the aessets in the image 
#
RUN invenio collect
RUN invenio webpack buildall 


#  This is old stuff that can be removed if the process works fine! 
# 
#
#    copy the logo to target
#
#COPY custom-assets/logo-fdm-dhbw.png /opt/invenio/src/static/images/logo-fdm-dhbw.png
#COPY custom-assets/logo-fdm-dhbw.png /opt/invenio/var/instance/static/images/logo-fdm-dhbw.png
#
#    copy the frontpage to target
#
#COPY custom-assets/fdm_frontpage.html /opt/invenio/src/templates/demo_inveniordm/demo_frontpage.html
#COPY custom-assets/fdm_frontpage.html /opt/invenio/var/instance/templates/demo_inveniordm/demo_frontpage.html
#
#    copy the invenio.cfg to target
#
#COPY custom-assets/invenio.cfg /opt/invenio/src/invenio.cfg
#COPY custom-assets/invenio.cfg /opt/invenio/var/instance/invenio.cfg
