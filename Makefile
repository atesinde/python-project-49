install: # установка и синхронизация зависимостей
	uv sync
brain-games: # запуск приложения "Игры разума"
	uv run brain-games
build: # собрать проект
	uv build
package-install: # установить пакет
	uv tool install dist/*.whl
package-reinstall: # переустановить пакет после изменений
	uv tool install --force dist/hexlet_code-0.1.0-py3-none-any.whl
lint: # запустить проверку линтера ruff
	uv run ruff check brain_games
