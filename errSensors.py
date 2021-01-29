from errbot import BotPlugin, botcmd, arg_botcmd, webhook


class errSensors(BotPlugin):
    """
    Show the results of reading sensors attached to my Raspberry Pi.
    """

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

