class BolosExceptionError(Exception):
    # Excepción General
    def __init__(self):
        super().__init__("Error del sistema")


class LanzamientoInvalidoError(Exception):
    # indicar que se ha intentado realizar un lanzamiento inválido,
    # como lanzar más de 2 veces en un frame normal o
    # más de 3 veces en el frame 10.
    def __init__(self, motivo: str):
        super().__init__(f"Lanzamiento invalido: {motivo}")


class FrameIncompletoEXceptionError(Exception):
    # indicar que se intenta calcular el puntaje de un frame
    # que no ha sido completado (no se han realizado todos los
    # lanzamientos permitidos).
    def __init__(self):
        super().__init__("Frame incompleto")


class FrameInexisenteExceptionError(Exception):
    # indicar que se intenta acceder a un frame que no existe
    # (por ejemplo, al calcular el puntaje de un spare y no
    # hay un frame siguiente).
    def __init__(self, mensaje):
        super().__init__(mensaje)


class RollExtraInvalidoExceptionError(Exception):
    # indicar que se intenta agregar un roll extra en un caso inválido,
    # como en un open frame o cuando ya se ha
    # utilizado el roll extra anterior.
    def __init__(self):
        super().__init__("No se puede agregar roll extra si no es strike o spare")
        