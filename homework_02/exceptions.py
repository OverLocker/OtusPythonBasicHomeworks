# """
# Объявите следующие исключения:
# - LowFuelError
# - NotEnoughFuel
# - CargoOverload
# """
# class LowFuelError(BaseException):
#     pass
#

class LowFuelError(BaseException):
    pass


class NotEnoughtFuel(BaseException):
    pass


class CargoOverload(BaseException):
    pass