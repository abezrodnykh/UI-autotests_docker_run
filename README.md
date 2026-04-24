В этом репозитории находится мой небольшой учебный проект с UI-тестами на Python + Pytest + Playwright. Запуск тестов настроен в Docker.

Инструкция по запуску тестов в Docker:

1. Скачайте Docker Desktop для вашей ОС: https://www.docker.com/products/docker-desktop.
Установите следуя инструкциям мастера установки.
Запустите Docker после установки

2. Формирование Dockerfile — инструкция для сборки образа - уже сформирован в проекте.

3. Сборка образа (build) — создание шаблона на основе Dockerfile:
docker build -t tests -f ci/Dockerfile .
где:                  
-t tests — присваиваем имя образу "tests"
-f ci/Dockerfile — указываем путь к Dockerfile
. — контекст сборки (текущая директория)

4. Запуск контейнера:
docker run -e BASE_URL=https://ecommerce-playground.lambdatest.io/ -e USER_LOGIN=dancegti@gmail.com -e USER_PASSWORD=1234 tests
где:                  
-e — передача переменной окружения
tests — имя образа для запуска

5. Просмотр и остановка контейнеров.
docker ps                    # Просмотр запущенных контейнеров
docker ps -a                 # Просмотр всех контейнеров (включая остановленные)
docker images                # Просмотр образов
docker stop <container_id>   # Остановка контейнера

6. Удаление.
docker rm <container_id>     # Удаление контейнера
docker rmi <image_id>        # Удаление образа
docker container prune       # Удаление всех остановленных контейнеров
docker image prune           # Удаление неиспользуемых образов
