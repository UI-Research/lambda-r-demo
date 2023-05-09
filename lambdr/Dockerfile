FROM public.ecr.aws/lambda/provided

ENV R_VERSION=4.0.3
ENV R_SCRIPT=app.R 

RUN yum -y install wget git tar openssl-devel libxml2-devel \
  && yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
  && wget https://cdn.rstudio.com/r/centos-7/pkgs/R-${R_VERSION}-1-1.x86_64.rpm \
  && yum -y install R-${R_VERSION}-1-1.x86_64.rpm \
  && rm R-${R_VERSION}-1-1.x86_64.rpm \
  && yum -y clean all \
  && rm -rf /var/cache/yum

ENV PATH="${PATH}:/opt/R/${R_VERSION}/bin/"

RUN R -e "install.packages(c('aws.s3', 'dplyr', 'lambdr'), repos = 'https://cloud.r-project.org/')"

RUN mkdir /lambda
COPY ${R_SCRIPT} /lambda
RUN chmod 755 -R /lambda

RUN printf '#!/bin/sh\ncd /lambda\nRscript ${R_SCRIPT}' > /var/runtime/bootstrap \
  && chmod +x /var/runtime/bootstrap
