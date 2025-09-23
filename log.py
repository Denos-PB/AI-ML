import logging

logging.basicConfig(
    filename="app.log",
    filemode="w",
    level=logging.INFO,
    format="%(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger()  # root logger


def average(numbers):
    try:
        if len(numbers) == 0:
            raise ValueError(logging.debug("The list is empty"))




average([1, 2, 3, 4, 5])
average([10, -20, -30])
average([])
average([1, 2, 3, 0, 5])
average([1, 2, "three", 4, 5])