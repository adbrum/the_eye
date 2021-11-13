#!/usr/bin/env bash
# Usage: source setup.sh

# Colors
red=`tput setaf 1`
green=`tput setaf 2`
reset=`tput sgr0`

echo "${green}>>> Creating .env${reset}"
cp contrib/env-sample.env .env

sleep 2
echo "${green}>>> Start docker-compose.${reset}"
docker-compose up -d

echo "${green}>>> Running migration database...${reset}"
docker-compose run --rm web python manage.py migrate

echo "${green}>>> Create superuser...${reset}"
docker-compose run --rm web python manage.py createsuperuser --email=''

echo "${green}>>> Running tests...${reset}"
docker-compose run --rm web python manage.py test

echo "${green}>>> Done.${reset}"