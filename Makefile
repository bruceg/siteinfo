compile:
	@set -x && for py in *.py; do python -c "import $${py%%.py}"; done
