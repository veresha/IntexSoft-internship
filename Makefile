start:
	docker compose --env-file .env up --build

makemigr:
	alembic revision --autogenerate -m 'migr'

migrate:
	alembic upgrade head

