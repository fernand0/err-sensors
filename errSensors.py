from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class errSensors(BotPlugin):
    """
    Show the results of reading sensors attached to my Raspberry Pi.
    """

    #def activate(self):
    #    """
    #    Triggers on plugin activation

    #    You should delete it if you're not using it to override any default behaviour
    #    """
    #    super(Err-sensors, self).activate()

    #def deactivate(self):
    #    """
    #    Triggers on plugin deactivation

    #    You should delete it if you're not using it to override any default behaviour
    #    """
    #    super(Err-sensors, self).deactivate()

    @botcmd(split_args_with=None) 
    def temp(self, message, args): 
        """A command which returns temperature measurement""" 
        
        from pigpio_dht import DHT22

        gpio = 4
        # The sensor is there.

        sensor = DHT22(gpio)
        result = sensor.read()
        result['valid'] = False
        # We drop the first measurement because it tends to be inaccurate

        while not result['valid']:
            import time
            time.sleep(1)
            result = sensor.read()

        temperature_c = result['temp_c']
        temperature_f = result['temp_f']
        humidity = result['humidity'] 
        res = "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format( 
                temperature_f, temperature_c, humidity)

        return res


    @botcmd(split_args_with=None) 
    def co2(self, message, args): 
        """A command which returns CO2 measurement""" 
        # pip install mh_z19
        # https://pypi.org/project/mh-z19/
        # https://esphome.io/components/sensor/mhz19.html
        # https://monitorserviceatelierueda.blogspot.com/2018/11/how-to-measure-room-co2-concentration.html
        # https://github.com/UedaTakeyuki/mh-z19/wiki/How-to-use-without-root-permission  
 
        import mh_z19 

        res = mh_z19.read_all()

        return res

    #def get_configuration_template(self):
    #    """
    #    Defines the configuration structure this plugin supports

    #    You should delete it if your plugin doesn't use any configuration like this
    #    """
    #    return {'EXAMPLE_KEY_1': "Example value",
    #            'EXAMPLE_KEY_2': ["Example", "Value"]
    #           }

    #def check_configuration(self, configuration):
    #    """
    #    Triggers when the configuration is checked, shortly before activation

    #    Raise a errbot.ValidationException in case of an error

    #    You should delete it if you're not using it to override any default behaviour
    #    """
    #    super(Err-sensors, self).check_configuration(configuration)

    #def callback_connect(self):
    #    """
    #    Triggers when bot is connected

    #    You should delete it if you're not using it to override any default behaviour
    #    """
    #    pass

    #def callback_message(self, message):
    #    """
    #    Triggered for every received message that isn't coming from the bot itself

    #    You should delete it if you're not using it to override any default behaviour
    #    """
    #    pass

    #def callback_botmessage(self, message):
    #    """
    #    Triggered for every message that comes from the bot itself

    #    You should delete it if you're not using it to override any default behaviour
    #    """
    #    pass

    #@webhook
    #def example_webhook(self, incoming_request):
    #    """A webhook which simply returns 'Example'"""
    #    return "Example"

    ## Passing split_args_with=None will cause arguments to be split on any kind
    ## of whitespace, just like Python's split() does
    #@botcmd(split_args_with=None)
    #def example(self, message, args):
    #    """A command which simply returns 'Example'"""
    #    return "Example"

    #@arg_botcmd('name', type=str)
    #@arg_botcmd('--favorite-number', type=int, unpack_args=False)
    #def hello(self, message, args):
    #    """
    #    A command which says hello to someone.

    #    If you include --favorite-number, it will also tell you their
    #    favorite number.
    #    """
    #    if args.favorite_number is None:
    #        return f'Hello {args.name}.'
    #    else:
    #        return f'Hello {args.name}, I hear your favorite number is {args.favorite_number}.'
