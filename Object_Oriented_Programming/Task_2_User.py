import Task_2

TAKE_A_PHOTO = 1
SEE_THE_STATUS = 2
CAMERA_DETAILS = 3
SEE_THE_FULLNESS_OF_CAMERA = 4
CLEAR_THE_MEMORY = 5
QUIT = 6


def main():
    OwnCamera = camera_configuration()
    OwnCamera.turn_on()
    choice = 0
    while choice != QUIT:
        choice = menu(OwnCamera)
        if choice == TAKE_A_PHOTO:
            OwnCamera.take_photo()
        elif choice == SEE_THE_STATUS:
            OwnCamera.is_camera_on()
        elif choice == CAMERA_DETAILS:
            OwnCamera.get_camera_info()
        elif choice == SEE_THE_FULLNESS_OF_CAMERA:
            OwnCamera.view_photos()
        elif choice == CLEAR_THE_MEMORY:
            OwnCamera.clear_memory()
    OwnCamera.turn_off()


def camera_configuration():
    brand = input('Enter the brand of your camera: ')
    model = input('Enter the model of your camera: ')
    resolution = input('Enter the resolution of your camera (in format WIDTH x HEIGHT): ')
    memory = int(input('Enter size of memory for your camera: '))
    return Task_2.PhotoCamera(brand, model, resolution, False, memory, 0)


def menu(camera_object):
    print()
    print('Menu')
    print('-----')
    print('"1" - Take a photo.')
    print('"2" - See the status of camera.')
    print('"3" - See the camera details.')
    print('"4" - See the fullness of memory.')
    print('"5" - Clear the camera memory.')
    print('"6" - Turn off the camera.')
    print('-----')
    choice = int(input('Enter you choice: '))
    print()
    if TAKE_A_PHOTO <= choice <= QUIT:
        return choice
    else:
        print('Enter a correct choice!')
        menu(camera_object)


main()
