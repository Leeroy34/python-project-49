install:
		poetry install

brain-games:
		poetry run brain-games

brain-even:
		poetry run brain-even

brain-calc:
		poetry run brain-calc

brain-gcd:
		poetry run brain-gcd

brain-progression:
		poetry run brain-progression

brain-prime:
		poetry run brain-prime

build:
		poetry build

publish:
		poetry publish --dry-run

package-install:
		python3 -m pip install --user dist/*.whl

lint-brain-calc:
		poetry run flake8 brain_games/games/brain_calc.py

lint-brain-even:
		poetry run flake8 brain_games/games/brain_even.py

lint-brain-gcd:
		poetry run flake8 brain_games/games/brain_gcd.py

lint-brain-prime:
		poetry run flake8 brain_games/games/brain_prime.py

lint-brain_progression:
		poetry run flake8 brain_games/games/brain_progression.py