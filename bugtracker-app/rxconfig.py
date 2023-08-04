import reflex as rx

class BugtrackerappConfig(rx.Config):
    pass

config = BugtrackerappConfig(
    app_name="bugtracker_app",
    db_url="sqlite:///reflex.db",
    env=rx.Env.DEV,
)