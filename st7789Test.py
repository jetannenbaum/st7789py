from machine import Pin, SPI
import st7789py
import vga2_16x16_dec as font

spi1 = SPI(1, baudrate=31250000, polarity=1, phase=0, sck=Pin(14),mosi= Pin(15))
tft = st7789py.ST7789(spi1, 240, 320, reset=Pin(11, Pin.OUT), cs=Pin(13, Pin.OUT), dc=Pin(12, Pin.OUT), backlight=Pin(10, Pin.OUT), rotation=0)

tft.fill_circle(100, 100, 50, st7789py.color565(255, 0, 255))

tft.text(font, "Hello World", 0, 0)
