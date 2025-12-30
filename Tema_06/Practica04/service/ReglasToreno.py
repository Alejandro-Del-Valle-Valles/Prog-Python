class ReglasTorneo:

    @classmethod
    def calcular_danyo(cls, danyo: int, defensa: int):
        """
        Calcula el daño final que recibe el ente en base al daño base de su enemigo y a la defenesa del propio ente.
        
        :param cls: Class
        :param danyo: Daño base a inflingir
        :type danyo: int
        :param defensa: Defensa de la entidad que recibe el daño.
        :type defensa: int
        :return: daño inflingido.
        :rtype: int
        """
        return danyo if defensa <= 0 else danyo - defensa//2