#!/bin/bash

docker stack rm cluster

pkill -f elasticsearch 

pkill -f kibana

