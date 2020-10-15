openssl req -new -newkey rsa:1024 -nodes -out ca.csr -keyout ca.key -config "openssl.cnf"
pause
openssl x509 -trustout -signkey ca.key -days 365 -req -in ca.csr -out ca.pem
pause
openssl genrsa -out client.key 1024
pause
openssl req -new -key client.key -out client.csr -config "openssl.cnf"
pause
openssl ca -in client.csr -out client.cer -config "openssl.cnf"
pause
openssl pkcs12 -export -out ISARA_client.p12 -inkey client.key -in client.cer -certfile ca.pem
pause