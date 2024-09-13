class AuthRouter:

    route_app_labels = {
        "user",
        "admin",
        "contenttypes",
        "sessions",
        "auth",
    }

    def db_for_read(
        self, model, **hints
    ):  # will go to settings database and find users , so check if model inside app , if yes return db
        if model._meta.app_label in self.route_app_labels:
            return "users"
        return None

    def db_for_write(self, model, **hints):  # write
        if model._meta.app_label in self.route_app_labels:
            return "users"
        return None

    def allow_relation(
        self, obj1, obj2, **hints
    ):  # model relation inside app , so the user database can have relation ONLY WITH  models in user
        if (
            obj1._meta.app_label in self.route_app_labels
            or obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(
        self, db, app_label, model_name=None, **hints
    ):  # only models from user app can only appear in users database
        if app_label in self.route_app_labels:
            return db == "users"
        return None
