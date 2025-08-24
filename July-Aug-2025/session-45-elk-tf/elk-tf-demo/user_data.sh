#!/bin/bash

#Update Install packages
apt-get update -y
apt-get install -y docker.io docker-compose

#Enable Docker Service
systemctl enable docker
systemctl start docker

mkdir -p /opt/elk
cd /opt/elk

cat <<EOF > docker-compose.yml
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.10
    container_name: elasticsearch
    environment:
      - discovery.type=single-node
      - ES_JAVA_OPTS=-Xms512m -Xmx512m
    ports:
      - "9200:9200"
    networks: [elk]
  logstash:
    image: docker.elastic.co/logstash/logstash:7.17.10
    container_name: logstash
    ports:
      - "5044:5044" 
    depends_on: [elasticsearch]
    networks: [elk]

  kibana:
    image: docker.elastic.co/kibana/kibana:7.17.10
    container_name: kibana
    environment:
      - ELASTICSEARCH_HOSTS=http://elasticsearch:9200
    ports:
      - "5601:5601"
    depends_on: [elasticsearch]
    networks: [elk]

networks:
  elk:
EOF

# Start ELK
docker-compose up -d