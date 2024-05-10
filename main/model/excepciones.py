class BolosException(Exception):
    # Excepción General
    pass


class LanzamientoInvalido(Exception):
    # indicar que se ha intentado realizar un lanzamiento inválido,
    # como lanzar más de 2 veces en un frame normal o
    # más de 3 veces en el frame 10.
    pass


class FrameIncompletoEXception(Exception):
    # indicar que se intenta calcular el puntaje de un frame
    # que no ha sido completado (no se han realizado todos los
    # lanzamientos permitidos).
    pass


class FrameInexisenteException(Exception):
    # indicar que se intenta acceder a un frame que no existe
    # (por ejemplo, al calcular el puntaje de un spare y no
    # hay un frame siguiente).
    pass


class RollExtraInvalidoException(Exception):
    # indicar que se intenta agregar un roll extra en un caso inválido,
    # como en un open frame o cuando ya se ha
    # utilizado el roll extra anterior.
    pass