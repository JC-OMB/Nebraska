from frontend.frontend import Frontend


class App:
    frontend = Frontend()

    @classmethod
    def run(cls):
        cls.frontend.render()
