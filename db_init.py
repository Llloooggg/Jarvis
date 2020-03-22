from db_routing import add_trigger, add_action


def db_fill():
    add_trigger('Тест', 'test_trigger')
    add_trigger('Будильник', 'alarm_clock')
    add_trigger('Проверить почту', 'check_email')

    add_action('Тест', 'test_action')
