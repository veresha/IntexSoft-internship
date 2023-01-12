start:
	docker compose --env-file .env up --build

makemigr:
	alembic revision --autogenerate -m "initial"

migrate:
	alembic upgrade head

