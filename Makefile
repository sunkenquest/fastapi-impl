run:
	uvicorn app.main:app --reload

front:
	cd frontend && npm run dev

intest:
	pytest -v app/tests/in_test/user_tests.py
	pytest -v app/tests/in_test/shop_item_tests.py
