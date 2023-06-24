# Hospital map

Интерактивная карта, где можно будет добавить рассположение больниц или других мест

## Установка и запуск

1. Убедитесь, что у вас установлен Python версии 3.11. и Django
2. 
   Клонируйте репозиторий с проектом:


       git clone https://github.com/your-username/your-project.git


3. Перейдите в директорию проекта:


      cd mysite

   3.1Создайте виртуальное окружение и активируйте его:

На Windows:

      python -m venv myenv

      myenv\Scripts\activate
      
На macOS и Linux:

      python3 -m venv myenv

      source myenv/bin/activate

4. Установите зависимости, используя утилиту pip:


    pip install -r requirements.txt

5. Запустите миграции базы данных:


    python3 manage.py migrate

6. Запустите сервер разработки:


    python3 manage.py runserver


