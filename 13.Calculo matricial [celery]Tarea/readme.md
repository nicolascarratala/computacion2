#Pasos para levantar

antes que todo: 

pyhton3 -m venv venv
pip3 install -r requirements.txt

primero:

docker compose up

segundo:

celery -A main worker --loglevel=INFO -c4

tercero:

python3 calc.py -f file.txt -c log|raiz|pot
