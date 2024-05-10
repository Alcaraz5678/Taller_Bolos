from abc import ABC, abstractmethod
from typing import Optional
from main.model.excepciones import BolosException, LanzamientoInvalido, FrameIncompletoEXception, \
    FrameInexisenteException, RollExtraInvalidoException


class Frame(ABC):
    def __init__(self):
        self.rolls: list = []

    @abstractmethod
    def agregar_roll(self, pins: int):
        pass

    @abstractmethod
    def calcular_puntaje(self) -> int:
        pass


class FrameNormal(Frame):
    def __init__(self):
        super().__init__()
        self.proximo_frame: Optional[Frame] = None

    def agregar_roll(self, pins: int):
        if len(self.rolls) < 2:
            self.rolls.append(pins)
        else:
            raise ValueError("Ya se han hecho todos los lanzamientos permitidos")

    def calcular_puntaje(self) -> int:
        puntaje = sum(self.rolls)
        if self.es_open_frame():
            return puntaje
        if self.proximo_frame is not None:
            if self.es_spare():
                puntaje += self.proximo_frame.rolls[0]
                return puntaje
            if self.es_strike():
                puntaje += sum(self.proximo_frame.rolls)
                return puntaje
        else:
            raise

    def es_strike(self) -> object:
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def es_spare(self):
        return sum(self.rolls) == 10 and not self.es_strike()

    def es_open_frame(self):
        return len(self.rolls) == 2 and sum(self.rolls) < 10


class Frame10(Frame):
    def __init__(self):
        super().__init__()
        self.roll_extra: int | None = None

    def calcular_puntaje(self) -> int:
        pass

    def agregar_roll(self, pins: int):
        if len(self.rolls) < 3:
            self.rolls.append(pins)
            if self.es_strike() or self.es_spare():
                self.agregar_roll_extra(pins)
        else:
            raise ValueError("Ya se han hecho todos los lanzamientos permitidos")

    def es_strike(self) -> object:
        return len(self.rolls) == 1 and self.rolls[0] == 10

    def es_spare(self):
        return sum(self.rolls) == 10 and not self.es_strike()

    def es_open_frame(self):
        return len(self.rolls) == 2 and sum(self.rolls) < 10

    def agregar_roll_extra(self, pins: int):
        if self.es_strike() or self.es_spare():
            self.roll_extra = pins
        else:
            raise ValueError("No se puede agregar roll extra si no es strike o spare")
