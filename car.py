class Car(object):
    def __init__(self, name='General', model='GM' ,car_type='honda' ):
        self.car_type = car_type
        self.model = model
        self.name = name
        self.speed = 0


    def doors(self, num_of_doors):
        if name == 'Porsche' or name == 'Agera R':
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if car_type == 'trailer':
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4
            return self
        
    def wheels(self, num_of_wheels):
        return num_of_wheels

    def drive(self, moving_man):
        return moving_man

    def drive(self, speeds):
        if self.car_type == 'trailer':
            self.speed = speeds * 11
        else:
            self.speed = 10 ** speeds

        return self


    def is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
            return True
