#!/bin/bash

# remuve old version
cd ~
cd kafe_site
sudo docker-compose down
cd ..
rm -rf kafe_site

# clone new version
git clone https://github.com/Exillite/kafe_site.git
cp ~/prodenv/.env.prod ~/kafe_site
cp ~/prodenv/.env.prod.db ~/kafe_site

# start new version
cd kafe_site
sudo docker-compose -f docker-compose.prod.yml up -d --build
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
sudo docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear

# logging
d=`date`
echo $d -- kafe site deploy >> ~/deploylogs.txt

rm -- "$0"
