#Pasos para levantar

antes que todo: 

pyhton3 -m venv venv
pip3 install -r requirements.txt

1:

en otra consola ejecutar:

docker compose up

2:

en otra consola ejecutar:

celery -A main worker --loglevel=INFO -c4

3:

en otra consola ejecutar:

python3 calc.py -f file.txt -c log|raiz|pot
