FROM public.ecr.aws/lambda/python:3.10

ENV R_VERSION=4.3.1

RUN yum -y install wget git tar openssl-devel libxml2-devel \
  && yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm \
  && wget https://cdn.rstudio.com/r/centos-7/pkgs/R-${R_VERSION}-1-1.x86_64.rpm \
  && yum -y install R-${R_VERSION}-1-1.x86_64.rpm \
  && rm R-${R_VERSION}-1-1.x86_64.rpm \
  && yum -y clean all \
  && rm -rf /var/cache/yum

ENV PATH="${PATH}:/opt/R/${R_VERSION}/bin/" 
ENV LD_LIBRARY_PATH="/opt/R/${R_VERSION}/lib/R/lib/" 

RUN R -e "install.packages(c('aws.s3', 'dplyr'), \
  repos = c(CRAN = 'https://packagemanager.posit.co/cran/__linux__/centos7/latest'))"

COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY . ${LAMBDA_TASK_ROOT} 