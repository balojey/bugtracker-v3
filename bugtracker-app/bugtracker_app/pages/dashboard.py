from ..components.components import base_layout, dashboard_charts


def dashboard():
    """Dashboard page"""
    return base_layout(dashboard_charts())
