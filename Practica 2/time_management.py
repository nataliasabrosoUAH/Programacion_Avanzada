"""Práctica 2 de Programación Avanzada: gestión de horas."""

import re


class Time:
    """Representa una hora en formato AM, PM o 24 HOURS."""

    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    # Método de instancia: inicializa los datos propios de cada objeto.
    def __init__(self) -> None:
        """Inicializa la hora a las 00:00:00 en formato de 24 horas."""
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.__time_format = "24 HOURS"
        type(self).time_count += 1

    # Propiedad de instancia: permite consultar las horas del objeto.
    @property
    def hours(self) -> int:
        """Devuelve las horas almacenadas."""
        return self.__hours

    # Propiedad de instancia: permite consultar los minutos del objeto.
    @property
    def minutes(self) -> int:
        """Devuelve los minutos almacenados."""
        return self.__minutes

    # Propiedad de instancia: permite consultar los segundos del objeto.
    @property
    def seconds(self) -> int:
        """Devuelve los segundos almacenados."""
        return self.__seconds

    # Propiedad de instancia: permite consultar el formato del objeto.
    @property
    def time_format(self) -> str:
        """Devuelve el formato de hora almacenado."""
        return self.__time_format

    # Método de instancia: valida y cambia el formato de este objeto.
    def __assign_format(self, time_format: str) -> bool:
        """Asigna un formato válido, convertido a mayúsculas.

        Args:
            time_format: Formato AM, PM o 24 HOURS.

        Returns:
            True si se pudo asignar; False en caso contrario.
        """
        if not isinstance(time_format, str):
            return False
        normalized_format = time_format.strip().upper()
        if self.is_valid_format(normalized_format):
            self.__time_format = normalized_format
            return True
        return False

    # Método de instancia: consulta el formato guardado en este objeto.
    def __is_24hour_format(self) -> bool:
        """Indica si el formato almacenado es 24 HOURS."""
        return self.__time_format == "24 HOURS"

    # Método de instancia: comprueba los valores según el formato del objeto.
    def _is_valid_time(self, hours: int, minutes: int, seconds: int) -> bool:
        """Comprueba que la hora, los minutos y los segundos son válidos.

        Args:
            hours: Hora que se desea comprobar.
            minutes: Minutos que se desean comprobar.
            seconds: Segundos que se desean comprobar.

        Returns:
            True cuando todos los valores son válidos.
        """
        if not all(type(value) is int for value in (hours, minutes, seconds)):
            return False
        if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
            return False
        if self.__is_24hour_format():
            return 0 <= hours <= 23
        return 1 <= hours <= 12

    # Método de instancia: actualiza la hora almacenada en este objeto.
    def set_time(
        self, hours: int, minutes: int, seconds: int, time_format: str
    ) -> bool:
        """Asigna una hora si el formato y los valores son correctos.

        Args:
            hours: De 0 a 23 en 24 HOURS, o de 1 a 12 en AM/PM.
            minutes: De 0 a 59.
            seconds: De 0 a 59.
            time_format: AM, PM o 24 HOURS.

        Returns:
            True si se asignó la hora; False si la entrada era incorrecta.
        """
        previous_format = self.__time_format
        if not self.__assign_format(time_format):
            return False
        if not self._is_valid_time(hours, minutes, seconds):
            self.__time_format = previous_format
            return False

        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds
        return True

    # Método de instancia: consulta los datos guardados en este objeto.
    def get_time(self) -> tuple[int, int, int, str]:
        """Devuelve horas, minutos, segundos y formato almacenados."""
        return (self.hours, self.minutes, self.seconds, self.time_format)

    # Método de clase: construye una instancia de la clase a partir de texto.
    @classmethod
    def from_string(cls, time_string: str) -> "Time | None":
        """Crea un Time a partir de 'HH:MM:SS FORMATO'.

        Args:
            time_string: Cadena como '14:30:00 24 HOURS' o '02:45:30 PM'.

        Returns:
            Un objeto Time válido o None si la cadena es incorrecta.
        """
        if not isinstance(time_string, str):
            print("Error: la hora debe introducirse como texto.")
            return None

        pattern = r"^\s*(\d{2}):(\d{2}):(\d{2})\s+(AM|PM|24 HOURS)\s*$"
        match = re.match(pattern, time_string, re.IGNORECASE)
        if match is None:
            print("Error: usa el formato HH:MM:SS AM, PM o 24 HOURS.")
            return None

        hours, minutes, seconds = (int(number) for number in match.group(1, 2, 3))
        time_format = match.group(4)
        # Comprobamos los rangos antes de crear el objeto, para no contarlo
        # si la hora no es válida.
        normalized_format = time_format.upper()
        if not (0 <= minutes <= 59 and 0 <= seconds <= 59):
            print("Error: los minutos y segundos deben estar entre 0 y 59.")
            return None
        if normalized_format == "24 HOURS":
            valid_hours = 0 <= hours <= 23
        else:
            valid_hours = 1 <= hours <= 12
        if not valid_hours:
            print("Error: las horas no están dentro del rango del formato.")
            return None

        new_time = cls()
        new_time.set_time(hours, minutes, seconds, normalized_format)
        return new_time

    # Método estático: valida un texto sin necesitar una instancia ni clase.
    @staticmethod
    def is_valid_format(time_format: str) -> bool:
        """Devuelve True si el formato es AM, PM o 24 HOURS."""
        return (
            isinstance(time_format, str)
            and time_format.strip().upper() in Time.TIME_FORMATS
        )

    # Método de clase: consulta el contador que comparten sus instancias.
    @classmethod
    def get_time_count(cls) -> int:
        """Devuelve el número de objetos Time creados."""
        return cls.time_count


def display_time(time: Time) -> str:
    """Obtiene la representación HH:MM:SS FORMATO de un objeto Time."""
    hours, minutes, seconds, time_format = time.get_time()
    return f"{hours:02d}:{minutes:02d}:{seconds:02d} {time_format}"


def main() -> None:
    """Ejecuta el menú de gestión de horas hasta que se elige terminar."""
    current_time = Time()

    while True:
        print("\n--- GESTIÓN DE HORAS ---")
        print("1. Introducir una nueva hora")
        print("2. Visualizar hora")
        print("3. Crear una hora a partir de una cadena")
        print("4. Terminar")
        option = input("Elige una opción (1-4): ").strip()

        if option == "1":
            try:
                hours = int(input("Horas: "))
                minutes = int(input("Minutos: "))
                seconds = int(input("Segundos: "))
                time_format = input("Formato (AM, PM o 24 HOURS): ")
            except ValueError:
                print("Error: horas, minutos y segundos deben ser enteros.")
                continue

            if current_time.set_time(hours, minutes, seconds, time_format):
                print("Hora guardada correctamente.")
            else:
                print("Error: hora o formato no válidos.")

        elif option == "2":
            print("Hora actual:", display_time(current_time))

        elif option == "3":
            time_string = input("Introduce la hora (HH:MM:SS FORMATO): ")
            created_time = Time.from_string(time_string)
            if created_time is not None:
                current_time = created_time
                print("Hora creada correctamente:", display_time(current_time))

        elif option == "4":
            print("Programa terminado.")
            break
        else:
            print("Error: selecciona una opción entre 1 y 4.")


if __name__ == "__main__":
    main()
