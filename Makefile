install: # установка и синхронизация зависимостей
	uv sync
brain-games: # запуск приложения "Игры разума"
	uv run brain-games
build: # собрать проект
	uv build
package-install: # установить пакет
	uv tool install dist/*.whl
