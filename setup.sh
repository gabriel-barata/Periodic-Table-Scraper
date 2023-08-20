#!/bin/bash

setup() {

    # Creating the python virtual environment and installing dependencies
    python3 -m venv venv
    venv/bin/activate
    pip install -r ./requirements.txt

    # Install the playwright drivers
    playwright install

    # Set the database
    cd database
    docker-compose up -d
    cd ..

}

run() {

  scrapy crawl periodic_elements

}

destroy() {

  cd database
  docker-compose down
  cd ..

}

case $1 in
  setup)
    setup
    ;;
  run)
    run
    ;;
  destroy)
    ;;
  *)
    echo "-e: No argument was declared! Usage: $0 {setup | run | destroy}"
    ;;
esac