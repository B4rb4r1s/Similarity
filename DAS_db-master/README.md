Докер файл и скрипт базы данных для **Системы Автоматизации Документооборота**.
Название образа должно соответствовать "happy_db", сборка образа:
  ```docker build -t happy_db .```
После борки, нужно поднять compose из [docker-compose](https://github.com/B4rb4r1s/DocumentAnalysisSystem/blob/main/docker-compose.yaml).
Когда контейнер развернётся, нужно запустить скрипт, создающий таблицы:
  ```docker-compose exec -it postgre bash /tmp/init_db.sh```
База данных готова к работе!
