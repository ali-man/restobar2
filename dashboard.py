from admin_tools.dashboard import modules, Dashboard


class MyModule(modules.DashboardModule):

    def is_empty(self):
        return self.message == ''

    def __init__(self, **kwargs):
        super(MyModule, self).__init__(**kwargs)
        self.template = 'my_blocks/hello.html'
        self.message = kwargs.get('message', '')


class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)

        self.children.append(
            modules.Group(
                title='Main',
                display='tabs',
                children=[
                    modules.ModelList(
                        title='Web-site',
                        models=(
                            'www.models.Profile',
                            'www.models.NewsProject',
                            'www.models.Articles',
                            'www.models.NewsMinecraft',
                            'www.models.NewFlatPage',
                        )
                    ),
                    modules.ModelList(
                            title='Forum',
                            models=(
                                'www.models.Profile',
                                )
                            ),
                    modules.ModelList(
                        title='API',
                        models=(
                            'www.models.Profile',
                        ),
                    ),
                    # modules.ModelList(
                    #     title='Accounts',
                    #     models=(
                    #         'django.contrib.auth.*',
                    #     ),
                    # ),
                    modules.ModelList(
                        title='Static pages',
                        models=(
                            'django.contrib.flatpages.*',
                            'django.contrib.sites.*',
                        ),
                    ),
                ]
            )
        )

        self.children.append(
            modules.ModelList(
                title='Пользователи',
                models=(
                    'django.contrib.auth.*',
                    'accounts.models.Profile',
                )
            )
        )

        self.children.append(
            modules.LinkList(
                title='Быстрые ссылки',
                children=[
                    {
                        'title': 'Forum',
                        'url': '/film/',
                        'external': False,
                        'attrs': {'target': '_blank'},
                    },
                    {
                        'title': 'API',
                        'url': '/film/parser/',
                        'external': False,
                        'attrs': {'target': '_blank'},
                    },
                    {
                        'title': '/accounts/login/',
                        'url': '/accounts/login/',
                        'external': False,
                        'attrs': {'target': '_blank'},
                    },
                ]
            )
        )