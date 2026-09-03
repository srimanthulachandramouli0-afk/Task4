sudo ufw status verbose
sudo ufw enable
sudo ufw deny 23/tcp
sudo ufw allow 22/tcp
sudo ufw status numbered
sudo ufw delete deny 23
