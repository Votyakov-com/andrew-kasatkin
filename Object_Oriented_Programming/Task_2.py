class PhotoCamera:
    def __init__(self, brand, model, resolution, is_on, memory_capacity, photos):
        self.__brand = brand
        self.__model = model
        self.__resolution = resolution
        self.__is_on = is_on
        self.__memory_capacity = memory_capacity
        self.__photos = photos

    def take_photo(self):
        result=PhotoCamera.store_photo(self)
        if result is True:
            self.__photos+=1
            print(f'Photo with resolution {self.__resolution} is done and saved.')
        else:
            print(f'Your memory is full.')

    def get_camera_info(self):
        print('Details of camera: ')
        print(f'Brand: {self.__brand}')
        print(f'Model: {self.__model}')
        print(f'Resolution: {self.__resolution}')

    def turn_on(self):
        self.__is_on = True
        print('Your camera is turn on.')

    def turn_off(self):
        self.__is_on = False
        print('Your camera is turn off.')

    def is_camera_on(self):
        result = self.__is_on
        if result is True:
            print('Your camera is on.')
        elif result is False:
            print('Your camera is off.')

    def store_photo(self):
        if self.__photos < self.__memory_capacity:
            return True
        else:
            return False

    def view_photos(self):
        print(f'Total number of saved photos: {self.__photos}')

    def clear_memory(self):
        self.__photos=0