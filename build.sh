#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

# ▼ ここを追加！「もし管理者がいなければ、自動で作ってね」という命令です
python manage.py createsuperuser --noinput || true