from admin_tools.dashboard import modules, Dashboard


class MyModule(modules.DashboardModule):
    text = ' zxc s'

    def is_empty(self):
        return self.message == ''

    def __init__(self, **kwargs):
        super(MyModule, self).__init__(**kwargs)
        self.template = 'admin_dashboard/hello.html'
        # self.config = ConfigSite.objects.first()
        if self.text:
            self.message = self.text
        else:
            self.message = kwargs.get('message', '')

    def init_with_context(self, context):
        if context.request.method == 'POST':
            self.text = context.request.POST['test']


class CustomIndexDashboard(Dashboard):

    def __init__(self, **kwargs):
        Dashboard.__init__(self, **kwargs)
        self.children.append(
            MyModule(title='Настройка системы', message='Привет!')
        )
        self.children.append(
            modules.Group(
                title='Main',
                display='tabs',
                children=[
                    modules.ModelList(
                        title='Главная',
                        models=(
                            'apps.general.models.Slider',
                            'apps.general.models.ConfigSite',
                        )
                    ),
                    modules.ModelList(
                        title='Товары',
                        models=(
                            'apps.products.models.Category',
                            'apps.products.models.Manufacturer',
                            'apps.products.models.Country',
                            'apps.products.models.Product',
                            'apps.products.models.OtherInfo',
                            'apps.products.models.ConfigSite',
                        )
                    ),
                    modules.ModelList(
                        title='Static pages',
                        models=(
                            'django.contrib.flatpages.*',
                            'django.contrib.sites.*',
                        ),
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
                        'title': 'Настройки сайта',
                        'url': '/admin/products/configsite/1/change/',
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