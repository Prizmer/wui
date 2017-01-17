-- drop rule if exists rule add_to_link_tcpip_100 on link_meters_comport_settings
create or replace rule add_to_link_tcpip_100 as
on delete
to link_meters_comport_settings
do also

INSERT INTO link_meters_tcpip_settings(
            guid, guid_meters, guid_tcpip_settings)
    VALUES (uuid_generate_v4(), OLD.guid_meters, 'a8799480-0971-4465-a26e-18a8bca76e9e' );

/* 
"bb8b1dd1-7b00-4b48-8c3e-c1dcb965a444";"192.168.127.203";2032
"2c4928b7-2f07-4bb9-95b5-fa3eed42392e";"192.168.127.203";2033
"9a4f72b4-e5e1-4ce9-9769-8498e1db89f3";"192.168.127.203";2034
"c4a9c84f-cd25-4201-8737-529db12925f1";"192.168.127.203";2035
"916be8c1-88f7-45eb-bf06-e7fac0c71264";"192.168.127.203";2036
"5c63ede8-2eef-40a8-9910-eec2d47ff0aa";"192.168.127.204";2047
"89a51c48-1620-4926-a058-91f993554fda";"192.168.127.204";2048
"d972288c-de0a-4b28-9609-44f3c99c2055";"192.168.127.204";2049
"a8799480-0971-4465-a26e-18a8bca76e9e";"192.168.127.211";21111
*/