import os
import pygame

def main():
    image_name = ''

    found_images = []
    for image_file in os.listdir():
        dot = False
        ext = ''
        for char in image_file:
            if char == '.':
                dot = True
                continue
            if dot:
                ext += char.lower()

        if ext in ['jpg', 'jpeg', 'png']:
            found_images.append(image_file)

    if found_images == []:
        raise Exception("Couldn't find an image with extension .jpg .jpeg or .png")

    elif len(found_images) > 1:
        while True:
            for image_file in found_images:
                print(image_file, end=" ")
            print()
            image_name = input("Which image do you want to use? ")

            if image_name in found_images:
                break
            else:
                print("Input the name of one of these files:")

    else:
        image_name = found_images[0]

    image = pygame.image.load(image_name)

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(image.get_rect().size)
    font = pygame.font.SysFont('Arial', 20)

    with open("coords.txt", 'w') as f:
        f.truncate(0)
        f.close()

    rects = open("coords.txt", 'a')
    coords = []
    clock = pygame.time.Clock()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                return

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                coords.append((x, y))
                rects.write(f"{x}, {y}\n")

            elif event.type == pygame.MOUSEBUTTONUP:
                pass

        screen.fill(pygame.Color('grey'))
        screen.blit(image, image.get_rect())

        #Dots for previously selected points
        for coord in coords:
            pygame.draw.circle(screen, pygame.Color(0, 0, 0), coord, 5)

        #Top left coord text
        text = font.render(str(pygame.mouse.get_pos()), False, (0, 0, 0))
        pygame.draw.rect(screen, pygame.Color(255, 255, 255), text.get_rect())
        screen.blit(text, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    rects.close()

if __name__ == '__main__':
    main()