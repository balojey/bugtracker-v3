import reflex as rx

class FrontendConfig(rx.Config):
    pass

config = FrontendConfig(
    app_name="frontend",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)