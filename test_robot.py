import robot

motor = robot.Motor("TestMotor")
bot = robot.Robot("Test Robot")


def test_init_motor():
    assert motor.name == "TestMotor"


def test_default_power():
    assert motor.get_power() == 0.0


def test_set_power():
    motor.set_power(5.0)
    assert motor.get_power() == 5.0


def test_stop_motor():
    motor.set_power(5.0)
    motor.stop()
    assert motor.get_power() == 0.0


def test_go_motor():
    motor.go(10.0)
    assert motor.get_power() == 10.0


def test_init_robot():
    assert bot.name == "Test Robot"


def test_robot_go():
    bot.go(10.0)
    assert bot.left_back.get_power() == 10.0


def test_robot_stop():
    bot.go(10.0)
    bot.stop()
    assert bot.left_back.get_power() == 0.0


def test_robot_motor_power():
    bot.go(10.0)
    assert (
        bot.left_back.power
        == bot.left_front.power
        == bot.right_back.power
        == bot.right_front.power
    )
