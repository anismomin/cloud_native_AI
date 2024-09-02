FROM openjdk:8-jre-slim

WORKDIR /app

ENV KAFKA_VERSION=3.7.0 \
    SCALA_VERSION=2.13 \
    KAFKA_HOME=/app/kafka_$SCALA_VERSION-$KAFKA_VERSION \
    PATH=$PATH:$KAFKA_HOME/bin

RUN apt-get update \
    && apt-get install -y bash wget netcat \
    && wget https://archive.apache.org/dist/kafka/$KAFKA_VERSION/kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz \
    && tar xzf kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz \
    && mv kafka_$SCALA_VERSION-$KAFKA_VERSION $KAFKA_HOME \
    && rm kafka_$SCALA_VERSION-$KAFKA_VERSION.tgz \
    && chmod +x /app

COPY create-topics.sh /app/

ENTRYPOINT ["bash", "/app/create-topics.sh"]