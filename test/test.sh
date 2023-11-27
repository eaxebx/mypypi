
sudo chown -R yang:yang /usr/share/nginx/html

rsync -av --delete /mnt/html/ /usr/share/nginx/html/
rsync -av --delete /usr/share/nginx/html/ /mnt/html/

sudo cp app.conf /etc/nginx/conf.d/
sudo cp vsftpd.conf /etc/

rsync -a /opt/media/ remote_user@remote_host_or_ip:/opt/media/