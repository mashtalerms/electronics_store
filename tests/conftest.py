from pytest_factoryboy import register

import tests.factories as factories


register(factories.UserFactory)

pytest_plugins = 'tests.fixtures'
