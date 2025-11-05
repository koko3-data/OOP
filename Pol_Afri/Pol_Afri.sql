CREATE USER 'polafri_user'@'localhost' IDENTIFIED BY 'mypassword';
GRANT ALL PRIVILEGES ON Pol_afri.* TO 'polafri_user'@'localhost';
FLUSH PRIVILEGES;