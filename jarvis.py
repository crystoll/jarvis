from dotenv import dotenv_values
import os


config = {
    **dotenv_values('.env'),
    **os.environ,
}


if __name__ == "__main__":
    print("hello")
