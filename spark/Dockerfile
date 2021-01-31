#
#  Author: Hari Sekhon
#  Date: 2016-01-16 09:58:07 +0000 (Sat, 16 Jan 2016)
#
#  vim:ts=4:sts=4:sw=4:et
#
#  https://github.com/harisekhon/Dockerfiles
#
#  If you're using my code you're welcome to connect with me on LinkedIn and optionally send me feedback to help improve or steer this or other code I publish
#
#  https://www.linkedin.com/in/harisekhon
#

#FROM harisekhon/centos-java:jre7
# > 100MB smaller than centos
FROM alpine:latest
MAINTAINER Hari Sekhon (https://www.linkedin.com/in/harisekhon)

ARG SPARK_VERSION=3.0.1
ARG HADOOP_VERSION=3.2
ARG ZEPPELIN_VERSION=0.9.0
ARG TAR=spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
ARG Z_TAR=zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz

ENV PATH $PATH:/spark/bin
ENV ZEPPELIN_PORT 18080

LABEL Description="Apache Spark" \
    "Spark Version"="$SPARK_VERSION"

#COPY spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION /spark
#ADD "http://d3kbcqa49mib13.cloudfront.net/${TAR}"

WORKDIR /

RUN set -eux && \
    apk add --no-cache bash openjdk8-jre-base wget tar && \
    python3 && \ 
    ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools
    
RUN wget -t 100 --retry-connrefused -O "$Z_TAR" "https://downloads.apache.org/zeppelin/zeppelin-${ZEPPELIN_VERSION}/${Z_TAR}" && \
    tar zxf "${Z_TAR}" && \
    rm -fv "${Z_TAR}" && \
    ln -s "zeppelin-${ZEPPELIN_VERSION}-bin-all" zeppelin
    
RUN wget -t 100 --retry-connrefused -O "$TAR" "https://downloads.apache.org/spark/spark-${SPARK_VERSION}/${TAR}" && \
    tar zxf "${TAR}" && \
    rm -fv "${TAR}" && \
    ln -s "spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION" spark
    
RUN apk del wget tar

RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd && \
    cp -v /spark/conf/spark-env.sh.template /spark/conf/spark-env.sh

COPY entrypoint.sh /
COPY zeppelin-env.sh /zeppelin/conf/

COPY conf_hdfs /spark

EXPOSE 4040 7077 8080 8081 18080

CMD ["/entrypoint.sh"]
