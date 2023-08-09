JAZZMIN_SETTINGS = {
    # Исправим смотря на тз
    "site_title": "Site",  # Заголовок сайта
    "site_header": "Site",  # Заголовок на экране входа
    "site_brand": "Django administrations",  # Выходит на сайте вместо Django-admin.(Администрирование сайта)
    "welcome_sign": "Welcome to the my work",  # Приветственный текст на экране входа
    "copyright": "Retmind",  # Авторское право (footer)
    "search_model": ["auth.User", "auth.Group"],
    # Для поиска пользователей или группы

    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},

        # telega
        {"name": "Support", "url": "https://t.me/Savadatsu", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],

    "show_sidebar": True,

    "changeform_format": "horizontal_tabs",

}
JAZZMIN_UI_TWEAKS = {
    # белый фон:
    # "theme": "flatly",
    # "theme" : "simplex",  # белый фон с цветами - RGB
    # cartoon
    # "theme": "sketchy",

    # темный фон:
    "theme": "darkly",
    # "theme": "slate",    # темный (серьезный , полностью)

}
