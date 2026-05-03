# Low Stock Alerts and Notifications
# Alert system for inventory management

class AlertManager:
    def __init__(self):
        self.alerts = []
        self.threshold = 5

    def check_low_stock(self, sku, current_level):
        if current_level <= self.threshold:
            alert = {
                "sku": sku,
                "level": current_level,
                "severity": "high" if current_level == 0 else "medium",
                "message": f"Low stock alert for {sku}"
            }
            self.alerts.append(alert)
            return alert
        return None

    def get_active_alerts(self):
        return self.alerts
