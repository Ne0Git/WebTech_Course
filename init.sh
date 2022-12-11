sudo ln -sf /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo /etc/init.d/mysql start

sudo mysql -u root -e "CREATE DATABASE IF NOT EXISTS ask_dev DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
CREATE USER 'box'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON ask_dev.* TO 'box'@'localhost';
FLUSH PRIVILEGES;"
