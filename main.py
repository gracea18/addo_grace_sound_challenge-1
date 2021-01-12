while True:
    input.sound_level()

    if input.sound_level() > 5:
        light.set_pixel_color(0, light.rgb(255, 128, 0))
        pause(100)
        light.set_pixel_color(1, light.rgb(239, 255, 11))
        pause(100)
        light.set_pixel_color(2, light.rgb(26, 255,0))
        pause(100)
        light.set_pixel_color(3, light.rgb( 0, 255, 175))
        pause(100)
        light.set_pixel_color(4, light.rbg())
        
