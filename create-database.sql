CREATE DATABASE cardcollector;

CREATE USER card_admin WITH PASSWORD 'password';

GRANT ALL PRIVILEGES ON DATABASE cardcollector TO card_admin;

