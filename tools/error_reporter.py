import logging

class ErrorReporter:
    @staticmethod
    def generate_report(exception):
        logging.error(f"Произошла ошибка: {exception}", exc_info=True)

        print(f"Ошибка: {exception}. Подробности сохранены в логах.")