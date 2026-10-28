import os
import streamlit as st


def get_setting(key):
    try:
        value = st.secrets[key]
        if value is not None:
            return str(value)
    except (KeyError, FileNotFoundError):
        pass

    return os.getenv(key)


DB_PORT = get_setting("DB_PORT")

DB_CONFIG = {
    "host": get_setting("DB_HOST"),
    "port": int(DB_PORT or "5432"),
    "database": get_setting("DB_NAME"),
    "user": get_setting("DB_USER"),
    "password": get_setting("DB_PASSWORD"),
}
