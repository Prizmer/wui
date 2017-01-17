--CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
INSERT INTO tcpip_settings(
             guid, ip_address, ip_port, write_timeout, read_timeout, attempts, 
            delay_between_sending)
    VALUES ( uuid_generate_v4(), '192.168.127.211', 21111, 200, 400, 3,400)
    returning guid