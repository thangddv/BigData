FROM ubuntu:18.04

ARG SPARK_VERSION=3.1.1
ARG HADOOP_VERSION=3.2
ARG ZEPPELIN_VERSION=0.9.0
ARG SPARK_TAR=spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz
ARG SPARK_URL=https://mirror.downloadvn.com/apache/spark/spark-${SPARK_VERSION}/${SPARK_TAR}
ARG ZEPPELIN_TAR=zeppelin-${ZEPPELIN_VERSION}-bin-all.tgz
ARG ZEPPELIN_URL=https://mirror.downloadvn.com/apache/zeppelin/zeppelin-${ZEPPELIN_VERSION}/${ZEPPELIN_TAR}

LABEL Description="Apache Spark" \
    "Spark Version"="$SPARK_VERSION"

WORKDIR /

USER root

# install supported tools, java, python
RUN apt-get update && apt-get install -y --no-install-recommends\
    curl \
    nano \
    openjdk-8-jdk \
    python3 \
    && rm -rf /var/lib/apt/lists/*

RUN set -x \
    && curl -fSL "$SPARK_URL" -o /tmp/${SPARK_TAR} \
    && tar -xvf /tmp/${SPARK_TAR} -C /opt/ \
    && rm /tmp/${SPARK_TAR}* \
    && curl -fSL "$ZEPPELIN_URL" -o /tmp/${ZEPPELIN_TAR} \
    && tar -xvf /tmp/${ZEPPELIN_TAR} -C /opt/ \
    && rm /tmp/${ZEPPELIN_TAR}*
    
ENV PATH $PATH:/opt/spark/bin

RUN pip3 install --no-cache --upgrade pip setuptools

COPY conf_hdfs /opt/spark

EXPOSE 4040 7077 8080 8081 18080

ENTRYPOINT [ "/entrypoint.sh" ]
