from abc import ABC, abstractmethod

class AbstractVehicle(ABC):
    def _init_(self,colour,num_tyre,gears):
        self.colour=colour
        self.num_tyre=num_tyre
        self.gears=gears

    @abstractmethod
    def display_details(self):
        pass