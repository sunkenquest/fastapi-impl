run:
	uvicorn app.main:app --reload

front:
	cd frontend && npm run dev

intest:
	pytest -v app/tests/in_test/user_tests.py
	pytest -v app/tests/in_test/message_tests.py
